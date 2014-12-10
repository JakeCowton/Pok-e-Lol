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
	ann = NN(6,3,3)
	_train(ann, data)
	return ann

def call_nn(nn, data):
	"""
	:type nn: NN object
	:param nn: The neural network
	:type data: array
	:param data: The input vars for the network
	:rtype: array
	:returns: The output layer
	"""
	return nn.feed_forward(data)
