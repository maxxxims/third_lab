import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

file_name = 'data.txt'
GIF_FPS = 15
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


data_n = np.genfromtxt(file_name)

A = (np.eye(len(data_n)) - np.eye(len(data_n), k=-1))
A[0, len(data_n) -1] = -1


def animate(i):
    global data_n
    data_n1 = data_n - 0.5 * A @ (data_n)
    data_n = data_n1

    ax.clear()
    ax.set_ylim([0, 10])
    ax.set_xlim([0, 50])

    ax.grid()
    ax.set_title('Frame ' + str(i + 1))
    ax.plot(data_n1)


result = animation.FuncAnimation(fig, animate, frames=255)
result.save('animation.gif', writer='imagemagick', fps=GIF_FPS)
#plt.show()
print()