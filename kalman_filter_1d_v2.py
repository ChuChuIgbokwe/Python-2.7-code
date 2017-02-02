#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 28, 2017 by 1:14 AM

from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

# import numpy.random as random
import math
import filterpy.filterpy.stats as stats
def gaussian_multiply(g1, g2):
    mu1, var1 = g1
    mu2, var2 = g2
    mean = (var1*mu2 + var2*mu1) / (var1 + var2)
    variance = (var1 * var2) / (var1 + var2)
    return (mean, variance)


def update(prior, likelihood):
    posterior = gaussian_multiply(likelihood, prior)
    return posterior




z = (10., 1.)  # Gaussian N(10, 1)

product = gaussian_multiply(z, z)

xs = np.arange(5, 15, 0.1)
ys = [stats.gaussian(x, z[0], z[1]) for x in xs]
print (ys)
plt.plot(xs, ys, label='$\mathcal{N}(10,1)$')

ys = [stats.gaussian(x, product[0], product[1]) for x in xs]
plt.plot(xs, ys, label='$\mathcal{N}(10,1) \\times \mathcal{N}(10,1)$', ls='--')
plt.legend()
plt.show()
print(product)

def plot_products(m1, v1, m2, v2, legend=True):
    plt.figure()
    product = gaussian_multiply((m1, v1), (m2, v2))

    xs = np.arange(5, 15, 0.1)
    ys = [stats.gaussian(x, m1, v1) for x in xs]
    plt.plot(xs, ys, label='$\mathcal{N}$' + '$({},{})$'.format(m1, v1))

    ys = [stats.gaussian(x, m2, v2) for x in xs]
    plt.plot(xs, ys, label='$\mathcal{N}$' + '$({},{})$'.format(m2, v2))

    ys = [stats.gaussian(x, *product) for x in xs]
    plt.plot(xs, ys, label='product', ls='--')
    plt.grid(True)
    if legend:
        plt.legend()
        plt.show()


z1 = (10.2, 1)
z2 = (9.7, 1)

plot_products(z1[0], z1[1], z2[0], z2[1])

prior, z = (8.5, 1.5), (10.2, 0.5)
plot_products(prior[0], prior[1], z[0], z[1], True)
prior, z = (8.5, 0.5), (10.2, 1.5)
plot_products(prior[0], prior[1], z[0], z[1], True)

