# Slope calculations
def down_slope(x, left, right):
    return float(float(right - x) / float(right - left))


def up_slope(x, left, right):
    return float(float(x - left) / float(right - left))
