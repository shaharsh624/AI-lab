x1 = [0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1]
x2 = [0.353, 0.471, 0.353, 0.647, 0.705, 0.882, 0.705, 1]
t = [0, 1, 0, 1, 0, 1, 0, 1]
y = [0 for _ in range(len(t))]
w1 = 0
w2 = 0
b = 0
alpha = 0.1
EPOCHS = 50


for _ in range(EPOCHS):
    for i in range(len(t)):
        y[i] = (w1 * x1[i]) + (w2 * x2[i]) + b

        if y[i] >= 0:
            y[i] = 1
        else:
            y[i] = 0

        if y[i] != t[i]:
            w1 += alpha * (t[i] - y[i]) * x1[i]
            w2 += alpha * (t[i] - y[i]) * x2[i]
            b += alpha * (t[i] - y[i])

print(y)
print("{:.2f}".format(w1), "{:.2f}".format(w2))
print("{:.2f}".format(b))
