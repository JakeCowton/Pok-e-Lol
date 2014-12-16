from slope_calculator import down_slope, up_slope

def membership_for_high(x):
	"""
	Calculate an OCEAN value's high membersip
	:type x: float
	:param x: The value
	:rtype: float
	:returns: Membership value
	"""
	left = 0
	right = 0

	if x <= left:
        return 0
    elif x >= right:
        return 1
    else:
        return float(up_slope(x, left, right))

def membership_for_low(x):
	"""
	Calculate an OCEAN value's low membersip
	:type x: float
	:param x: The value
	:rtype: float
	:returns: Membership value
	"""
	left = 0
    right = 0

    if x <= left:
        return 1
    elif x >= right:
        return 0
    else:
        return float(down_slope(x, left, right))
