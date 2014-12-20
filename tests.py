import unittest
from .environment.nn_training_data import get_training_data, get_test_data
from .ann.nn_manager import find_mse, _train
from .ann.nn import NN

class NNLayerTest(unittest.TestCase):

	def setUp(self):
		self.mse_list = {}
		self.training_data = get_training_data()
		self.test_data = get_test_data()

	def tearDown(self):
		# count = 0
		# for i in range(7):
		# 	for j in range(1,7):
		# 		print "NN(6,%d,%d,3) = %s" % \
		# 			(i, j, str(self.mse_list["%s, %s" % (i, j)]))
		# 		count += 1

		print "6,%s,3 gives smallest MSE" % \
			min(self.mse_list, key=self.mse_list.get)


	def test_hidden_layer_size(self):
		"""
		Tests MLPs with different hidden layer sizes
		"""

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
