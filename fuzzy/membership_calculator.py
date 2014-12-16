from slope_calculator import down_slope, up_slope

def membership_for_high(x):
    """
    Calculate an OCEAN value's high membersip
    :type x: float
    :param x: The value
    :rtype: float
    :returns: Membership value
    """
    left = 0.4
    right = 0.6

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
    left = 0.4
    right = 0.6

    if x <= left:
        return 1
    elif x >= right:
        return 0
    else:
        return float(down_slope(x, left, right))

def find_membership(x, direct=True):
    """
    Finds the membership of the x value
    :type x: float
    :param x: The value
    :type direct: bool
    :param direct: If the input is directly proportional to logic
    :rtype: string
    :returns: Whether x results in high logic or low
    """
    # If high membership >= low membership
    if membership_for_high(x) >= membership_for_low(x):
        # If x is directly proporional to logic
        # Return the raw result
        if direct:
            return "HIGH"

        # Return the inverse
        else:
            return "LOW"
    else:
        # If x is directly proporional to logic
        # Return the raw result
        if direct:
            return "LOW"

        # Return the inverse
        else:
            return "HIGH"
