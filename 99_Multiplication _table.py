#第一种方法
for row in range(1, 10):
    for col in range(1, row+1):
        print('{}*{}={}'.format(col, row, col * row), end='\t')
    print()

#第二种方法
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(j,i,i*j),end='')
    print()
