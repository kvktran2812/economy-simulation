import numpy as np
from typing import List
import matplotlib.pyplot as plt

#############################################
# TODO:
# List of next thing that might be interesting to add to this module
# - Production Possibilities Curve for more than 3 products ? (Might be interested but not use much in real-life scenario)


#############################################

def sort_according_to_cost(production_combination):
    t_production = np.array(production_combination).T
    oc = t_production[:, 0] / t_production[:, 1]  # Compute opportunity cost
    sorted_indices = np.argsort(oc)     # Get sorted indices
    sorted_production = t_production[sorted_indices].T

    return sorted_production


def ppc_2goods(good1: List[float], good2: List[float]) -> np.ndarray:
    n1 = len(good1)
    n2 = len(good2)

    if n1 != n2:
        raise ValueError("Size of 2 list of goods is not the same")
        
    production = np.array([good1, good2])
    sorted_production = sort_according_to_cost(production)
    
    first_product_sum = sum(sorted_production[0])
    second_product_sum = 0
    ret = np.zeros((2, n1+1))
    ret[0,0] = first_product_sum

    for i in range(n1):
        first_product_sum -= sorted_production[0][i]
        second_product_sum += sorted_production[1][i]
        ret[0,i+1] = first_product_sum
        ret[1,i+1] = second_product_sum

    return ret


def ppc_plot(good1: List[float], good2: List[float], good_name_1: str = "Good Name 1", good_name_2: str = "Good Name 2") -> None:
    ppc_result = ppc_2goods(good1, good2)

    # Plot PPC curve
    plt.plot(ppc_result[0], ppc_result[1], color='red')
    plt.fill_between(ppc_result[0], ppc_result[1], 0, color='lightblue', alpha=0.7)

    # Show extreme points
    plt.scatter(ppc_result[0], ppc_result[1], color='red', label='Extreme Points')


    # Labels and title
    plt.xlabel(good_name_2)
    plt.ylabel(good_name_1)
    plt.title('Production Possibilities Curve (PPC)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return