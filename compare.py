import time
from array import array
from gpu_sin import gpu_sin
from cpu_sin import cpu_sin

def main():
    # Test array of values from 1 to 1000 for demonstration purposes
    test_values = array('f', range(1, 10**6))
    
    # Measure CPU computation time
    start_time = time.time()
    output_sine_values_cpu = cpu_sin(test_values)
    cpu_time = time.time() - start_time
    
    print(f"CPU computation time: {cpu_time:.2f} seconds")
    print(f"Sine of {test_values[1]} radians (CPU): {output_sine_values_cpu[1]}")
    
    # Measure GPU computation time
    start_time = time.time()
    output_sine_values_gpu = gpu_sin(test_values)
    gpu_time = time.time() - start_time
    
    print(f"GPU computation time: {gpu_time:.2f} seconds")
    print(f"Sine of {test_values[1]} radians (GPU): {output_sine_values_gpu[1]}")
    
    # Calculate speedup
    if gpu_time > 0:
        speedup = cpu_time / gpu_time
        print(f"The GPU is {speedup:.2f} times faster than the CPU.")
    else:
        print("GPU computation time is zero, cannot calculate speedup.")

    # # Verify if results are similar
    # for i in range(len(test_values)):
    #     if output_sine_values_cpu[i] != output_sine_values_gpu[i]:
    #         print(f"Difference found at index {i}: CPU value = {output_sine_values_cpu[i]}, GPU value = {output_sine_values_gpu[i]}")
    #         break
    # else:
    #     print("Results from CPU and GPU match exactly.")

if __name__ == "__main__":
    main()