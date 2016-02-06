import numpy as np
import matplotlib.pyplot as graph
from scipy.optimize import minimize


def cost_function(weights, rates, values):
    return weights * values * rates * np.e ** rates
