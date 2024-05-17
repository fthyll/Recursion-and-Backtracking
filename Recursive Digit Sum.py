def superDigit(n, k):
    # Function to calculate the super digit of a number
    def calculate_super_digit(num):
        if len(num) == 1:
            return int(num)
        else:
            return calculate_super_digit(str(sum(int(digit) for digit in num)))

    # Calculate the super digit of n
    super_digit_n = calculate_super_digit(n)

    # Multiply the super digit of n by k
    super_digit_n *= k

    # Calculate the super digit of the multiplied result
    result = calculate_super_digit(str(super_digit_n))
    
    return result

if __name__ == '__main__':
    # Read inputs
    n, k = input().rstrip().split()
    k = int(k)
    
    # Calculate and print the super digit
    result = superDigit(n, k)
    print(result)
