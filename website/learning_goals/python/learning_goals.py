# -*- coding: utf-8 -*-
# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Final-quiz-learning-goals----Thursday-April-17,-Buch-A104,-3:30pm-to-5pm" data-toc-modified-id="Final-quiz-learning-goals----Thursday-April-17,-Buch-A104,-3:30pm-to-5pm-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Final quiz learning goals -- Thursday April 17, Buch A104, 3:30pm to 5pm</a></span><ul class="toc-item"><li><span><a href="#Math/numerics" data-toc-modified-id="Math/numerics-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Math/numerics</a></span></li><li><span><a href="#Python/coding" data-toc-modified-id="Python/coding-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Python/coding</a></span></li></ul></li><li><span><a href="#Quiz-1-learning-goals" data-toc-modified-id="Quiz-1-learning-goals-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Quiz 1 learning goals</a></span><ul class="toc-item"><li><span><a href="#ODEs" data-toc-modified-id="ODEs-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>ODEs</a></span></li><li><span><a href="#Simulation-/-python" data-toc-modified-id="Simulation-/-python-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Simulation / python</a></span></li></ul></li><li><span><a href="#Quiz-2-learning-goals" data-toc-modified-id="Quiz-2-learning-goals-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Quiz 2 learning goals</a></span><ul class="toc-item"><li><span><a href="#Finite-Volume-method" data-toc-modified-id="Finite-Volume-method-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Finite Volume method</a></span></li><li><span><a href="#Simulation-/-python" data-toc-modified-id="Simulation-/-python-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Simulation / python</a></span></li></ul></li><li><span><a href="#Quiz-3-learning-goals" data-toc-modified-id="Quiz-3-learning-goals-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Quiz 3 learning goals</a></span><ul class="toc-item"><li><span><a href="#Differential-equations" data-toc-modified-id="Differential-equations-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Differential equations</a></span><ul class="toc-item"><li><span><a href="#Math-Details" data-toc-modified-id="Math-Details-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Math Details</a></span></li></ul></li><li><span><a href="#Simulation-/-python" data-toc-modified-id="Simulation-/-python-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Simulation / python</a></span></li></ul></li><li><span><a href="#Quiz-4-learning-goals" data-toc-modified-id="Quiz-4-learning-goals-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Quiz 4 learning goals</a></span><ul class="toc-item"><li><span><a href="#Computational-methods" data-toc-modified-id="Computational-methods-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Computational methods</a></span></li><li><span><a href="#Mathematics" data-toc-modified-id="Mathematics-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Mathematics</a></span></li><li><span><a href="#Be-able-to-set-up-boundary-value-problem:" data-toc-modified-id="Be-able-to-set-up-boundary-value-problem:-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Be able to set up boundary value problem:</a></span></li><li><span><a href="#Simulation-/-python" data-toc-modified-id="Simulation-/-python-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Simulation / python</a></span></li></ul></li></ul></div>
# %% [markdown]
# # Summary of course learning goals
# %% [markdown]
# ## Final quiz learning goals -- Thursday April 17, Buch A104, 3:30pm to 5pm
#
# **Exam is written to take 60 minutes, you'll have 90 minutes so hopefully not rushed**
#
# **Note that the final quiz is comprehensive, and all learning goals from prior quizzes are fair game.
#   Having said that,
#   here are the set that we think are particularly high priority, study these first**
#
# ### Math/numerics
#
# * Can write a mathematical model (i.e. the appropriate equations) that describes how a conserved quantity such as mass, volume (if the material in incompressible), energy, in a single, discrete control volume, (for example the TMF problem) changes through time.
#
# * Can represent fluxes, sources and sinks in the conservation equation with the correct dimensions (eg, stuff per mass per time, stuff per volume per time, stuff per time, etc).
#
# * Can represent a model for a discrete control volume (eg TMF) as either a difference equation or a differential equation.
#
# * Can approximate fluxes between finite volumes using finite-difference methods;
#
# * Can recognize how to create a linear system of equations from a finite-volume discretization of a conservation problem;
#
# * Can incorporate Dirichlet (first-type or specified dependent variable) and second type or flux boundary conditions into a finite-volume system of equations; can write the linear system of equations for a forward or backward Euler approximation of a transient finite-volume problem
#
# ### Python/coding
#
#
# * Can define a simple class that contains class variables,
#   instance variables and instance methods and use it to pass parameters
#   into and out of a function.
#
# * Can write basic functions with default values
#
# * Can use the pandas apply method to execute a function on every
#   row of a dataframe
#
# * Can add a column to a data frame and use groupby with
#   that column to group dataframe rows into subset dataframes
#
# * Can do simple statistics (mean, median, max, min,
#   summary) on pandas dataframes and pandas series objects
#
# * Can construct dataframes from lists of tuples, lists of
#   dictionaries, or numpy arrays using from_records member
#   function
#
#
#
# %% [markdown]
# ## Quiz 1 learning goals
#
# On Tuesday, Feb. 5, we will have our first quiz of the
# course. The quiz will last 30 minutes and will be a traditional
# pen-and-paper format.
#
# The learning goals for this quiz are:
#
# ### ODEs
#
#  - Recognize an ordinary differential equation (ODE).
#  - Recognize that the solutions to ODEs are FUNCTIONS, not single
#    numbers.
#  - Be able to determine the ORDER of an ODE.
#  - Be able convert between the notations dy/dx, and y’.
#  - Be able to recognize whether an ODE is linear or nonlinear.
#  - Be able to write a simple differential equation model of a system,
#    given the description of the system.
#  - Identify information required to determine a particular solution
#    (boundary and initial conditions) of an ODE.
#  - Be able to confirm that a solution “solves” a given ODE.
#
# ### Simulation / python
#
#  - Be able to read a code fragment in python (to the level covered in
#    the notebooks given in class up to January 24, 2019), and recognize
#    syntax errors.
#  - Be able to write the code to determine the type of a variable.
#  - Be able to define a numpy array of a specified size in one or two
#    dimensions
#  - Be able write a simple loop over a specified range.
#  - Be able to state the basic conservation principle (of mass)
#  - Be able to take a conservation principle description in words (eg
#    TMF) and convert it to a mathematical equation (algebraic or
#    differential).
#  - Be able to compute (by hand) the forward Euler approximation for one
#    or two time steps, given a description of the conservation problem
#    or ODE.
#  - Be able to compute (by hand) the backward Euler approximation for
#    one or two time steps, given a description of the conservation
#    problem or ODE.
#  - Be able to describe the relationship between time step and error in
#    the Euler approximation.
#  - Be able to compute the error in an Euler approximation, given the
#    analytical solution to the problem.
#
# We expect to return your graded notebooks by Monday or Tuesday of next
# week.
#
# More resources are available on the course webpage at
# <https://phaustin.github.io/eosc213/index.html>
# %% [markdown]
# ## Quiz 2 learning goals
#
# Our second quiz is scheduled for Thursday, February 28. It will be 30
# minutes long in pen and paper format. Bring a calculator.
#
#
# The learning goals for this quiz are:
#
# ### Finite Volume method
#
#  - Be able to derive a general finite-volume stencil, either
#    steady-state or transient, in one or two dimensions given the
#    geometry of the gridblocks, expressions for fluxes (eg, Fick’s law).
#    You will not be given the general stencil (N S E W) in a quiz.
#  - Be able to determine the dimensions of terms in an expression from
#    the dimensions of other variables and terms in the equation.
#  - Be able to incorporate sources and sinks in a finite-volume stencil.
#  - Be able to write discrete approximations for Fick’s law in porous
#    media.
#  - Be able to write the appropriate equations for a gridblock in a
#    finite-volume mesh, including gridblocks on the boundary.
#  - Be able to place the equations/coefficients in a system matrix A,
#    and right-hand side vector b.
#  - Be able to compute fluxes between gridblocks given the values of the
#    dependent variable in the gridblocks.
#  - Be able to formulate stencils for both explicit and implicit
#    time-stepping.
#  - Be able to describe the advantages and disadvantages of explicit and
#    implicit time-stepping schemes.
#
# ### Simulation / python
#
#  - Be able to read a code fragment in python (to the level covered in
#    the notebooks given in class up to February 26, 2019), and recognize
#    syntax errors.
#  - Can define a function and pass mandatory (args) and optional
#    (kwargs) arguments in and return values out using python. For
#    reference see for example
#    <https://phaustin.github.io/eosc213/web_notebooks/Assignment_Transient.html>
#    and explanation in
#    <https://jakevdp.github.io/WhirlwindTourOfPython/08-defining-functions.html>
#    .
#  - Can use python figure and axis objects to make a line plot with
#    multiple lines, including a legend. See
#    <https://phaustin.github.io/eosc213/web_notebooks/Lec5_Euler.html>
#    and
#    <https://clouds.eos.ubc.ca/~phil/djpine_python/chap5/chap5_plot.html>
# %% [markdown]
# ## Quiz 3 learning goals
#
# Our third quiz is scheduled for Thursday, March 14th. It will be 30
# minute in pen and paper format. Bring a calculator. The learning goals
# for this quiz are:
#
# ### Differential equations
#
# 1. Be able to take a discrete approximation to limit of infinitesimal
# volume size and time step to arrive at the partial differential
# equation.
#
# 2. Partial differential equation:
#
#    - distinguish between terms that represent fluxes, sources and
#      storage of quantities within the volume (infinitesimal point).
#    - recognize the order of the equation.
#    - recognize conservative forms
#    - be able to write the steady-state version of a PDE
#    - be able to understand the significance of the mathematical concept
#      of divergence and its relationship to flux at a point
#    - be able to recognize a partial differential equation when written
#      in vector form using divergence and gradient and “nabla” notation.
#    - be able to analyze units
#    - be able to predict the asymptotic solutions of simple boundary
#      value problems
#    - give a physical interpretation of a PDE
#    - be able to simplify a partial differential equation when
#      coefficients are constant.
#
#
# 3. Be able to set up boundary value problem:
#
#    - define domain of the problem.
#    - define the equations that govern the dependent variable.
#    - define the parameters of the equation, and if they are spatially
#      homogeneous (do not vary in space) or heterogeneous.
#
#
# #### Math Details
#
# For the mathematical/physical/pde concepts, refer to the notebook
# <https://phaustin.github.io/eosc213/web_notebooks/9_pdes_1.html>
#
# - understand the conservation/continuity equation (equations
#   13,24,27,28,31). Be able to explain what it means, what are the
#   different terms, ... If **provided** with certain fluxes, be able to
#   know the units (diffusion coefficient, darcy-velocity, heat fluxes, ...
#   for example).
#
# - be able to manipulate this equation (write it with nabla, divergence,
#   gradient, ... be able to specify it in 1D, 2D, steady-state, ...) and
#   simplify it if certain assumptions are given.
#
# - understand concepts of divergence, fluxes
#
# - understand the link between the PDE and the stencil (how to
#   approximate the derivatives of the fluxes based on discrete
#   approximation: west-center-east).
#
# - if given certain boundary conditions in certain problem, be able to
#   conceptually draw the steady-state solution.
#
# For concrete examples to practise and understand the different
# influences of boundary conditions, solution profiles, the 1d transient
# assignment or the different notebooks we have covered should really help
# you. Run these programs, modify boundary conditions. You can do the same
# with the first part of the 2d transient assignement (it includes
# multiple types of boundary conditions, can deal with heterogeneities,
# source terms). You can play around to understand the link between
# boundary conditions and steady-state solutions and build your intuition.
#
# For the classes, the example given today in class (or in 2D assignment)
# can help you with that. For function practise, try to develop your own
# function. Look at the function "harmonic averaging" of the 2D transient
# assignement and modify it to a geometric or arithmetic averaging. You
# can take any simple problem you want and put it in a function (absolute
# value, square, opposite, ...) for good practise. We learn coding by
# coding!
#
# ### Simulation / python
#
#
# 1. Be able to read a code fragment in python (to the level covered in
#    the notebooks given in class up to March 12, 2019), and recognize syntax
#    errors, or predict the result of simple short functions.
#
# 2. Be able to define a simple class that contains class variables,
#    instance variables and instance methods and use it to pass parameters
#    into and out of a function.
#
# 3. Be able to write basic functions with default values (similar than
#    quiz 2)
#
#
#
# For the Python questions:
#
# - check out last quiz: you should be able to do that question
#
# - the notebooks about classes today: you should be able to predict the
#   value "30" which was asked in class. And to add a function(method) in
#   the class.
#
#
#
# %% [markdown]
# ## Quiz 4 learning goals
#
# Our last quiz is scheduled for Thursday, March 28. It will
# be 30 minutes in pen and paper format. Bring a calculator.
#
#
# The learning goals for this quiz are:
#
# ### Computational methods
#
#  - Be able to develop finite-difference approximations for first and
#    second derivatives (total and partial).
#  - Be able to determine the truncation error and order of a finite -
#    difference approximation from Taylor-series analysis.
#  - Can construction forwards, backwards and central finite difference
#    approximation stencils.
#  - Can distinguish truncation error from roundoff error.
#  - Can identify the controls truncation error, and recognize
#    pathological situations which lead to large truncation errors.
#  - Using a finite-difference stencil, can construct the system of
#    equations for a finite-difference approximation to an ordinary or
#    partial differential equation, including defining the grid of nodes
#    and applying first-type (Dirichlet) and second-type (Neumann)
#    boundary conditions.
#
# ### Mathematics
#
#  - Be able to read a partial differential equation:
#      - distinguish between terms that represent fluxes, sources and
#        storage of quantities within the volume (infinitesimal point).
#      - recognize the order of the equation.
#      - recognize conservative forms
#      - recognize flux terms
#      - understand the physical meaning of terms in a partial
#        differential conservation law equation
#      - identify dimensions of terms in equations
#  - Be able to simplify a partial differential equation when
#    coefficients are constant.
#
# ### Be able to set up boundary value problem:
#
#  - define domain of the problem.
#  - define the equations that govern the dependent variable.
#  - define the parameters of the equation, and if they are spatially
#    homogeneous (do not vary in space) or heterogeneous.
#  - distinguish between the principal boundary conditions that prevail.
#  - assign initial conditions (if a time dependent problem).
#  - Determine that a solution satisfies the boundary value problem.
#
# ### Simulation / python
#
#  - Pandas
#      - Be able to use the apply method to execute a function on every
#        row of a dataframe
#      - Be able to add a column to a data frame and use groupby with
#        that column to group dataframe rows into subset dataframes
#      - Be able to do simple statistics (mean, median, max, min,
#        summary) on dataframes and dataframe series
#      - Be able to construct dataframes from lists of tuples, lists of
#        dictionaries, or numpy arrays using from_records member
#        function
