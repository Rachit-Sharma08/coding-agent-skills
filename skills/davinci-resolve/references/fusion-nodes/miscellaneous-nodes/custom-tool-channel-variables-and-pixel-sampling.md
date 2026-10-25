# Custom tool channel variables and pixel sampling

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom tool.
[Chapter index](INDEX.md) / [Previous section](custom-tool-value-variables-n1-n8-p1x-p4x-p1y-p4y-s1-s4.md) / [Next section](custom-tool-math-functions.md) / [Custom Tool CT](custom-tool-value-variables-n1-n8-p1x-p4x-p1y-p4y-s1-s4.md)
<a id="source-channel-pixel-variables-vy1vy3-nz1nz3"></a>

### Channel (Pixel) Variables vy1..vy3 nz1..nz3

Y Vector (for image1..image3) Z Normal (for image1..image3)

NOTE: Reach for c1, c2, c3 whenever you want a pixel’s value within whichever channel is current. Doing so eases the copying and pasting of expressions. Say you key `c1/2` in as the red expression: the outcome is half the red pixel’s value out of image 1, yet paste that same expression into the blue channel and it now carries the blue channel pixel’s value instead.

For the red value of the current pixel sitting in input 1, key in r1. Where that image sits in input 2, it turns into r2.

- `get[ch][#]b(x, y)` Fetch the pixel at x,y, or 0 when it falls out of bounds—e.g., `getr1b(0,0)`
- `get[ch][#]d(x, y)` Fetch the pixel at x,y, or the edge pixel when out of bounds—e.g., `getr1d(0,0)`
- `get[ch][#]w(x, y)` Fetch the pixel at x,y, or wrap it when out of bounds—e.g., `getr1w(0,0)`

NOTE: Several different approaches exist for pointing at pixels somewhere other than the present one inside an image.

Within the description above, `[ch]` stands as a letter naming the channel you wish to reach. The `[#]` stands as a number naming the input image. Thus, to grab the red component of the current pixel (the same as r), you would reach for `getr1b(x,y)`. And to grab the alpha component of whatever pixel sits dead center in image 2, you would reach for `geta2b(0.5, 0.5)`.

- `getr1b(x,y)` Return the red value belonging to the pixel at position x, y, supposing a valid pixel were there. Should the position fall past the image’s boundaries, it would return 0.0 (all channels).
- `getr1d(x,y)` Return the red value belonging to the pixel at position x, y. Were the named position to land outside the image’s boundaries, the result would be drawn from the image’s outer edge (RGBA only).
- `getr1w(x,y)` Return the red value belonging to the pixel at position x, y. Were the named position to land outside the image’s boundaries, the x and y coordinates would wrap over to the image’s opposite side and carry on from there (RGBA only).

So as to reach other channel values through these functions, swap the r in the examples above for the right channel variable (r, g, b, a and, with the `getr1b()` functions alone, z, and so forth), per the examples above. Swap the 1 for either a 2 or a 3 in those examples so as to reach the images coming from the other image inputs.
