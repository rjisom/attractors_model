import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dt = 0.01
num_steps = 10000

def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three-dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    
    return np.array([x_dot, y_dot, z_dot])

def dadras(xyz, *, a=3, b=2.7, c=1.7, d=2, e=9):
    x, y, z = xyz
    x_dot = y-a*x+b*y*z
    y_dot = c*y-x*z+z
    z_dot = d*x*y-e*z
    
    return np.array([x_dot, y_dot, z_dot])

def halvorsen(xyz, *, a=1.89):
    x, y, z = xyz
    x_dot = ((a)*-1)*x+(y*-4)+(z*-4)-(y**2)
    y_dot = ((a)*-1)*y+(z*-4)+(x*-4)-(z**2)
    z_dot = ((a)*-1))*z+(x*-4)+(y*-4)+(x**2)
    
    return np.array([x_dot, y_dot, z_dot])

def createPlot(title, attractorType):
    xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
    xyzs[0] = (0., 1., 1.05)  # Set initial values
    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        xyzs[i + 1] = xyzs[i] + attractorType(xyzs[i]) * dt

    # Plot
    ax = plt.figure().add_subplot(projection='3d')

    ax.plot(*xyzs.T, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title(title)
     
    return (ax.figure)

plot1 = createPlot('Lorenz Attractor',lorenz)
plot2 = createPlot('Dadras Attractor',dadras)
plot3 = createPlot('Halverson Attractor',havlerson)

st.pyplot(plot1.figure)
st.pyplot(plot2.figure)
st.pyplot(plot3.figure)
