#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ref https://www.science-emergence.com/Articles/How-to-calculate-and-visualize-Kullback-Leibler-divergence-using-python-/
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

from scipy.stats import norm
from scipy.integrate import quad
import os

FIG_PATH = os.getcwd() + "/../Statistic_Figures/"


def p(x):
    return norm.pdf(x, 0, 2)


def q(x):
    return norm.pdf(x, 2, 2)


def KL(x):
    return p(x) * np.log(p(x) / q(x))


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

ax.text(-2.5, 0.17, 'p(x)', horizontalalignment='center', fontsize=17)
ax.text(4.5, 0.17, 'q(x)', horizontalalignment='center', fontsize=17)

plt.plot(range, p(range))
plt.plot(range, q(range))

# ---------- Second Plot

ax = fig.add_subplot(1, 2, 2)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.set_xlim(-10, 10)
ax.set_ylim(-0.1, 0.25)

ax.text(3.5, 0.17, r'$p(x) +q(x)$', horizontalalignment='center', fontsize=17)

ax.plot(range, KL(range))

ax.fill_between(range, 0, KL(range))

plt.savefig(FIG_PATH + 'KullbackLeibler.png', bbox_inches='tight')
plt.show()
