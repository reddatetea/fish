for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            x = '{}853{}{}'.format(i1,i2,i3)
            y = float(x)
            if y%72==0 :
                print(y)
