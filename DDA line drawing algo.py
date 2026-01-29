import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
        
    Xinc = dx / steps if steps != 0 else 0
    Yinc = dy / steps if steps != 0 else 0
    
    x = x1
    y = y1
    
    X = [x]
    Y = [y]
    
    for _ in range(int(steps)):
        x += Xinc
        y += Yinc
        X.append(round(x))
        Y.append(round(y))
        
    return X, Y

if __name__ == '__main__':
    print("DDA Line Drawing Algorithm")
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        
        x_vals, y_vals = dda(x1, y1, x2, y2)
        
        plt.plot(x_vals, y_vals, marker='o')
        plt.title('DDA Algorithm')
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.grid()
        plt.show()
    except ValueError:
        print("Invalid input")
