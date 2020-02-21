a = input('Введіть речення ')
if len(a)<2:
    print('ban')
else:
    b=a[0]+a[1]+a[-2]+a[-1]
    print(b)