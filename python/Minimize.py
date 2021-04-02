import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import optimize

sys.path.append(".")

# minimizing a function
# no more command line arguments! just try a couple of methods

# function to be minimized: 5(x+3)^2 + (1/2)xy + 3(y-5)^2
def minfunc(vecs):
	x = vecs[0]
	y = vecs[1]
	return 5.*np.power(x+3., 2) + (0.5)*x*y + 3.*np.power(y-5., 2)


# x, y coordinate mesh
mesh = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))

# get mesh of z values
z = minfunc(mesh)

# minimize the function, save the results. try several methods
x0 = np.array([0,0]) # just try the origin as our starting point

print("Powell's Method:")
res1 = optimize.minimize(minfunc, x0, method="Powell", bounds=[(-10, 10), (-10, 10)], options={"disp": True, "return_all": True})
print("Minimum: (", res1["x"][0], ", ", res1["x"][1], ")\n")

print("\nConjugate Gradient Method:")
res2 = optimize.minimize(minfunc, x0, method="CG", options={"disp": True, "return_all": True})
print("Minimum: (", res2["x"][0], ", ", res2["x"][1], ")\n")

print("\nQuasi-Newton Method:")
res3 = optimize.minimize(minfunc, x0, method="BFGS", options={"disp": True, "return_all": True})
print("Minimum: (", res3["x"][0], ", ", res3["x"][1], ")\n")

#print("Powell's Method Err: ", )


# show the results
fig = plt.figure(figsize=(8, 8))
ax = plt.gca()
ax.set_aspect("equal")

# contour plot of function
cs = plt.contour(mesh[0], mesh[1], z, levels=20)

# plot location of each minimum
plt.axvline(res1["x"][0], c="C0", ls="--", label="Powell: ({}, {})".format(res1["x"][0], res1["x"][1]))
plt.axhline(res1["x"][1], c="C0", ls="--")

plt.axvline(res2["x"][0], c="C1", ls="--", label="CG: ({}, {})".format(res2["x"][0], res3["x"][1]))
plt.axhline(res2["x"][1], c="C1", ls="--")

plt.axvline(res3["x"][0], c="C2", ls="--", label="BFGS: ({}, {})".format(res2["x"][0], res3["x"][1]))
plt.axhline(res3["x"][1], c="C2", ls="--")
plt.legend()

# label the contours
ax.clabel(cs, inline=True)

# axes and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Convex 2-D Function")
plt.show()
fig.savefig("min_function.jpg", dpi=180)


#The estimates are close enough that you really can't zoom in enough to see the differences
# ignore this code
"""
fig1 = plt.figure(figsize=(8, 8))
ax1 = plt.gca()
#ax1.set_aspect("equal")
zoom_mesh = np.meshgrid(np.linspace(-3.263625, -3.263575, 100), np.linspace(5.271965, 5.271975, 100))
cs = plt.contour(zoom_mesh[0], zoom_mesh[1], minfunc(zoom_mesh), levels=20)
plt.axvline(res1["x"][0], c="C0", ls="--", label="Powell: ({}, {})".format(res1["x"][0], res1["x"][1]))
plt.axhline(res1["x"][1], c="C0", ls="--")

plt.axvline(res1["x"][0], c="C1", ls="--", label="CG: ({}, {})".format(res2["x"][0], res3["x"][1]))
plt.axhline(res1["x"][1], c="C1", ls="--")

plt.axvline(res1["x"][0], c="C2", ls="--", label="BFGS: ({}, {})".format(res2["x"][0], res3["x"][1]))
plt.axhline(res1["x"][1], c="C2", ls="--")
plt.legend()

ax1.clabel(cs, inline=True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Convex 2-D Function")#.format(method))
plt.show()
fig1.savefig("min_function_zoom.jpg", dpi=180)
"""