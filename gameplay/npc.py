
from numpy import array
from ..environment import nn_training_data
from ..environment.slp_training_data import slp_t_data
from ..ann.nn_manager import create_nn, call_nn
from ..slp.slp_manager import create_slp, call_slp
from ..fuzzy.membership_calculator import find_membership

class NPCManager(object):
	""" Controls the NPCs actions """

	def __init__(self, npc, user):
		# Store vars
		data = None
		self.npc = npc
		self.user = user

		data = None
		# Get training data
		if npc.name.upper() == 'AHRI':
			self.name = 'Ahri'
			data = nn_training_data.get_ahri()

		# Get the nerual networked trained to the npc
		self.nn = create_nn(data)
		self.slp = create_slp(slp_t_data)

		# Set the emotions of the NPC
		self.set_emotions()

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def set_emotions(self):
		"""
		Use emotions to calculate variables
		"""
		# Use a combination of whether O, C and A are high or low to determine
		# logic follows the majority of the 3 (O is inverse)
		logic_calc_inputs = [
			find_membership(self.npc.ocean.get('O'), direct=False),
			find_membership(self.npc.ocean.get('C')),
			find_membership(self.npc.ocean.get('A'))
			]

		# Count occurences of high and low in logic_calc_inputs
		if logic_calc_inputs.count('HIGH') >= 2:
			# Set logic at the highest value
			self.npc.logic = 1.0
		elif logic_calc_inputs.count('LOW') >= 2:
			# Set logic to the low value
			self.npc.logic = 0.5
		else:
			raise ValueError

		# Calculate if `E` is high or low
		self.npc.extroversion = find_membership(self.npc.ocean.get('E'))


		# N will cause the degradtion of L
			# If N is high: degradtion 0.3
			# If N is low: degradtion 0.1
		if find_membership(self.npc.ocean.get('N'))  == 'HIGH':
			self.npc.logic_degrader = 0.03
		else:
			self.npc.logic_degrader = 0.01

	# ---------- Decisions functions ------------

	def attack_or_defend(self, inputs):
		"""
		Use the SLP to calculate whether to attack or defenc
		"""
		return call_slp(self.slp, inputs)

	def choose_attack(self):
		"""
		Use the NN to choose an attack
		:rtpye: char
		:returns: The attack ability to use
		"""
		inputs = array([
			float(self.user.health),
			float(self.npc.abilities['R'].damage),
			float(self.npc.abilities['R'].useable()),
			float(self.npc.abilities['W'].damage),
			float(self.npc.abilities['W'].useable()),
			float(self.npc.abilities['Q'].damage)
		 ])
		outputs = call_nn(self.nn, inputs)
		# Emotional stuff here
		choice = None, None
		if outputs[0] > choice[1] and self._test('R'):
			choice = 'R', outputs[0]
		if outputs[1] > choice[1] and self._test('W'):
			choice = 'W', outputs[1]
		if outputs[2] > choice[1] and self._test('Q'):
			choice = 'Q', outputs[2]

		return choice[0]

	def _test(self, key):
		"""
		Tests if the key is valid and available
		:type key: char
		:param key: Q, W, E, R
		:rtype: bool
		:returns: If the key is valid and available
		"""
		if self.npc.abilities.has_key(key) and \
			self.npc.abilities.get(key).useable():
			return True
		else:
			return False

	def choose_defence(self):
		"""
		Select a defensive tactic
		:rtype: Ability()
		:returns: ability to use
		"""
		ability = self.npc.abilities.get('E')
		if ability.useable(): return 'E'
		return None
