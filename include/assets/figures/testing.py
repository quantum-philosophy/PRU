#!/usr/bin/env python3

from matplotlib.ticker import MaxNLocator
import matplotlib as mp
import matplotlib.pyplot as pp
import numpy as np
import os

path = os.path.join(os.path.dirname(__file__), 'testing.pdf')

width, height, dpi = 940, 500, 72
mp.rc('font', family='Times New Roman', size=32)

steps = [1, 2, 3, 4]

candidare = [
    0.3369318544864655,
    0.5669063925743103,
    0.6535235047340393,
    0.6224241852760315,
]

reference = [
    0.486515611410141,
    0.821384906768799,
    0.944715559482575,
    0.956437349319458,
]

pp.figure(figsize=(width / dpi, height / dpi), dpi=dpi, facecolor='w',
          edgecolor='k', frameon=False)
pp.plot(steps, candidare, 'r', steps, reference, 'b')
pp.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
pp.xlabel('Step')
pp.ylabel('Error')
pp.savefig(path, dpi=dpi)
pp.show()
