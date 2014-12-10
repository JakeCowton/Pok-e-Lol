# Training data for champions

import numpy as np

def get_ahri():
	"""
	Training data for Ahri champion
	"""
	# Available
	AVAIL = 1.0
	# On Cooldown
	ON_CD = 0.0

	# Declare the structure of the training data
	t_data = np.zeros(24, dtype=[('inputs',  float, 6), ('outputs', float, 3 )])

	# Set the training data
	t_data[0]  = (0.04,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
	t_data[1]  = (0.04,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
	t_data[2]  = (0.04,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
	t_data[3]  = (0.04,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
	t_data[4]  = (0.04,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  0.7,   0.5)
	t_data[5]  = (0.03,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
	t_data[6]  = (0.03,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
	t_data[7]  = (0.03,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
	t_data[8]  = (0.03,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
	t_data[9]  = (0.03,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  0.8,   0.2)
	t_data[10] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
	t_data[11] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
	t_data[12] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
	t_data[13] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
	t_data[14] = (0.02,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
	t_data[15] = (0.02,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  1.0,   0.0)
	t_data[16] = (0.02,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  1.0,   0.0)
	t_data[17] = (0.01,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   1.0)
	t_data[18] = (0.01,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   1.0)
	t_data[19] = (0.01,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
	t_data[20] = (0.01,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
	t_data[21] = (0.01,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
	t_data[22] = (1.0,     0.04, AVAIL,  0.02, AVAIL,  0.01),   (0.7,  0.9,   0.2)
	t_data[23] = (0.8,     0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.6)

	return t_data