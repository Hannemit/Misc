from scipy.stats import nbinom
import numpy as np
import matplotlib.pyplot as plt


def max_llh_given_r_param(neg_binom_r_param, count_data):
    """
    For a given n parameter (r, n, etc.. the int parameter), give the log likelihood of observing data (counts)
    using the maximum likelihood estimator of the other negative binomial parameter (p).
    :param neg_binom_r_param: int (could be float too), parameter of neg binom distribution
    :param count_data: np array, count values we model with negative binomial
    :return: float, log likelihood
    """
    num_counts = len(count_data)
    p = 1 - sum(count_data) / (num_counts * neg_binom_r_param + sum(count_data))

    llh = sum(nbinom.logpmf(count_data, neg_binom_r_param, p))
    return llh


# set parameters
n, p = 10, 0.4

# generate x values and get pmf
x = np.arange(nbinom.ppf(0.01, n, p), nbinom.ppf(0.99, n, p))
pmf = nbinom.pmf(x, n, p)

# plot
plt.plot(pmf)
plt.axvline(x=n)
plt.show()

# check whether peak occurs at correct value for n (r).
r_vals = np.arange(5, 20)
llh = np.zeros(len(r_vals))
counts = np.random.negative_binomial(n, p, size=100000)
for ii, r in enumerate(r_vals):
    llh[ii] = max_llh_given_r_param(r, counts)

# plot
fig = plt.figure()
plt.plot(r_vals, llh)
plt.axvline(x=n)
plt.show()
