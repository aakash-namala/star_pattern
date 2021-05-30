#program to print pattern

n=int(input('Enter the range:'))
for i in range(1,n):
    for j in range(i):
        print('*',end='')
    print('\n')
