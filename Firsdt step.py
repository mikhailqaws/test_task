def prime_function(low, high):
    for iter in range(low, high):
        for i in range(2,iter):
            if (iter%i==0):
                break
        else:
            print(iter)
prime_function(5, 9)