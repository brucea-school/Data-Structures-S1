import numpy as np


def max_int_in_array(array):
    if len(array) == 1:
        return array[0]
    else:
        large = -10000000
        for i in array:
             if i>large:
                 large = i
        return large





print(max_int_in_array(np.array([5, 2, -5, 10, 23, -21])))