import numpy as np
import pandas as pd


num_points = 1000
x_coords = np.random.randint(0, 1001, num_points)
y_coords = np.random.randint(0, 1001, num_points)


df = pd.DataFrame({'x': x_coords, 'y': y_coords})


df.to_excel('coordinates.xlsx', index=False)

import matplotlib.pyplot as plt

df = pd.read_excel('coordinates.xlsx')


grid_size = 200  
num_grids = 1000 // grid_size


colors = plt.cm.tab20(np.linspace(0, 1, num_grids ** 2))


plt.figure(figsize=(10, 10))


for i in range(num_grids):
    for j in range(num_grids):
        subset = df[(df['x'] >= i * grid_size) & (df['x'] < (i + 1) * grid_size) & 
                    (df['y'] >= j * grid_size) & (df['y'] < (j + 1) * grid_size)]
        if not subset.empty:
            color_index = i * num_grids + j  
            plt.scatter(subset['x'], subset['y'], c=[colors[color_index]], s=10, label=f'Grid {i},{j}')

plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.title('Izgaralar Halinde Renkli Noktaların Görselleştirilmesi')
plt.grid(True)
plt.show()
