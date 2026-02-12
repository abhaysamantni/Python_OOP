# This program uses recursion to print numbers
# from the Fibonacci series.

import fibonacci

def main():
    print('The first 10 numbers in the')
    print('Fibonacci series are:')

    for number in range(1, 11):
        print(fibonacci.fib(number))
    


# Call the main function.
main()
