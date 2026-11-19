xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [2.9, 3.4, 4.9, 4.7, 6.2, 6.9, 7.3, 8.6]

w, b = 0.0, 0.0

lr = 0.1

for epoch in range(1000):
    print("epoch: ", epoch)
    print("w: ", w)
    print("b: ", b)
    dw, db = 0.0, 0.0
    for x,y in zip(xs,ys):
        pred = w + x*b
        err = pred - y
        dw += 2 * err * x / len(xs)
        db += 2 * err / len(xs)
    w += lr * dw
    b += lr * db

    
