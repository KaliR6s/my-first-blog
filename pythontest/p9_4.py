import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color='tab:orange')
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor='tab:orange')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('sin', color='tab:orange')  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor='tab:orange')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()