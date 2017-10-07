# From "https://en.wikipedia.org/wiki/Gradient_descent"
# From calculation, it is expected that the local minimum occurs at x=9/4

import matplotlib.pyplot as plt
cur_x = 6 # The algorithm starts at x=6
gamma = 0.01 # step size multiplier
precision = 0.00001
previous_step_size = cur_x
x=[]
y=[]
def df(x):
    return 4 * x**3 - 9 * x**2

while previous_step_size > precision:
    prev_x = cur_x
    cur_x += -gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    x.append(cur_x)
print("The local minimum occurs at %f" % cur_x)

plt.plot(x)
plt.text(30, 1.25, 'Local minima occurs at 9/4=2.25, analytically')
plt.xlabel("Iternation no.")
plt.ylabel("X value update")
plt.text(15, 1.05, 'That is where the gradient saturates afround after 40 iterations')
