def fizz_buzz(numbers):
    '''
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3 with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    # for i in range(len(numbers)):
    #     num = numbers[i]
    #     if num % 3 == 0:
    #         numbers[i] = "fizz"
    #     if num % 5 == 0:
    #         numbers[i] = "buzz"
    #     if num % 5 == 0 and num % 3 == 0:
    #         numbers[i] = "fizzbuzz"
    for i, num in enumerate(numbers):
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 5 == 0 and num % 3 == 0:
            numbers[i] = "fizzbuzz"


'''
Command window command 

# Run as console
ipython --no-banner -i range_vs_enumerate.py 

# Run to test. If no output is given, it means that 
# the code passed all tests
python3 -m doctest range_vs_enumerate.py

enumerate
[tup for tup in enumerate([1,2,3])] # Gives index and value
>>> [(0,1),(1,2),(2,3)]
[tup for tup in enumerate([1,2,3], start=10)] # Will start index at 10




'''
