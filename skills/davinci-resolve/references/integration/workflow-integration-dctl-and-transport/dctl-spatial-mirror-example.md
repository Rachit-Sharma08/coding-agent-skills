# DCTL spatial mirror example

Version: DaVinci Resolve 20.3 Reference Manual. Context: Workflow integration DCTL and transport.
[Chapter index](INDEX.md) / [Previous section](dctl-gain-and-matrix-examples.md) / [Next section](tcp-transport-wire-format-and-commands.md)
<a id="source-a-more-complex-dct-lut-example"></a>

### Spatial mirror transform

This complete DCTL example keeps the left half and samples its reflection on the right.
The dimensions and integer pixel coordinates are supplied to the transform by Resolve.

```c
// Spatial access for a mirror effect.
__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y,
                           __TEXTURE__ p_TexR, __TEXTURE__ p_TexG,
                           __TEXTURE__ p_TexB)
{
    const bool isMirror = (p_X < (p_Width / 2));
    const float r = isMirror ? _tex2D(p_TexR, p_X, p_Y)
        : _tex2D(p_TexR, p_Width - 1 - p_X, p_Y);
    const float g = isMirror ? _tex2D(p_TexG, p_X, p_Y)
        : _tex2D(p_TexG, p_Width - 1 - p_X, p_Y);
    const float b = isMirror ? _tex2D(p_TexB, p_X, p_Y)
        : _tex2D(p_TexB, p_Width - 1 - p_X, p_Y);
    return make_float3(r, g, b);
}
```
