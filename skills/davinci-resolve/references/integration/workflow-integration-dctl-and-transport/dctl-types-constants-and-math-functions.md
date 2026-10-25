# DCTL types constants and math functions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Workflow integration DCTL and transport.
[Chapter index](INDEX.md) / [Previous section](dctl-function-signatures.md) / [Next section](dctl-gain-and-matrix-examples.md) / [DCTL installation and syntax prerequisites](creating-dctl-luts-and-about-dctl.md) / [DCTL transform and device declarations](dctl-function-signatures.md)


### Additional math intrinsics

| Signature | Meaning |
| --- | --- |
| `float _cosf(float x)` | Cosine; input in radians. |
| `float _acosf(float x)` | Inverse cosine; result in radians. |
| `float _asinf(float x)` | Inverse sine; result in radians. |
| `float _fdivide(float x, float y)` | x divided by y. |
| `float _frecip(float x)` | One divided by x. |

### Types and constant memory

These functions accept an integer type: `min, max, abs, rotate`. Additional supported C Math functions are: `acosh, acospi, asinh, asinpi, atan, atanh, atanpi, atan2pi, cbrt, cosh, cospi, exp10, expm1, trunc, fdim, fma, lgamma, log1p, logb, rint, round, rsqrt, sincos, sinh, sinpi, tan, tanh, tanpi, tgamma`. The vector types `float2`, `float3`, and `float4` all work. Their data fields are: `float x float y float z float w`. To build a vector value, call `make_floatN()` where N = 2, 3, or 4. You can also declare your own structure with “typedef struct.” As an illustration:

```c
typedef struct {
    float c00, c01, c02;
    float c10, c11, c12;
} Matrix;
```

When declaring constant memory, apply `__CONSTANT__`. As an illustration:

```c
__CONSTANT__ float NORM[] = {1.0f / 3.0f, 1.0f / 3.0f, 1.0f / 3.0f};
```

To hand the constant memory over as a function argument, use the `__CONSTANTREF__` qualifier, for instance:

```text
__DEVICE__ float DoSomething(__CONSTANTREF__ float* p_Params)
```

Every float value has to end with the ‘f’ character (for example `1.2f`).
