from abc import abstractmethod
from typing import Union, List
import numpy as np


class BaseEstimator:

    def __init__(self):
        self.parameters = {}

    @abstractmethod
    def update(self, new_value: Union[float, int, List[int], List[float]]) -> None:
        pass

    def consume(self, data: Union[List[float], List[int]]) -> None:
        data = iter(data)
        for new_value in data:
            self.update(new_value)

    def fit(self, data: Union[List[float], List[int], float, int]) -> None:
        if hasattr(data, "__iter__"):
            self.consume(data)
        else:
            self.update(data)


class NegBinom(BaseEstimator):

    def __init__(self, n: np.nan, p: np.nan, ddof):
        super().__init__()
        self.ddof = ddof
        self.active_proportion = 1.0
        self.internal_params = {}

        if not np.isnan(n) or np.isnan(p):
            if np.isnan(n) or np.isnan(p):
                raise ValueError("Specify either both n and p or neither")
            num_fitted = 50  # some number
            try:
                temp = 1.0 / p
                temp_2 = temp - 1.0
                mean = n * temp_2
                var = n * temp_2 * temp
                m2 = var * (num_fitted - self.ddof)
            except ZeroDivisionError:
                raise ZeroDivisionError(f"initialise with p > 0, not {p}")
            self.initialise_aggregate(n=n, p=p, num_fitted=num_fitted, mean=mean, sq_diff=m2)

    def initialise_aggregate(self, n=np.nan, p=np.nan, num_fitted=0, mean=0.0, sq_diff=0.0):
        self.parameters = {"mean": mean, "sq_diff": sq_diff, "num_fitted": num_fitted}
        self.internal_params["n"] = n
        self.internal_params["p"] = p

    def update(self, new_value: Union[float, int]):
        """

        :param new_value:
        :return:
        """
        if new_value < 0:
            raise ValueError(f"new value should be >=0, not {new_value}")

        self.parameters["mean"], self.parameters["sq_diff"], self.parameters["num_fitted"] = welford.update_welford(
            self.parameters["mean"], self.parameters["sq_diff"], self.parameters["num_fitted"], new_value
        )
        self.update_internal_params()