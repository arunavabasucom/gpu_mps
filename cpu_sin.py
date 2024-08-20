import math
from array import array

def cpu_sin(input_array):
    """
    Compute the sine of an array of values using the CPU.
    
    Parameters:
    input_array (array): An array of floating-point values for which to compute the sine.
    
    Returns:
    An array containing the sine values corresponding to the input array.
    """
    # Compute sine values for each element in the input array
    return array('f', (math.sin(x) for x in input_array))

# Example usage
if __name__ == "__main__":
    A = array('f', range(1, 10**8))  # Array of values from 1 to 999
    output_sine_values_cpu = cpu_sin(A)
    print(f"Sine of {A[1]} radians (CPU): {output_sine_values_cpu[1]}")
