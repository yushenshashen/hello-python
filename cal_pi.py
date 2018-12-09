#goal: calculate the pi use area of circle

from random import random
from time import perf_counter

start_time = perf_counter()
end_time = perf_counter()

dots = 1000*10000
hits = 0
for i in range(dots):
    x, y = random(), random()
    dists = pow(x**2+y**2, 0.5)
    if dists <= 1:
        hits += 1

pi = 4 * hits/dots
print('pi is : {:.5f}'.format(pi))
end_time = perf_counter()
print('cost time: {:5f}s'.format(end_time-start_time))
