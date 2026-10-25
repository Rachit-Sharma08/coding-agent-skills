# Dolby vision cm v4 0 controls and previewing and trimming at different levels

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](dolby-vision-mapping-analysis-and-licensing.md) / [Next section](davinci-resolve-grading-workflow-for-dolby-vision.md)
<a id="source-dolby-vision-cm-v40-controls"></a> <a id="source-managing-dolby-vision-metadata"></a> <a id="source-previewing-and-trimming-at-different-levels"></a> <a id="source-setting-up-resolve-color-management-for-grading-hdr"></a>

### Dolby Vision CM v4.0 Controls

Choose Dolby Vision 4.0 from the Project Settings’ Color Management panel and you switch on the 4.0 build of Dolby’s content mapping algorithm, which brings up the controls below.

- Lift/Gamma/Gain: These act much the same as the Y-only Lift, Gamma, and Gain master wheels found in the Color Wheels palette, letting you trim the picture’s overall contrast levels. Per the Dolby Best Practices Guide, hold positive Lift to a ceiling of 0.025 and rely mostly on Gamma and Gain whenever the image has to be lightened.
- Saturation Gain: Trims saturation across the most strongly saturated areas of a scene. Values with lower saturation are touched less.
- Chroma Weight: Darkens the saturated regions of the picture to retain color vividness where smaller gamuts clip the image for want of saturation headroom in the highlights.
- Tone Detail: Preserves highlight contrast detail that might otherwise vanish as the highlights drop into lower dynamic ranges, typically through clipping. Pushing Tone Detail Weight up retains a greater share of highlight detail. Applied, it can lend highlight detail extra sharpness.
- Mid Contrast Bias: Shapes picture contrast in the band surrounding the computed average picture level. It lets you raise or lower contrast within the image’s midtones.
- Highlight Clipping: Cuts detail and alters the roll-off of the picture’s brighter region by clipping highlights to the degree needed. Handy when the tone mapped image surfaces unwanted detail.

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

The Primary Trims controls sitting in the Dolby Vision palette light up only after you have authorized your system with a special license that Dolby supplies. A fourth control group lives in a second palette mode, the Secondary Trims. They too become editable only once an analysis has been run and only when you hold a Dolby license.

- Secondary Saturations: A bank of slider-based vector-style controls (akin to the Hue vs. Sat curve) lets you tune the Saturation of Red, Yellow, Green, Cyan, Blue, and Magenta so you can selectively refine the outcome.
- Secondary Hues: A further bank of slider-based vector-style controls (akin to the Hue vs. Hue≈controls) lets you tune the Hue of Red, Yellow, Green, Cyan, Blue, and Magenta as you fine tune the outcome.

The Secondary Trims controls, viewed on a licensed Dolby Vision system Taken together, all this trimming metadata gives the colorist a way to steer how the iCMU or eCMU converts the image from the Mastering Display named in the Project Settings to the Target Display named in the Dolby Vision palette. The metadata travels across the whole ecosystem so your artistic intent holds up over a range of platforms and displays.

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

### Previewing and Trimming At Different Levels

On top of that, you can call on the iCMU or eCMU to preview 100 nit, 600 nit, 1000 nit, and 2000 nit renditions of your program under various gamuts, should you wish to observe how the master scales across those pairings of peak luminance level and standard. Naturally this means your DaVinci Resolve workstation or eCMU has to be hooked up to a display that can be driven to those peak luminance output levels. While far from common practice, you can also set the “Trim Controls For” drop-down menu to assorted mixes of peak luminance, gamut, and color temperature so as to visually trim your program’s grades at as many as four separate peak luminance levels, the 100 nit, 600 nit, 1000 nit, and 2000 nit reference points among them. Picking an entry from the “Trim Controls For” drop-down menu readies you to tweak trim metadata for that entry. Swapping among entries in the “Trim Controls For” drop-down menu then lets you tailor a program’s look to the peak luminance and color volume behavior of many different televisions with far finer control. Should you go to the extra trouble of running a full trim pass of your program across multiple nit levels (via the Dolby Vision controls), the Level 2 or Level 8 metadata each pass produces keeps the artistic intent as faithful as possible across a broad span of displays, striving to give the viewer the truest possible take on the director’s intent wherever it turns up. As an example, were a program graded against a 4000 nit display together with one 100 nit BT.709 trim pass, a Dolby Vision-compatible television peaking at 750 nit would lean on the 100 nit trim pass metadata to work out the best way to “split the difference” and output the signal correctly. By contrast, if the colorist ran three trim passes — the first at 100 nits, the second at 600 nits, and a third at 1000 nits — then a 750 nit-capable Dolby Vision television could draw on the 600 and 1000 nit trim metadata to put out more accurately scaled color volume and HDR-strength highlights that, relative to the colorist’s tweaks, make fuller use of that set’s 750 nit output.

### Managing Dolby Vision™ Metadata

