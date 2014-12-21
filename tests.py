import unittest
from collections import Counter
from .environment.nn_training_data import get_training_data, get_test_data
from .ann.nn_manager import find_mse, _train
from .ann.nn import NN

class NNLayerTest(unittest.TestCase):

	def setUp(self):
		self.list_of_bests = []
		self.mse_list = {}
		self.training_data = get_training_data()
		self.test_data = get_test_data()


	def test_hidden_layer_size(self):
		"""
		Tests MLPs with different hidden layer sizes
		"""
		print "test_hidden_layer_size beginning"
		for iteration in range(50):
			# First hidden layer (0 to 6)
			for i in range(7):
				# Second hidden layer (1 to 6)
				for j in range(1,7):
					# If first hidden is 0
					if not i:
						nn = NN(6, j, 3)
						_train(nn,self.training_data)
						self.mse_list["%d,%d" % (i, j)] = \
							(find_mse(nn, self.test_data))

					# If first hidden has a value
					else:
						nn = NN(6, i, j, 3)
						_train(nn, self.training_data)
						self.mse_list["%d,%d" % (i, j)] = \
							(find_mse(nn, self.test_data))

			# Store the iteration's lowest error
			iter_min = min(self.mse_list, key=self.mse_list.get)
			# Display it
			print "6,%s,3 gives smallest MSE for test %d" % \
				(iter_min, iteration)
			# Store it in a list
			self.list_of_bests.append(iter_min)
			# Clear the MSE list for next iteration
			self.mse_list.clear()

		print self.list_of_bests
		best = Counter(self.list_of_bests).most_common()[0]
		print "Most common in list: %s" % str(best)
