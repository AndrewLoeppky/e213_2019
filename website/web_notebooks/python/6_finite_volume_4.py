# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ''
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.0-rc2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.8
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: true
#     toc_position:
#       height: calc(100% - 180px)
#       left: 10px
#       top: 150px
#       width: 358.523px
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#One-dimensional-steady-state-finite-volume-approximation---cont'd" data-toc-modified-id="One-dimensional-steady-state-finite-volume-approximation---cont'd-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>One-dimensional steady-state finite-volume approximation - cont'd</a></span><ul class="toc-item"><li><span><a href="#Summary-to-this-point" data-toc-modified-id="Summary-to-this-point-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Summary to this point</a></span></li><li><span><a href="#1.-Write-the-total-fluxes-in-terms-of-specific-fluxes:" data-toc-modified-id="1.-Write-the-total-fluxes-in-terms-of-specific-fluxes:-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>1. Write the total fluxes in terms of specific fluxes:</a></span></li><li><span><a href="#2.-Write-specific-fluxes-in-terms-of-Fick's-law." data-toc-modified-id="2.-Write-specific-fluxes-in-terms-of-Fick's-law.-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>2. Write specific fluxes in terms of Fick's law.</a></span></li><li><span><a href="#3.-Discrete-approximation-for-Fick's-law" data-toc-modified-id="3.-Discrete-approximation-for-Fick's-law-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>3. Discrete approximation for Fick's law</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Your turn</a></span><ul class="toc-item"><li><span><a href="#Your-answer-here:" data-toc-modified-id="Your-answer-here:-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Your answer here:</a></span></li></ul></li><li><span><a href="#Python" data-toc-modified-id="Python-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Python</a></span><ul class="toc-item"><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.6.1"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.6.2"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Your turn</a></span></li></ul></li></ul></li><li><span><a href="#1-D-steady-state-diffusion-stencil" data-toc-modified-id="1-D-steady-state-diffusion-stencil-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>1-D steady-state diffusion stencil</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-2.0.1"><span class="toc-item-num">2.0.1&nbsp;&nbsp;</span>Your turn</a></span></li></ul></li><li><span><a href="#Reflection" data-toc-modified-id="Reflection-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Reflection</a></span></li></ul></li></ul></div>
# %% [markdown]
# ## One-dimensional steady-state finite-volume approximation - cont'd
#
# ### Summary to this point
#
# We want to express the fundamental 1-D steady-state stencil for an interior gridblock C, with neighbours E, W:
# \begin{align}
# \left(J_{EC}+J_{WC}\right) &= 0 \label{eq5141}\\
# \end{align}
#
# in terms of concentrations. We laid out a three-step program:
#
# ### 1. Write the total fluxes in terms of specific fluxes:
# For a mesh with gridblocks of constant size $\Delta x$, $\Delta y$, $\Delta z$ and fluxes along the x-coordinate direction, we can write:
#
# <img src="figures/jwc-general.png" style="width: 160px;" >
#
# \begin{align}
# &J_{EC}=j_{EC}(\Delta y) (\Delta z)\label{eq5143}\\
# &J_{WC}=j_{WC}(\Delta y) (\Delta z)\label{eq5142}\\
# \end{align}
#
#
# because the  area of the face orthogonal to the $x$ direction is $(\Delta y)(\Delta z)$.
#
# So in terms of specific fluxes the fundamental 1-D steady-state stencil becomes:
#
# \begin{align}
# &\left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) = 0 \label{eq5144}\\
# \end{align}
#
#
# ### 2. Write specific fluxes in terms of Fick's law.
# Since both $j_{EC}$ and $j_{WC}$ are aligned with the $x$ coordinate direction, the appropriate component of the flux vector is $j_x$:
#
# \begin{align}
# j_x &= - D\theta{\partial c \over \partial x} \label{eq5145}\\
# \end{align}
#
#
#
# %% [markdown]
# ### 3. Discrete approximation for Fick's law
#
# Consider the stencil below
#
# <img src="figures/1d_stencil_w_nodes_dx_nodes.png" style="width: 200px;" >
#
#
#
# To approximate specific fluxes such as $j_x = - D\theta {\partial c \over \partial x}$ in terms of concentrations at nodal values in the centre of gridblocks, we use **finite-difference approximations**, which are motivated by the definition of the derivative:
#
# \begin{align}
# {\partial c \over \partial x} &= \lim_{\Delta x \rightarrow 0} {c(x+\Delta x) - c(x)\over \Delta x} \label{eq5146}\\
# \end{align}
#
# where $c(x+\Delta x)$ is notation for "the concentration at the point $x+\Delta x, y, z$."
#
# We can use this idea to approximate the component of the gradient in **Fick's law** \ref{eq5145} and compute the fluxes $j_{EC}$ and $j_{WC}$ in terms of values of concentration located at the centers of gridblocks **E, C, W** as (here for the case where $\Delta x$ are the same for each gridblock, so that the nodes are separated by a distance $\Delta x$):
#
# \begin{align}
# j_{EC} &\approx D\theta {c_E - c_C \over \Delta x}  \label{eq5147}\\
# \end{align}
#
# Recall that by our convention, $J_{EC}$ and $j_{EC}$ are positive ($>0$) when mass is entering gridblock C.
#
# ### Your turn
# Assume at some instant in time, $c_E=15~mg/L$ and $c_C=20~mg/L$.
# %% [markdown]
# <div class="alert alert-info">
#
#
#
# #### Your answer here:
# 1. Is mass diffusing into or out of the gridblock C? How do you know?
# 2. Is the sign of the flux $j_{EC}$ computed using the finite difference approximation above, Eq (\ref{eq5147}) consistent with our sign convention?
# </div>
# %% [markdown]
# ### Python
# If $\Delta x= 0.1 m$, $\Delta y=0.15 m$, and $\Delta z=0.12 m$, and the diffusion coefficient is $D=2\times 10^{-10}~m^2/s$, and the porosity is $\theta = 0.25$, write a short python code to compute $j_{EC}$ and $J_{EC}$
# %% {"scrolled": true}
"""
Code fragment to compute specific and total fluxes j_ec and J_ec
"""
dx = 0.1
dy = 0.15
dz = 0.12
diff_coef = 2.0e-10
poros = 0.25
j_ec_spec = 11111  # replace 0 with your code
j_ec_tot = 99999  # replace 0 with your code
units_spec = "PUT CORRECT SPECIFIC FLUX UNITS HERE"
units_tot = "PUT CORRECT TOTAL FLUX UNITS HERE"
output_text = f"""
    The specific flux j_ec is {j_ec_spec} {units_spec}
    and the total flux is
    J_ec {j_ec_tot} {units_tot}
    """
