# Gradient Descent application for Optimization Problem
# using Rosenbrock Function

# we ask help for mathematics calculation
import numpy as np

# First case: we set a=0 and b=100
def DerrivRosenbrock0 ( point ):
    dx = 2*point[0] - 400*point[0]*(point[1] - (point[0]**2))
    dy = 200*(point[1] - (point[0]**2))
    return dx, dy

# Second case: we set a=1 and b=100
def DerrivRosenbrock1 ( point ):
    dx = (-2*(1 - point[0]) - 400*(point[1] - (point[0]**2)**2))
    dy = 200*(point[1] - (point[0]**2))
    return dx, dy

def main():
    # set the learning rate first
    # this learning set is ad hoc corresponds to objective function
    lrate = 0.002
    # initialize a point
    a = np.array([-.5, .2])
    # set number of epochs (can be changed as you want)
    epoch = 100000
    # we have to record all tuples of the points and its function
    ai = []
    for i in range(epoch):
        # objective function for first case (uncomment code below)
        # f = (a[0]**2) + (100*((a[1] - a[0]**2)**2))
        # objective function for second case
        f = ((1 - a[0])**2) + (100*((a[1] - a[0]**2)**2))
        # append the point and its obj function to ai as 1D list
        ai.append([a,f])
        # compute its derrivative on point a
        # Derrivative for first case (uncomment code below)
        # fi = np.array(DerrivRosenbrock0(a))
        # Derrivative for second case
        fi = np.array(DerrivRosenbrock1(a))
        # set the new point based on its 
        a = a - np.dot(lrate,fi)
    
    # convert ai into a numpy array
    ai = np.array(ai)
    # print(ai.shape) 'uncomment this to check ai shape and delete this sentences'
    # print the last 10 of ai
    print(ai[-10:-1])
    # the minimum value of the function is just the last element of ai
    print(f'the minimum is: {ai[-1, 1]} at point: {ai[-1,0]}')


if __name__ == '__main__':
    main()    