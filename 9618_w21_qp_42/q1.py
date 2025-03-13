def Unknown(x, y) -> int:
    if x < y:
        print(x + y)
        return Unknown(x + 1, y) * 2
    else:
        if x == y:
            return 1
        else:
            print(x + y)
            return Unknown(x - 1, y) // 2

# main
Unknown(10, 15)
Unknown(10, 10)
Unknown(15, 10)

def iterativeUnknown(x, y) -> int:
    result = 1
    while x!= y:
        print(x + y)

        if x < y:
            x += 1
            result *= 2
        else:
            x -= 1
            result //= 2
    
    return result
    
print("\nITERATIVE\n")
Unknown(10, 15)
Unknown(10, 10)
Unknown(15, 10)