print(output_text)

# %% [markdown]
# <div class="alert alert-info">
#
# #### Your turn
#
# The approximation for $j_{EC}$ is given above in equation \ref{eq5148}.
#
# Write the corresponding discrete approximation for $j_{WC}$ in terms of $D\theta$, $c_W$, $c_C$ and $\Delta x$, $\Delta y$, and $\Delta z$.
#
# </div>

# %% [markdown]
# <div class="alert alert-info">
#
# #### Your turn
# \begin{align}
# j_{WC} &\approx {????} \label{eq5148}\\
# \end{align}
#
# 1. Is the sign of the flux $j_{WC}$ computed using your expression positive for flux entering gridblock C?
# 2. Assume values for $c_w$ and $c_C$, and show that the sign works out.
# </div>

# %% [markdown]
# ## 1-D steady-state diffusion stencil
#
# Bringing it all together, the 1-D steady-state diffusion stencil in terms of specific fluxes
#
# \begin{align*}
# &\left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) = 0 \\
# \end{align*}
#
# becomes in terms of concentrations:
#
#

# %% [markdown]
# <div class="alert alert-info">
#
# #### Your turn
# -replace $j_{WC}$ with the correct expression in terms of concentration.
#
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   j_{WC}   \right) (\Delta y) (\Delta z) = 0 \label{eq5149}\\
# \end{align}
#
#
# </div>

# %% [markdown]
# ### Reflection
#
# What have you learned? What have you struggled with? Reflect on anything else you have learned or struggled with and write it here.
