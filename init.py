import metalcompute as mc
from pathlib import Path
from typing import Tuple

class MetalComputeINIT:
    '''
    Initialize the Metal shader and prepare the kernel function.
    '''
    def __init__(self, path: str, function_name: str):
        self.path = path
        self.function_name = function_name
        self.dev = mc.Device()
        program_code = Path(path).read_text()
        self.kernel_function = self.dev.kernel(program_code).function(function_name)
        
    
    def get_kernel_function_and_device(self) -> Tuple:
        '''
        Returns a tuple containing the initialized Metal kernel function and the device.
        '''
        return self.kernel_function, self.dev

# Example usage
