# DCTL function signatures

Version: DaVinci Resolve 20.3 Reference Manual. Context: Workflow integration DCTL and transport.
[Chapter index](INDEX.md) / [Previous section](creating-dctl-luts-and-about-dctl.md) / [Next section](dctl-types-constants-and-math-functions.md) / [DCTL installation and syntax prerequisites](creating-dctl-luts-and-about-dctl.md)
<a id="source-dctl-syntax"></a>

### Entry points and math intrinsics

Prefix each authored function with `__DEVICE__`. Put the primary `transform` after helper functions.
These are signature excerpts; provide a body when implementing a function.

```text
__DEVICE__ float2 DoSomething()
__DEVICE__ float3 transform(float p_R, float p_G, float p_B)
```

The primary transform returns `float3`. The following signatures return `float`.
The shared DCTL intrinsic signatures follow the [official Fuse SDK math tables](https://documents.blackmagicdesign.com/UserManuals/Fusion_Fuse_SDK.pdf#page=132), which distinguish clamping from saturation and correct malformed signatures in the Resolve manual.
Check the installed Resolve developer documentation for host and version availability.

| Signature | Meaning |
| --- | --- |
| `float _fabs(float x)` | Absolute value. |
| `float _powf(float x, float y)` | x raised to y. |
| `float _logf(float x)` | Natural logarithm. |
| `float _log2f(float x)` | Base-2 logarithm. |
| `float _log10f(float x)` | Base-10 logarithm. |
| `float _exp2f(float x)` | Base-2 exponential. |
| `float _expf(float x)` | Base-e exponential. |
| `float _copysignf(float x, float y)` | Magnitude of x with the sign of y. |
| `float _fmaxf(float x, float y)` | Larger value. |
| `float _fminf(float x, float y)` | Smaller value. |
| `float _clampf(float x, float min, float max)` | Clamp x to the specified bounds. |
| `float _saturatef(float x)` | Clamp x to [0, 1]. |
| `float _sqrtf(float x)` | Square root. |
| `float _ceilf(float x)` | Round toward positive infinity, with a float result. |
| `float _floorf(float x)` | Round toward negative infinity, with a float result. |
| `float _fmod(float x, float y)` | x minus y times trunc(x/y). |
| `float _fremainder(float x, float y)` | Floating-point remainder; listed in the Resolve 20.3 manual. |
| `float _round(float x)` | Nearest integral value, with a float result. |
| `float _hypotf(float x, float y)` | Square root of x squared plus y squared. |
| `float _atan2f(float y, float x)` | Angle of the vector (x, y), in radians. |
| `float _sinf(float x)` | Sine; input in radians. |
