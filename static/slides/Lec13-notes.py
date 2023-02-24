## Exercise 1

from scipy import optimize
import timeit

def f(x): 
  return np.exp(x[0]-1) + np.exp(-x[1]+1) + (x[0]-x[1])**2

def grad(x):
  return [
    np.exp(x[0]-1) + 2 * (x[0]-x[1]),
    -np.exp(-x[1]+1) - 2 * (x[0]-x[1])
  ]

def hess(x):
  return [
    [ np.exp(x[0]-1) + 2, -2                  ],
    [ -2                , np.exp(-x[1]+1) + 2 ]
  ]

x0 = [0, 0]

optimize.minimize(fun=f, x0=x0, jac=grad, method="BFGS")
optimize.minimize(fun=f, x0=x0, jac=grad, method="CG")
optimize.minimize(fun=f, x0=x0, jac=grad, method="Newton-CG")
optimize.minimize(fun=f, x0=x0, method="Nelder-Mead")

timeit.Timer(lambda: optimize.minimize(fun=f, x0=x0, jac=grad, method="BFGS")).repeat(1, 100)
timeit.Timer(lambda: optimize.minimize(fun=f, x0=x0, jac=grad, method="CG")).repeat(1, 100)
timeit.Timer(lambda: optimize.minimize(fun=f, x0=x0, jac=grad, method="Newton-CG")).repeat(1, 100)
timeit.Timer(lambda: optimize.minimize(fun=f, x0=x0, method="Nelder-Mead")).repeat(1, 100)


## Exercise 2

from numpy import np
from scipy.stats import gamma
from scipy import optimize

g = gamma(a=2.0, scale=2.0)
x = g.rvs(size=100, random_state=1234)

def mle_gamma(θ): 
  if θ[0] <= 0 or θ[1] <= 0:
    return 1e16
  else:
    return -np.sum(np.log(gamma.pdf(x, a=θ[0], scale=θ[1])))

optimize.minimize(
  mle_gamma, x0=[1,1], method="bfgs"
)

gamma.fit(x, floc=0)
