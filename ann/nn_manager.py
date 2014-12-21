# Gives access to the NN

import numpy as np
from os import system as sys
from .nn import NN

def _train(net, data, epochs=1000, lr=0.1, momentum=0.1):
	"""
	Train `net` with `data`
	:param net: the network to train
	:param data: the data to train with
	:param epochs: The number full iterations through data
	:param lr: learning rate
	:param momentum: NN momentum
	"""
	for i in range(epochs):
		# Show how long is left
		sys('clear')
		print "Loading... %d%%" % int(float(i)/epochs * 100)

		# Run one epoch
		for n in range(data.size):
			net.feed_forward(data['inputs'][n])
			net.back_propagate(data['outputs'][n], lr, momentum)
	sys('clear')

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

def _normalise(data):
	"""
	:type data: List
	:param data: List of NN inputs in this order:
	  NPC health, R damage, R availability, W damage, W availability, Q damage
	:rtype: List
	:returns: Normalised version of `data`
	"""
	health, r_dam, r_avail, w_dam, w_avail, q_dam = data

	health = float(health) / float(500)

	r_dam = float(r_dam) / float(500)

	w_dam = float(w_dam)/float(500)

	q_dam = float(q_dam) / float(500)

	return [health, r_dam, r_avail, w_dam, w_avail, q_dam]

def call_nn(nn, data):
	"""
	:type nn: NN object
	:param nn: The neural network
	:type data: array
	:param data: The input vars for the network
	:rtype: array
	:returns: The output layer
	"""

	data = _normalise(data)
	return nn.feed_forward(data)
