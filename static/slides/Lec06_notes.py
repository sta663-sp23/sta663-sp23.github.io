## Exercise 1

x = np.arange(16).reshape((4,4)); x

x[1:3, 1:3]

x[[1,2], [1,2]] # incorrect


## Exercise 2

pts = np.linspace(-1,3, 5000)
x, y = np.meshgrid(pts, pts)

f = (1-x)**2 + 100*(y-x**2)**2


np.min(f)
x[f == np.min(f)]
y[f == np.min(f)]

min_i = np.argmin(f, axis=None)
x.reshape(-1)[min_i]
y.reshape(-1)[min_i]


## Exercise 3

#   A (128 x 128 x 3) + B (3):
#
#   A    128 x 128 x 3
#   B                3
#   ------------------
#   A+B  128 x 128 x 3 


#   A (8 x 1 x 6 x 1) + B (7 x 1 x 5)
#
#   A    8 x 1 x 6 x 1
#   B        7 x 1 x 5
#   ------------------
#   A+B  8 x 7 x 6 x 5


#   A (2 x 1) + B (8 x 4 x 3)
#
#   A            2 x 1
#   B        8 x 4 x 3
#   ------------------
#   A+B         Error


#   A (3 x 1) + B (15 x 3 x 5)
#
#   A            3 x 1
#   B       15 x 3 x 5
#   ------------------
#   A+B     15   3   5


#   A (3) + B (4)
#
#   A       3
#   B       4
#   --------------
#   A+B   Error


## Demo 1

rng = np.random.default_rng(1234)

d = rng.normal(loc=[-1,0,1], scale=[1,2,3], size=(1000,3))
d.mean(axis=0)
d.std(axis=0)

ds = (d - d.mean(axis=0)) / d.std(axis=0)
ds.mean(0)
ds.std(0)
