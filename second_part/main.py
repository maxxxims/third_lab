import numpy as np
import matplotlib.pyplot as plt

def average_start(n):
    global data
    return data[max(0, n-9): n + 1].mean()

file_names = ['signal01.dat', 'signal02.dat', 'signal03.dat']
result_numbers = [i+1 for i in range(len(file_names))]

for file_name, i in zip(file_names, result_numbers):
    data = np.genfromtxt(file_name, dtype=float)
    fit_data = np.convolve(data, np.ones((10,)) / 10, mode='valid')
    n_data = []
    for j in range(9):
        n_data.append(average_start(j))
    fit_data = np.hstack((n_data, fit_data))
    #print(len(n_data))


    #print(data.shape, np.hstack((average_start(data)[:9], fit_data)).shape)
    print(data.shape, fit_data.shape)

    plt.subplot(1, 2, 1)
    plt.grid()
    plt.plot(data)
    plt.title('Сырой сигнал номер ' + str(i))
    plt.subplot(1, 2, 2)
    plt.grid()
    plt.plot(fit_data)
    plt.title('Обработанный сигнал'+str(i))
    plt.savefig('result' + str(i) + '.jpg')
    plt.show()