# DCTL gain and matrix examples

Version: DaVinci Resolve 20.3 Reference Manual. Context: Workflow integration DCTL and transport.
[Chapter index](INDEX.md) / [Previous section](dctl-types-constants-and-math-functions.md) / [Next section](dctl-spatial-mirror-example.md)
<a id="source-a-matrix-dct-lut-example"></a> <a id="source-a-simple-dct-lut-example"></a>

### Gain transform

Save these as separate DCTL examples: each defines its own transform entry point.
The first applies independent RGB gains.

```c
// Simple color gain transformation.
__DEVICE__ float3 transform(float p_R, float p_G, float p_B)
{
    const float r = p_R * 1.2f;
    const float g = p_G * 1.1f;
    const float b = p_B * 1.2f;
    return make_float3(r, g, b);
}
```

### Matrix transform

This is the manual's RGB-to-YUV matrix example; retain its coefficient values.

```c
__CONSTANT__ float RGBToYUVMat[9] = {
    0.2126f, 0.7152f, 0.0722f,
    -0.09991f, -0.33609f, 0.436f,
    0.615f, -0.55861f, -0.05639f
};

__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y,
                           float p_R, float p_G, float p_B)
{
    float3 result;
    result.x = RGBToYUVMat[0] * p_R + RGBToYUVMat[1] * p_G + RGBToYUVMat[2] * p_B;
    result.y = RGBToYUVMat[3] * p_R + RGBToYUVMat[4] * p_G + RGBToYUVMat[5] * p_B;
    result.z = RGBToYUVMat[6] * p_R + RGBToYUVMat[7] * p_G + RGBToYUVMat[8] * p_B;
    return result;
}
```
