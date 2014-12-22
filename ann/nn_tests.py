
import unittest
import numpy as np
from .nn import NN, sigmoid, sigmoid_first_d
from .nn_manager import create_nn, _normalise

class MLPTest(unittest.TestCase):
	"Tests for MLP"

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

class MLPManagerTest(unittest.TestCase):
	"Tests for MLP Manager"

	def setUp(self):
		self.data = np.zeros(24, dtype=[('inputs',  float, 6),
			('outputs', float, 3)])
		self.data[0]  = (0.04,    0.04, 1.0,  0.02, 1.0,  0.01), \
			(1.0,  0.0,   0.0)
		self.data[1]  = (0.04,    0.04, 1.0,  0.02, 0.0,  0.01), \
			(1.0,  0.0,   0.0)
		self.data[2]  = (0.04,    0.04, 1.0,  0.02, 0.0,  0.01), \
			(1.0,  0.0,   0.0)
		self.data[3]  = (0.04,    0.04, 1.0,  0.02, 1.0,  0.01), \
			(1.0,  0.0,   0.0)
		self.data[4]  = (0.04,    0.04, 0.0,  0.02, 1.0,  0.01), \
			(0.0,  0.7,   0.5)
		self.data[5]  = (0.03,    0.04, 1.0,  0.02, 1.0,  0.01), \
			(1.0,  0.0,   0.0)
		self.data[6]  = (0.03,    0.04, 1.0,  0.02, 0.0,  0.01), \
			(1.0,  0.0,   0.0)

	def test_create_nn(self):
		nn = create_nn(self.data)
		assert type(nn) == NN

	def test_normalise(self):
		raw_data = [500, 25, 1, 35, 0, 10]
		normalised_data = _normalise(raw_data)
		assert normalised_data == [1.0, 0.05, 1.0, 0.07, 0.0, 0.02]
