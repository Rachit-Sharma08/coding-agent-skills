# Additional controls in the hue and sat curves

Version: DaVinci Resolve 20.3 Reference Manual. Context: Curves.
[Chapter index](INDEX.md) / [Previous section](high-clip-adjustment-and-rgb-parade.md) / [Next section](custom-lum-vs-sat-and-hue-vs-hue-sat-vs-sat.md)
<a id="source-additional-controls-in-the-hue-and-sat-curves"></a> <a id="source-curves-part-2"></a>

### Additional Controls in the Hue and Sat Curves


A handful of curves — Hue vs. Hue, then Hue vs. Sat, plus Hue vs. Lum, along with Lum vs. Sat and Sat vs. Sat — accept adjustments in much the same way as the Custom curves do, but each one carries extra controls positioned beneath its curve graph. Enable Bezier button: Switching this on forces the curve to rely on Bezier control handles instead of the standard DaVinci Resolve Curve Control points when you reshape each control point. Once Bezier handles are active, clicking any control point exposes its pair of Bezier handles, and dragging either one reshapes the curve around that point. Six-Vector Color Patches: Every Hue curve carries six buttons that automatically drop in control points for working the red/yellow/green/cyan/blue/magenta hue ranges. Pressing one of these buttons inserts three control points: a pair marking the outer edges of the hue range you intend to change, plus a central point you move to apply the change. Input and Output (Hue Rotate/Saturation/Lum) fields: This pair of numeric fields holds the horizontal and vertical adjustment amounts for whichever control point is active. Select any point on a curve to inspect or change those numbers. Which curve you've chosen determines the label shown on the second field. Detailed descriptions of each curve follow in the sections below. To reach any curve type, click its corresponding icon near the top right of the Curve Palette.
