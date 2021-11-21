import numpy as np
import matplotlib.pyplot as plt


file_names = ['signal01.dat', 'signal02.dat', 'signal03.dat']
result_numbers = [i+1 for i in range(len(file_names))]

for file_name, i in zip(file_names, result_numbers):
    data = np.genfromtxt(file_name)
    fit_data = np.convolve(data, np.ones((10,)) / 10, mode='valid')

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