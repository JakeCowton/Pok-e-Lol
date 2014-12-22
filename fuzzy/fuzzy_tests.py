import unittest
from .slope_calculator import down_slope, up_slope
from .membership_calculator import membership_for_low, \
								   membership_for_mid, \
								   membership_for_high, \
								   find_membership

class FuzzyTest(unittest.TestCase):

	def setUp(self):
		self.left1 = 2
		self.right1 = 3
		self.left2 = 7
		self.right2 = 8

	def test_down_slope(self):
		assert down_slope(7.5, self.left2, self.right2) == float(0.5)

	def test_up_slope(self):
		assert up_slope(7.5, self.left2, self.right2) == float(0.5)

	def test_membership_for_low(self):
		x = 0.1
		assert membership_for_low(x) is 1
		x = 0.125
		assert membership_for_low(x) is 1
		x = 0.126
		assert 0 < membership_for_low(x) < 1
		x = 0.2
		assert 0 < membership_for_low(x) < 1
		x = 0.375
		assert membership_for_low(x) is 0
		x = 0.5
		assert membership_for_low(x) is 0

	def test_membership_for_mid(self):
		x = 0.1
		assert membership_for_mid(x) is 0
		x = 0.125
		assert membership_for_mid(x) is 0
		x = 0.126
		assert 0 < membership_for_mid(x) < 1
		x = 0.374
		assert 0 < membership_for_mid(x) < 1
		x = 0.375
		assert membership_for_mid(x) is 1
		x = 0.5
		assert membership_for_mid(x) is 1
		x = 0.625
		assert membership_for_mid(x) is 1
		x = 0.626
		assert 0 < membership_for_mid(x) < 1
		x = 0.874
		assert 0 < membership_for_mid(x) < 1
		x = 0.875
		assert membership_for_mid(x) is 0
		x = 1.0
		assert membership_for_mid(x) is 0

	def test_membership_for_high(self):
		x = 0.5
		assert membership_for_high(x) is 0
		x = 0.625
		assert membership_for_high(x) is 0
		x = 0.626
		assert 0 < membership_for_high(x) < 1
		x = 0.874
		assert 0 < membership_for_high(x) < 1
		x = 0.875
		assert membership_for_high(x) is 1
		x = 1.0
		assert membership_for_high(x) is 1

	def test_find_membership(self):
		x = 0.0
		assert find_membership(x) == 'LOW'
		x = 0.124
		assert find_membership(x) == 'LOW'
		x = 0.125
		assert find_membership(x) == 'LOW'
		x = 0.126
		assert find_membership(x) == 'LOW'
		x = 0.374
		assert find_membership(x) == 'MID'
		x = 0.375
		assert find_membership(x) == 'MID'
		x = 0.5
		assert find_membership(x) == 'MID'
		x = 0.625
		assert find_membership(x) == 'MID'
		x = 0.626
		assert find_membership(x) == 'MID'
		x = 0.874
		assert find_membership(x) == 'HIGH'
		x = 0.875
		assert find_membership(x) == 'HIGH'
		x = 1.0
		assert find_membership(x) == 'HIGH'