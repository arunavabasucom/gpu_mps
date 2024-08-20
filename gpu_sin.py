from array import array
from init import MetalComputeINIT

from array import array

def gpu_sin(input_array):
    """
    Compute the sine of an array of values using a GPU and Metal shader.
    
    Parameters:
    input_array (array): An array of floating-point values for which to compute the sine.
    
    Returns:
    An array containing the sine values corresponding to the input array.
    """
    
    # Number of elements in the input array
    count = len(input_array)
    
    # Initialize Metal compute with the specified shader
    metal_compute = MetalComputeINIT("./shaders/sin.metal", "_shsin")
    kernel, dev = metal_compute.get_kernel_function_and_device()
    
    # Create a buffer for the results
    B = dev.buffer(count * 4)  # 4 because a float32 needs 4 bytes
    B_view = memoryview(B).cast('f')
    
    # Run the kernel to compute the sine of each value in input_array
    kernel(count, input_array, B)
    
    # Return the result array containing the sine values
    return B_view

# Example usage

A = array('f',range(1,10**8)) # 0..9
output_sine_values = gpu_sin(A)
print("Sine values:", output_sine_values[1])

