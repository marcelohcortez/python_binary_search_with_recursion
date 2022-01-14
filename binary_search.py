import random
from list import listOfNumbers

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0

    if high is None:
        high = len(list) -1

    if high < low:
        print('\nThat number is not on the list\n')

    midpoint = (low + high) // 2

    if list[midpoint] == target:
        print(f'\nThe chosen number was in position {midpoint}')
        return
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, high)

if __name__ =='__main__':
    target = int(input('\nSelect a number from 1 to 50000 to search for: \n'))
    print(binary_search(listOfNumbers, target, low=None, high=None))
