import timeit


def logarithmic(n):
    start = timeit.default_timer()
    
    k = 0
    while n > 0:
        n = n // 2
        k += 1
    
    run_time = (timeit.default_timer() - start) * 1000
    print("logarithmic: {} Time: {:.6f} ms".format(k, run_time))
    return k


def linear(n):
    start = timeit.default_timer()
    
    k = 0
    for _ in range(n):
        k += 1
    run_time = (timeit.default_timer() - start) * 1000
    print("logarithmic: {} Time: {:.6f} ms".format(k, run_time))


def quadratic(n):
    start = timeit.default_timer()
    
    k = 0
    for _ in range(n):
        for _ in range(n):
            k += 1
            
    run_time = (timeit.default_timer() - start) * 1000
    print("logarithmic: {} Time: {:.6f} ms".format(k, run_time))


def exponential(n):
    start = timeit.default_timer()
    
    k = 0
    for _ in range(2**n):
        k += 1
    
    run_time = (timeit.default_timer() - start) * 1000
    print("logarithmic: {} Time: {:.6f} ms".format(k, run_time))
    
    
    
# Big O верхня границя складності в залежності від вхідних даних. 
# Теоретична оцінка + Big O не враховує самі операції, наприклад, додати interegs та floats, зовсім по різному.


n = 10

logarithmic(n)
linear(n)
quadratic(n)
exponential(n)
