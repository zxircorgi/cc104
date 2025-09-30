def display(lower, upper) :
    while lower <= upper :
        print(lower, end=' ')
        lower += 1
    print("{} {} {}".format(lower, upper, upper - lower))