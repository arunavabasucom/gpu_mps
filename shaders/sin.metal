//SIN ()
#include <metal_stdlib>;
using namespace metal;
kernel void _shsin(const device float *A [[buffer(0)]],      
                   device float *B [[buffer(1)]],
                   uint id [[thread_position_in_grid]]) {
    B[id] = sin(A[id]); 
}