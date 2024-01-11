def factorial(n): 
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(4))


def factorial_and_one(n): 
    result = 1
    for i in range(1, n+1):
        result *= i
    return result + 1

print(factorial_and_one(3))

def multiply(n):
    result = 1
    # n = int(input("choose a number"))
    print(n)
    for i in range(1, n+1):
        print(f'before: + {result}')
        result += i
        print(f'after: + {result}')
    return result
        
print(multiply(6))