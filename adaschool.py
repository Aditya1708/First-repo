t = int(input())
for i in range(t):
    s = input()
    a = s.split()
    n = int(a[0])
    m = int(a[1])
    if (m%2==0 or n%2==0):
        print('YES')
    else:
        print('NO')





