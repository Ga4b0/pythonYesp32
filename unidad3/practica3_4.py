# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

#print('hola mundo')
l1 = []
l2 = []

for i in range(1,15):
    l1.append(random.randint(1,100))
    l2.append(random.randint(1,100))
    
fig, ax = plt.subplots()
ax.plot(l1,l2)
fig.canvas.draw()
img = np.array(fig.canvas.buffer_rgba())
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('Grafico', img)
cv2.waitKey(0)
cv2.destroyAllWindows()