#   In the above image, n represents how many numbers are in the set of numbers.  Everything to the right of the summation symbol (sigma) is what is added each time and i represents the counter at that time.
#   If, for example, n was 10, the above image would represent the sum of all digits starting at 0 to 10, which is 385 (0 + 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100).  Please note, 102 is included in the above calculation.
#   Define a function summation_squared (n) that implements this algorithm.  Save your file as FAIA_Q19.py and upload it.

n = 0
i = 1
squared_sum = []
n_variables = [5, 2, 10]

def summation_squared (n):
    for i in range (n + 1):
        squared_sum.append(pow (i, 2))
    return(sum(squared_sum))

for temp in n_variables:
    n = temp
    squared_sum.clear()
    print(summation_squared (n))