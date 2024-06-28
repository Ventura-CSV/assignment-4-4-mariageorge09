def main():

    numbers = []
    maxval = 0
    for num in range(5): 
        number = int(input('Enter your number: '))
        numbers.append(number)
    minval = numbers[0]
    for x in numbers:
        if x > maxval:
            maxval = x
    for x in numbers:
        if x < minval:
            minval = x
    print(numbers)
    print('Max Number: ')
    print(maxval)
    print('Smallest Number: ')
    print(minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
