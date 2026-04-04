import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.round((1/(1+(2.71828**-z))),5)
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        
        ans= np.maximum(0,z)
        return ans
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        pass
