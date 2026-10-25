# Grading hybrid loggamma in DaVinci resolve and ouputting hybrid log gamma

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](hybrid-log-gamma-hlg.md)
<a id="source-generate-hdr-light-level-report-studio-version-only"></a> <a id="source-grading-hybrid-loggamma-in-davinci-resolve"></a> <a id="source-ouputting-hybrid-log-gamma"></a>

### Grading Hybrid Log­‑Gamma in DaVinci Resolve

To monitor an ST.2084 image, you need only obtain a Hybrid Log-Gamma-compatible HDR display and route the output of your video interface into that display’s input. Configuring Resolve Color Management for an HLG grade works exactly the same way as configuring it for a Dolby Vision grade, the one difference being that the Output Color Space offers four HLG options to pick from:

- Rec.709 HLG ARIB STD-B67
- Rec.2020 HLG ARIB STD-B67
- Rec.2100 HLG
- Rec.2100 HLG (Scene)

As an alternative, turning on “Use Separate Color Space and Gamma” lets you set your gamut to either Rec. 2020 or Rec. 709 while assigning Rec. 2100 HLG as the EOTF. In that case the values shown on your scopes won’t match the data-to-nit table given earlier for grading against the PQ EOTF.

### Ouputting Hybrid Log-Gamma

After you finish building an HLG grade for your program, that grade can be rendered out to any high-quality media format that handles 10-bit.

Setup and Workflows | HDR Viewers HDR Setup and Grading

### Generate HDR Light Level Report (Studio Version Only)

It is now possible to produce HDR Light Level reports straight from the Media Pool. Begin by selecting a clip in the Media Pool, then right-click and pick Generate HDR Report from the context menu. You’ll then be asked where to store the resulting HDR Light Level report, which is written as a .pdf file. Behind the scenes the tool examines every frame of rendered HDR clips and reports light level figures such as MaxCLL and MaxFALL. The report also embeds a still of the frame holding the brightest luminance, marked with a box around the spot where those peak values occurred.

An HDR Light Level report exported from DaVinci Resolve

Setup and Workflows | HDR Viewers HDR Setup and Grading
