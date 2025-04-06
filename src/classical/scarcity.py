import numpy as np
from typing import List

# TODO: Increase dimension
def prodduction_possibilities_curve(production: List[List[int]], mode='linear'):
    n = len(production)

    if n == 0:
        raise ValueError("No production at all, empty list can not be productions")
    else:
        __validate_production(production)
    
    if n == 1:
        return production
    
    if n > 2:
        raise NotImplementedError("Solution for dimension above 2 is not implemented")
    
    return -production[0]/production[1]

def __validate_production(production: List[int]):
    n = len(production)

    for i in range(n):
        if production[i] <= 0:
            raise ValueError(f"Production can not be less than or equal to zero. Production of index {i} is {production[i]}")