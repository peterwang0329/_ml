import torch as th

def gradientDescent(learning_rate=0.1,max_loops=1000):
    x,y,z = 0
    f = x*x + y*y + z*z - 2*x - 4*y - 6*z + 8
    f.backward()

    