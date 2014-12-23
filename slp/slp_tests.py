
import unittest
from .slp import SLP
from .slp_manager import create_slp, _normalise

class SLPManagerTest(unittest.TestCase):
	"Tests for SLP Manager"

	def test_normalise(self):
		raw_data = [500, 212]
		normalised_data = _normalise(raw_data)
		assert normalised_data == [1.0, 0.424]

	def test_create_slp(self):

		slp_t_data = [
				 [[0.1,     0.1],      1],
				 [[0.1,     0.2],      1],
				 [[0.1,     0.3],      0],
				 [[0.1,     0.4],      0],
				 [[0.1,     0.5],      0],
				 [[0.1,     0.6],      0],
				 [[0.1,     0.7],      0],
				 [[0.1,     0.8],      0],
				 [[0.1,     0.9],      0],
				 [[0.1,     1.0],      0]]
		slp = create_slp(slp_t_data)
		assert type(slp) == SLP
