from micrograd.hw6_engine import Value

def gradientDescent(learning_rate=0.1, max_loops=100):
    x = Value(0.0)
    y = Value(0.0)
    z = Value(0.0)

    for i in range(max_loops):
        f=x*x + y*y + z*z - 2*x - 4*y - 6*z + 8
        f.backward()
        grad_x = x.grad
        grad_y = y.grad
        grad_z = z.grad
        grad_norm = (grad_x**2 + grad_y**2 + grad_z**2)**0.5
        print(f' x={x.data:.4f}, y={y.data:.4f}, z={z.data:.4f}, f={f.data:.4f}, grad_norm={grad_norm}')
        if grad_norm < 0.001:
            break
        x.data -= learning_rate * grad_x
        y.data -= learning_rate * grad_y
        z.data -= learning_rate * grad_z

        x.grad = 0.0
        y.grad = 0.0
        z.grad = 0.0

    return x.data,y.data,z.data,f.data

final_x,final_y,final_z,final_f = gradientDescent(learning_rate=0.1, max_loops=100)
print(f'final_x={final_x:.4f} final_y={final_y:.4f} final_z={final_z:.4f} final_f={final_f*(-1)}')