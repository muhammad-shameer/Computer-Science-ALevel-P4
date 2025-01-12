def LinearSearch(array: list[int], target: int) -> int:
    count = 0
    for element in array:
        if element == target:
            count += 1
    return f"the number {target} is found {count} times"

def PrintArray(array: list[int]):
    print(*array)

def main():
    DataArray = []
    with open("source/Data.txt", 'r') as file:
        for line in file:
            DataArray.append(int(line)) # converts the strings into actual integers
    PrintArray(DataArray)

    usr_input = int(input(("Enter a whole number between 0 and 100 inclusive: ")))
    if usr_input >= 0 and usr_input <= 100:
        result = LinearSearch(DataArray, usr_input)
        print(result)
    else:
        print("Enter a valid number")


if __name__ == "__main__":
    main()