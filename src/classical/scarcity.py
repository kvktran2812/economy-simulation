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
def production_probabilities_curve(production_combination: List[List[int]]):
    n = len(production_combination)
    
    # validate
    if n == 0:
        raise ValueError("List is empty, there is no production here")
    
    if n == 1:
        raise ValueError("There is only one product here")
    
    if n > 2:
        raise NotImplementedError("Not support for more than 2 products")
    
    # Check if array has same dimension
    dim = len(production_combination[0])
    for p in production_combination:
        if len(p) != dim:
            raise ValueError("List of production don't have the same size")
    
    first_product_sum = sum(production_combination[0])
    second_product_sum = 0
    ret = np.zeros((n, dim+1))
    ret[0,0] = first_product_sum

    for i in range(dim):
        first_product_sum -= production_combination[0][i]
        second_product_sum += production_combination[1][i]
        print(first_product_sum, second_product_sum)
        ret[0,i+1] = first_product_sum
        ret[1,i+1] = second_product_sum

    return ret

def __validate_production(production: List[int]):
    n = len(production)

    for i in range(n):
        if production[i] < 0:
            raise ValueError(f"Production can not be less than zero. Production of index {i} is {production[i]}")