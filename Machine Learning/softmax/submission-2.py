import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z=z-max(z)
        exp_ans=np.exp(z)
        ans= []
        summ=0
        for i in range(len(exp_ans)):
            summ+=exp_ans[i]
        for i in range(len(exp_ans)):
            ans.append(exp_ans[i]/summ)

        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        return np.round(ans,4)
