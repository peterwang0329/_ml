from micrograd.hw6_engine import Value

x = Value(2.0)
f = x.sigmoid()
print(f'{f.data:.4f}')
f.backward()
print(f'x.grad=',x.grad)
print(f'gx={x.grad:.4f}')