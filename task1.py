"""
Use random module with a seed of 2020 to generate 20 integers between 100 and 120 (inclusive). 
Then write code to calculate the median and mode.  The median is the 10th largest number. 
The mode is the number that occurs the most. If two or more number have the same frequency, list them all.
"""
# Import random library
import random
from math import floor

# Set random seed generator
random.seed(2020)

# Global Variables
INTEGERS = 20 # Set Number of Integers
MIN_VALUE = 100 # Min value for random list
MAX_VALUE = 120 # Max value for random list

# Create a list 20 random variables through list comprehension
LIST_1 = [random.randrange(MIN_VALUE,MAX_VALUE + 1) for _ in range(INTEGERS)]

# Median using Statistics Module
import statistics
MEDIAN_S = statistics.median(LIST_1)
print(f'Using Statistics Module, the Median is {MEDIAN_S}')

# Mode using Statistics Module
MODE = statistics.multimode(LIST_1)
print(f'Using Statistics Module, the Mode is {MODE}')

# functions
def get_median(array):
    """Returns the Median from a list"""
    if len(array) == 0:
        return '\nYour list is empty, cannot compute median'

    list_sorted = sorted(array) 
    if len(list_sorted) % 2 == 0:
        split_1 = int(len(list_sorted) / 2 - 1)
        split_2 = int(len(list_sorted) / 2)
        median = (list_sorted[split_1] + list_sorted[split_2]) / 2.0
    else:
        middle_point = floor(len(list_sorted) / 2)
        median = list_sorted[middle_point]
    return median

def get_mode(array):
    """Returns the number of Mode(s)"""
    if len(array) == 0:
        return '\nYour list is empty, cannot compute Mode'

    list_sorted = sorted(array)
    number_frequency = {}
    for num in list_sorted:
        number_frequency[num] = number_frequency.get(num, 0) + 1

    # Convert dictionary to a list sorted
    dictionary_sorted = sorted(number_frequency.items(), key=lambda x: x[1], reverse=True)
    
    # See if there is more than one mode
    mode = 0
    mode_count = 0
    for _, frequency in dictionary_sorted:
        if frequency > mode:
            mode = frequency
            mode_count = 1
        elif frequency == mode:
            mode_count += 1
        elif frequency < mode:
            break

    modes = []
    for mode, _ in dictionary_sorted[:mode_count]:
        modes += [mode]
    return modes

# Manually Calculated Median
print(f'Manually Calculated Median is {get_median(LIST_1)}')

# Manually calculating Mode
print(f'Manually Calculated Mode(s): {get_mode(LIST_1)}')
