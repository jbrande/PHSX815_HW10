# PHSX815_HW10

This program minimizes the 2-Dimensional function 5(x+3)^2 + (1/2)xy + 3(y-5)^2 using scipy's optimize.minimize functions. We minimize the function using three separate methods: Powell's method, with bounds given, the Polak-Ribiere implementation of the Conjugate Gradient method, and the BFGS implementation of the Quasi-Newton method.

The program can be called as python python/Minimize.py with no arguments. The program will automatically minimize the function with each method, and print some information about the results.
The program will print the resulting minimum, and plot the function over the intervals x=[-10, 10] and y=[-10, 10] and show the minima for each method with the intersection of a vertical and horizontal line. This plot is saved as "min_function.jpg" in the directory.