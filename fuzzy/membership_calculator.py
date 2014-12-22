from .slope_calculator import down_slope, up_slope

def membership_for_low(x):
    """
    Calculate an OCEAN value's low membersip
    :type x: float
    :param x: The value
    :rtype: float
    :returns: Membership value
    """
    left = 0.125
    right = 0.375

    if x <= left:
        return 1
    elif x >= right:
        return 0
    else:
        return float(down_slope(x, left, right))

def membership_for_mid(x):
    """
    Calculate an OCEAN value's medium membersip
    :type x: float
    :param x: The value
    :rtype: float
    :returns: Membership value
    """
    left_1 = 0.125
    right_1 = 0.375
    left_2 = 0.625
    right_2 = 0.875

    if x <= left_1:
        return 0
    elif x > left_1 and x < right_1:
        return float(up_slope(x, left_1, right_1))
    elif x >= right_1 and x <= left_2:
        return 1
    elif x > left_2 and x < right_2:
        return float(down_slope(x, left_2, right_2))
    else:
        return 0

def membership_for_high(x):
    """
    Calculate an OCEAN value's high membersip
    :type x: float
    :param x: The value
    :rtype: float
    :returns: Membership value
    """
    left = 0.625
    right = 0.875

    if x <= left:
        return 0
    elif x >= right:
        return 1
    else:
        return float(up_slope(x, left, right))

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
    # If high membership is largest
    if membership_for_high(x) >= membership_for_low(x) and \
                                 membership_for_mid(x):

        # If x is directly proporional to logic
        # Return the raw result
        if direct:
            return "HIGH"

        # Return the inverse
        else:
            return "LOW"

    # If mid membership is largest
    elif membership_for_mid(x) >= membership_for_low(x) and \
                                  membership_for_high(x):
        return "MID"

    # If low membership is largest
    elif membership_for_low(x) >= membership_for_high(x) and \
                                  membership_for_mid(x):
        # If x is directly proporional to logic
        # Return the raw result
        if direct:
            return "LOW"

        # Return the inverse
        else:
            return "HIGH"