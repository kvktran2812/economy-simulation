import numpy as np
from typing import List

# TODO: Increase dimension
def production_slope(production: List[int], mode='linear'):
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


# TODO: Complete calculation
def production_probabilities_curve(production_combination):
    n = len(production_combination)
    
    # validate
    if n == 0:
        raise ValueError("List is empty, there is no production here")
    
    if n == 1:
        raise ValueError("There is only one worker who produce")
    
    dim = len(production_combination[0])
    if dim <= 1:
        raise ValueError("In this economy system, number of distinct production items is less than 2, not valid for production probabilities curve calculation")
    

    
    return

def __validate_production(production: List[int]):
    n = len(production)

    for i in range(n):
        if production[i] <= 0:
            raise ValueError(f"Production can not be less than or equal to zero. Production of index {i} is {production[i]}")