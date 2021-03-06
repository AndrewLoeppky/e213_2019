#!/usr/bin/env python
"""Calculate the values of surface height (h) and east-west velocity
(u) in a dish of water where a point disturbance of h initiates waves.
Use the simplified shallow water equations on a non-staggered grid.

This is an implementation of lab7 section 4.3.

Example usage from the shell::

  # Run 5 time steps on a 9 point grid
  $ rain.py 5 9

The graph window will close as soon as the animation finishes.  And
the default run for 5 time steps doesn't produce much of interest; try
at least 100 steps.

To have the graph window persist after the script ends run it from
within the ipython shell, or the Python interpreter.

Example usage from ipython::

  $ ipython -pylab
  ...
  In [1]: run rain 200 9

Example usage from the Python interpreter::

  $ python
  ...
  >>> import rain
  >>> # Run 200 time steps on a 9 point grid
  >>> rain.main((200, 9))
"""
from __future__ import division

import copy
import sys
from builtins import object
from builtins import range

import matplotlib.pyplot as plt
import numpy as np


class Quantity(object):
    """Generic quantity to define the data structures and method that
    are used for both u and h.

    u and h objects will be instances of this class.
    """

    def __init__(self, n_grid, n_time):
        """Initialize an object with prev, now, and next arrays of
        n_grid points, and a store array of n_time time steps.
        """
        self.n_grid = n_grid
        # Storage for values at previous, current, and next time step
        self.prev = np.zeros(n_grid)
        self.now = np.zeros(n_grid)
        self.next_val = np.zeros(n_grid)
        # Storage for results at each time step.  In a bigger model
        # the time step results would be written to disk and read back
        # later for post-processing (such as plotting).
        self.store = np.zeros((n_grid, n_time))

    def store_timestep(self, time_step, attr="next_val"):
        """Copy the values for the specified time step to the storage
        array.

        The `attr` argument is the name of the attribute array (prev,
        now, or next_val) that we are going to store.  Assigning the value
        'next_val' to it in the function def statement makes that the
        default, chosen because that is the most common use (in the
        time step loop).
        """
        # The __getattribute__ method let us access the attribute
        # using its name in string form;
        # i.e. x.__getattribute__('foo') is the same as x.foo, but the
        # former lets us change the name of the attribute to operate
        # on at runtime.
        self.store[:, time_step] = self.__getattribute__(attr)

    def shift(self):
        """Copy the .now values to .prev, and the .next_val values to .new.

        This reduces the storage requirements of the model to 3 n_grid
        long arrays for each quantity, which becomes important as the
        domain size and model complexity increase.  It is possible to
        reduce the storage required to 2 arrays per quantity.
        """
        # Note the use of the copy() method from the copy module in
        # the standard library here to get a copy of the array, not a
        # copy of the reference to it.  This is an important and
        # subtle aspect of the Python data model.
        self.prev = copy.copy(self.now)
        self.now = copy.copy(self.next_val)


