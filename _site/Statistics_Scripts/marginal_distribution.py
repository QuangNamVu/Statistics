#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ref https://www.science-emergence.com/Articles/How-to-calculate-and-visualize-Kullback-Leibler-divergence-using-python-/
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import os
from scipy.stats import norm, bernoulli, uniform
from scipy.integrate import quad

FIG_PATH = os.getcwd() + "/figures/"


def p_z(z):
    # return bernoulli.pdf(z, 0, 2)
    return uniform.pdf(z, 0, 5) + 2 * uniform.pdf(z, 5, 6)


def p_xz(x):
    return norm.pdf(x, 2, 2)


def marginal_distribution(x):
    return p_z(x) * p_xz(x)


range = np.arange(-10, 10, 0.001)

fig = plt.figure(figsize=(18, 8), dpi=100)

# ---------- First Plot

ax = fig.add_subplot(1, 2, 1)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.set_xlim(-10, 10)
ax.set_ylim(-0.1, 0.25)

ax.text(-2.5, 0.17, '$p(z)$', horizontalalignment='center', fontsize=17)
ax.text(4.5, 0.17, '$p(x|z)$', horizontalalignment='center', fontsize=17)

plt.plot(range, p_z(range))
plt.plot(range, p_xz(range))

# ---------- Second Plot

ax = fig.add_subplot(1, 2, 2)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.set_xlim(-10, 10)
ax.set_ylim(-0.1, 0.25)

ax.text(3.5, 0.17, r'$p(x) = p(x|z) \dot p(z)$', horizontalalignment='center', fontsize=17)

ax.plot(range, marginal_distribution(range))

ax.fill_between(range, 0, marginal_distribution(range))

plt.savefig(FIG_PATH + 'Marginal_distribution.png', bbox_inches='tight')
plt.show()
