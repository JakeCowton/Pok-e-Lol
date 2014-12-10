# Gives access to the NN

import numpy as np
from nn import NN

def _train(net, data, epochs=10000, lr=0.1, momentum=0.1):
	"""
	Train `net` with `data`
	"""
	for i in range(epochs):
		n = np.random.randint(data.size)
		net.feed_forward(data['inputs'][n])
		net.back_propagate(data['outputs'][n], lr, momentum)

def create_nn(data):
	"""
	Create and train the neural network
	:type data: ndarray
	:param data: Training data for the network
	:returns: A trained NN object
	"""
	ann = NN(n_ins, n_hidden, n_outs)
	_train(ann, data)
	return ann