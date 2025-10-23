import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
pw = []
f = 100
duty1 = []
duty_in = []
freq = []
pe = []
ind = []
count = 0
for i in range(200):
    x.append(i / 100)
    y.append(
        1000 * np.sin(10 * np.pi * x[i] + 3 * np.pi / 4)
        + (300 * np.sin(2 * np.pi * x[i] + 1 * np.pi / 4))
        + 2000
    )
    if i != 0:
        pw.append(0.5 * (y[i - 1] + y[i]) / 5)
        duty = pw[i - 1] * (1 / f)
        while duty > 1:
            f = 8 * f / 7
            duty = pw[i - 1] * (1 / f)
        freq.append(f)
        duty_in.append(i)
        duty1.append(duty)
        T = 1 / f
        on = duty * T
        for t in range(100):
            if on > (t * T):
                pe.append(5)
                ind.append(count / 19000)
                count += 1
            else:
                pe.append(0)
                ind.append(count / 19000)
                count += 1
y = np.sin(x)
plt.plot(freq, duty1)
# plt.plot(duty_in, duty1)
plt.show()
