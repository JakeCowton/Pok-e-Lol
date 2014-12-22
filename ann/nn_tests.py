
import unittest
import numpy as np
from .nn import NN, sigmoid, sigmoid_first_d

class MLPTest(unittest.TestCase):
	"""
	Tests for the MLP
	"""

	def test_create_nn(self):
		ann = NN(6,6,6,6)
		assert ann.layers[0].size == 7 # For bias
		assert ann.layers[1].size == 6
		assert ann.layers[2].size == 6
		assert ann.layers[3].size == 6

		ann = NN(5,4,3,2,1)
		assert ann.layers[0].size == 6 # For bias
		assert ann.layers[1].size == 4
		assert ann.layers[2].size == 3
		assert ann.layers[3].size == 2
		assert ann.layers[4].size == 1

	def test_sigmoid(self):
		assert sigmoid(1) == np.tanh(1)
		assert sigmoid(0.123412) == np.tanh(0.123412)
		assert sigmoid(0) == np.tanh(0)
		assert sigmoid(2) == np.tanh(2)

	def test_sigmoid_first_d(self):
		assert sigmoid_first_d(1) == 1-(1**2)
		assert sigmoid_first_d(0.123412) == 1-(0.123412**2)
		assert sigmoid_first_d(0) == 1-(0**2)
		assert sigmoid_first_d(2) == 1-(2**2)
