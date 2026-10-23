import matplotlib.pyplot as plt
import numpy as np

x_line = np.linspace(0.1, 4.0, 500)  #500 чисел равномерно распределенных от 0,1 до 4
x_ints = np.array([1, 2, 3, 4])
plt.figure(figsize=(10, 6)) #окно графика и его размеры
plt.plot(x_line, x_line**2, label='x^2', color='gray', linewidth=3)  #график x^2
plt.scatter(x_ints, x_ints**2, color='gray', ) 
plt.plot(x_line, np.exp(x_line), label='e^x', color='blue', linewidth=3)  #график e^x
plt.scatter(x_ints, np.exp(x_ints), color='blue')
plt.plot(x_line, np.log(x_line), label='ln(x)', color='green', linewidth=3)  #график lnx
plt.scatter(x_ints, np.log(x_ints), color='green')
plt.plot(x_line, x_line**3, label='x^3', color='red', linewidth=3)  #график x^3
plt.scatter(x_ints, x_ints**3, color='red')
plt.axhline(0, color='black', linewidth=1, linestyle='--')  #горизонтальная ось
plt.axvline(0, color='black', linewidth=1, linestyle='--')  #вертикальная ось
plt.grid(True, linestyle=':', alpha=1)  #задний фон
plt.title('Графики функций с выделением целых точек', fontsize=12)
plt.xlabel('Ось X', fontsize=12)
plt.ylabel('Ось Y', fontsize=12)
plt.legend(fontsize=12)
plt.show()