def initial_conditions(u, h, ho):
    """Set the initial condition values.
    """
    u.prev[:] = 0
    h.prev[:] = 0
    h.prev[len(h.prev) // 2] = ho


def boundary_conditions(u_array, h_array, n_grid):
    """Set the boundary condition values.
    """
    u_array[0] = 0
    u_array[n_grid - 1] = 0
    # h_array[0] = h_array[1]
    # h_array[n_grid-1] = h_array[n_grid-2]


def first_time_step(u, h, g, H, dt, dx, ho, gu, gh, n_grid):
    """Calculate the first time step values from the analytical
    predictor-corrector derived from equations 4.18 and 4.19.
    """
    u.now[1 : n_grid - 1] = 0
    factor = gu * ho  # remove factor of 2
    midpoint = n_grid // 2
    u.now[midpoint - 1] = -factor
    u.now[midpoint] = factor  # change index
    h.now[1 : n_grid - 1] = 0
    h.now[midpoint] = ho - g * H * ho * dt ** 2 / (dx ** 2)  # remove factor of 4


def leap_frog(u, h, gu, gh, n_grid):
    """Calculate the next time step values using the leap-frog scheme
    derived from equations 4.16 and 4.17.
    """
    # Modified for a staggered grid
    for pt in range(1, n_grid - 1):
        u.next_val[pt] = u.prev[pt] - 2 * gu * (h.now[pt + 1] - h.now[pt])
        h.next_val[pt] = h.prev[pt] - 2 * gh * (u.now[pt] - u.now[pt - 1])


def animate(u, h, ho, dt, n_time):
    """Create animated graphs of the model results using matplotlib.

    You probably need to run the rain script from within ipython,
    launched with `ipython -pylab` in order to see the graphs.  And
    the default run for 5 time steps doesn't produce much of interest;
    try at least 100 steps.
    """
    # Turn interactive mode on so that the graph displays can be
    # update at each time step
    plt.ion()
    # Create a figure with 2 sub-plots
    fig = plt.figure()
    fig.subplots_adjust(left=0.17)
    ax_u = plt.subplot(211)
    ax_h = plt.subplot(212)
    # Set the figure title, and the axes labels.  Capture the
    # generated title text object so that we can update it in the time
    # step loop.
    title = fig.text(0.45, 0.95, "Results at t = 0.000s")
    ax_u.set_ylabel("u [cm/s]")
    ax_h.set_ylabel("h [cm]")
    ax_h.set_xlabel("Grid Point")
    # Graph the initial conditions, and set the y-axis limits for the
    # plots.  Capture the generated line objects so that we can update
    # them in the time step loop.
    u_line, = ax_u.plot(u.store[:, 0])
    u_limit = round(np.amax(u.store) + 0.05, 1)
    ax_u.set_ylim((-u_limit, u_limit))
    h_line, = ax_h.plot(h.store[:, 0])
    ax_h.set_ylim((-ho, ho))
    # Display the initial conditions
    plt.draw()
    for t in range(1, n_time):
        # Update the figure title, and lines data at each time step,
        # and re-draw them
        title.set_text("Results at t = %.3fs" % (dt * t))
        u_line.set_ydata(u.store[:, t])
        h_line.set_ydata(h.store[:, t])
        plt.draw()


def main(args):
    """Run the model.

    args is a 2-tuple; (number-of-time-steps, number-of-grid-points)
    """
    n_time = int(args[0])
    n_grid = int(args[1])
    #     Alternate implementation:
    #     n_time, n_grid = map(int, args)

    # Constants and parameters of the model
    g = 980  # acceleration due to gravity [cm/s^2]
    H = 1  # water depth [cm]
    dt = 0.001  # time step [s]
    dx = 1  # grid spacing [cm]
    ho = 0.01  # initial perturbation of surface [cm]
    gu = g * dt / dx  # first handy constant
    gh = H * dt / dx  # second handy constant
    # Create velocity and surface height objects
    u = Quantity(n_grid, n_time)
    h = Quantity(n_grid, n_time)
    # Set up initial conditions and store them in the time step
    # results arrays
    initial_conditions(u, h, ho)
    u.store_timestep(0, "prev")
    h.store_timestep(0, "prev")
    # Calculate the first time step values from the
    # predictor-corrector, apply the boundary conditions, and store
    # the values in the time step results arrays
    first_time_step(u, h, g, H, dt, dx, ho, gu, gh, n_grid)
    boundary_conditions(u.now, h.now, n_grid)
    u.store_timestep(1, "now")
    h.store_timestep(1, "now")
    # Time step loop using leap-frog scheme
    for t in range(2, n_time):
        # Advance the solution and apply the boundary conditions
        leap_frog(u, h, gu, gh, n_grid)
        boundary_conditions(u.next_val, h.next_val, n_grid)
        # Store the values in the time step results arrays, and shift
        # .now to .prev, and .next_val to .now in preparation for the next
        # time step
        u.store_timestep(t)
        h.store_timestep(t)
        u.shift()
        h.shift()
    # Print the results
    np.set_printoptions(suppress=True)
    print("u:\n", u.store)
    print("h:\n", h.store)
    # Plot the results as animated graphs
    animate(u, h, ho, dt, n_time)


if __name__ == "__main__":
    # sys.argv is the command-line arguments as a list. It includes
    # the script name as its 0th element. Check for the degenerate
    # cases of no aditional arguments, or the 0th element containing
    # `sphinx-build`. The latter is a necessary hack to accommodate
    # the sphinx plot_directive extension that allows this module to
    # be run to include its graph in sphinx-generated docs.
    if len(sys.argv) == 1 or "sphinx-build" in sys.argv[0]:
        # Default to 5 time steps, and 9 grid points
        main((5, 9))
    elif len(sys.argv) == 3:
        # Run with the number of time steps and grid point the user gave
        main(sys.argv[1:])
    else:
        print("Usage: rain n_time n_grid")
        print("n_time = number of time steps; default = 5")
        print("n_grid = number of grid points; default = 9")