While you work through analyzing and trimming the HDR grades shown on your Master Display so they read right on your Target Display, there will be moments when copying and pasting metadata from one clip to the next proves handy. Analysis Metadata can be copied and pasted on its own, apart from Trim Metadata and Mid Tone Offset, and when you trim across several passes you may either copy and paste metadata for all Target Displays, or — if you only mean to overwrite a single pass — copy and paste metadata for just the current Target Display. Here are the ways to move Dolby Vision Metadata between clips by copy and paste. For Analysis Metadata, do this: Pick the clip to copy from, choose Copy Analysis Metadata in the Dolby Vision palette option menu, then pick the clip to paste onto and choose Paste Analysis Metadata from that same Dolby Vision palette option menu. To handle Trim Metadata across all Target Displays, take any one of these routes:

- Pick the clip to copy from, choose Edit > Dolby Vision > Copy Trim Metadata, then pick the clip to paste onto and choose Edit > Dolby Vision > Paste Trim Metadata.
- Pick the clip to copy from, choose Copy Trim Metadata in the Dolby Vision palette option menu, then pick the clip to paste onto and choose Paste Trim Metadata from that same menu.
- Pick the clip to paste onto, then hold the Option-Shift keys down and middle-click the clip you intend to copy from.

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

- For Trim Metadata limited to the current Target Display, take any one of these routes: Pick the clip to copy from, choose Copy Trim Metadata in the Dolby Vision palette option menu, then pick the clip to paste onto and choose Paste Trim Metadata to Current from that same menu.

Pick the clip to paste onto, then hold the Option key down and middle-click whichever clip you want to copy from.

- To copy and paste Mid Tone Offset: Pick the clip to copy from, choose Copy Mid Tone Offset in the Dolby Vision palette option menu, then pick the clip to paste onto and choose Paste Mid Tone Offset from that same menu.

### Setting Up Resolve Color Management for Grading HDR

With the hardware in place, configuring Resolve itself to put out HDR for Dolby Vision mastering goes smoothly through Resolve Color Management (RCM). The steps stay largely identical regardless of the HDR mastering technology in play; only certain Output Color Space settings change. 1 In the Color Management panel of the Project Settings, set Color Science to DaVinci YRGB Color Managed. 2 Next, open the Color Management panel and point the Output Color Space drop-down at the ST.2084 setting matching the peak luminance, in nits, of your grading display. For instance, grading on a Sony BVM X300 calls for ST.2084 1000 nit, whereas grading on a Flanders Scientific XM310K calls for ST.2084 3000 nit, so that each display’s full capability is tapped. Keep in mind that whatever HDR setting you select enforces a hard clip at that setting’s top nit value. The point is to keep you from inadvertently overdriving HDR displays where doing so carries negative consequences (this limitation does not apply to every HDR display).

- ST.2084 300 nit
- ST.2084 500 nit
- ST.2084 800 nit
- ST.2084 1000 nit
- ST.2084 2000 nit
- ST.2084 3000 nit
- ST.2084 4000 nit

That setting governs nothing more than the output EOTF (think of it as a kind of gamma transform, to borrow the wording DaVinci Resolve’s UI has employed thus far). 3 After that, pick a Timeline Color Space entry that lines up with the gamut you intend to grade in and send to output. As an illustration, if your plan is to treat the Timeline as a log-encoded signal during grading and “normalize” it yourself, ARRI Log C or Cineon Film Log are the picks (this approach comes strongly advised for top results). Should you instead prefer to save effort by letting DaVinci Resolve normalize the Timeline to P3-D65 and grade like that, you can select that option too. As for setting the output gamut, the principle is this: with “Use Separate Color Space and Gamma” switched off, the Timeline Color Space setting establishes your output gamut. Switch “Use Separate Color Space and Gamma” on and you are free to name any gamut you like in the left Output Color Space drop-down menu while picking the EOTF over in the right dropdown menu (just as step 2 spelled out).

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

4 Note that, when output correctly, HDR ST.2084 signals take on a very “log-like” appearance so that a wide dynamic range can be squeezed into the bandwidth of an ordinary video signal. The job of “normalizing” this log-encoded picture into its proper look falls to the HDR display itself. Because of that, what shows in your Color page Viewer will look flat and log-like even while the same picture on your HDR reference display reads vivid and correct. When you are on a run-of-the-mill SDR computer display and want the Color Page Viewer image to look “normalized” at the cost of clipping the HDR highlights (only in the Viewer, never in the grade), the 3D Color Viewer Lookup Table setting — found under the Project Settings’ Color Management panel — lets you assign the right ST.2084 setting whose peak nit level matches the HDR broadcast display you are outputting toward. 5 One more thing: the “Timeline resolution” and “Pixel aspect ratio” your project uses (in the project settings) are written into the Dolby Vision metadata, so confirm your project sits at the final Timeline resolution and PAR before grading gets under way.
