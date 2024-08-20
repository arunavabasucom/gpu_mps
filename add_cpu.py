from array import array
import math

# Create an array of floats from 1 to 999 (assumed to be in radians)
A = array('f', range(1, 10**8))

# Create an array to store the sine values
sine_values = array('f', (math.sin(x) for x in A))

# Print the sine value at the first index (which corresponds to the sine of 1 radian)
print(f"Sine of {A[1]} radians: {sine_values[1]}")
