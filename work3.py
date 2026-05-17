



def reverse_seq(n: int):
    res = []
    for i in range(n, 0, -1):
        res.append(i)
    return res


print(reverse_seq(5))