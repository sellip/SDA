# compute the cube sum of first n natural numbers

def cube(n):
    sum = 0
    for i in range(1, n+1):
        sum +=pow(i, 3)
    return sum


print(cube(5))
print(cube(2))

