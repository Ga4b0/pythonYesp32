# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 13:15:07 2025

@author: gaodg
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

ejesx =['A','B','C','D']
ejesy =[]

for i in range(1,5):
    ejesy.append(random.randint(1,100))
    
fig, ax = plt.subplots()
grafico = ax.bar(ejesx,ejesy, color='skyblue')
for grafico, ejesy in zip(grafico,ejesy):
    ax.text(grafico.get_x()+ grafico.get_width()/2,
            ejesy +1, str(ejesy), ha='center', va= 'bottom', fontsize=10, color='black')
ax.set_xlabel('Ejes x')
ax.set_ylabel('Ejes y')
ax.set_title('Grafico de barras con Open cv')
fig.canvas.draw()
img = np.array(fig.canvas.buffer_rgba())
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('Grafico', img)
cv2.waitKey(0)
cv2.destroyAllWindows()