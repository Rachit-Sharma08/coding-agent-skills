# After an automatic SDR to HDR conversion and advanced RCM setup

Version: DaVinci Resolve 20.3 Reference Manual. Context: Data levels color management and ACES.
[Chapter index](INDEX.md) / [Previous section](camera-raw-formats-and-source-media-color-space-metadata.md) / [Continue Input DRT Tone Mapping](input-drt-tone-mapping-options.md)
<a id="source-203-nit-support-for-sdr-to-hdr"></a> <a id="source-advanced-rcm-setup"></a> <a id="source-after-an-automatic-sdr-to-hdr-conversion"></a> <a id="source-choosing-a-timeline-color-space"></a> <a id="source-dual-setting-resolve-color-management"></a> <a id="source-gamut-limiting-restricting-values-within-a-larger-gamut"></a> <a id="source-input-drt-tone-mapping"></a> <a id="source-setting-the-input-color-space"></a> <a id="source-single-setting-resolve-color-management"></a> <a id="source-single-setting-vs-dual-setting-rcm"></a> <a id="source-the-davinci-intermediate-oetf-encoding-sdr-levels"></a> <a id="source-the-davinci-intermediate-oetf-seen-encoding-hdr-levels"></a> <a id="source-the-davinci-wide-gamut-color-space"></a> <a id="source-timeline-working-luminance"></a>

### After an automatic SDR to HDR conversion

Going the other direction, from HDR to SDR, the reverse takes place:

- Within your program, 0-50 nits (18% mid-gray) lands at 0-50 nits on output (no change).
- Within your program, the 51 to 100 nits band gets shifted to 51-90 nits (slightly

compressed).

- Within your program, the 101 to 1000 nits band gets shifted to 91-100 nits

(greatly compressed).

Although these ways of converting between SDR and HDR give you a workable jumping-off point, they are not meant as a hands-off fix. It is vital to run a trim pass any time you output a deliverable in a fresh color space and EOTF, so you can inspect every clip and tweak it to better the result where needed. NOTE: While converting SDR to HDR, this behavior can amplify noise in imported SDR media that happens to hold large flat sweeps of bright color. Where certain clips betray this problem, you can switch the behavior off clip by clip from the Media Pool clip contextual menu, or from the Thumbnail Timeline contextual menu on the Color page, by toggling “Inverse DRT for SDR to HDR Conversion.”

### Advanced RCM Setup

Advanced users wanting finer command of every facet of RCM can pick Custom from the Resolve Color Management preset menu. That lays bare every control there is, opening a wealth of workflow possibilities for advanced users and post production facilities. Since each setting wraps up a sizable amount of functionality, the sections to follow treat each parameter one at a time. NOTE: Older projects on RCM will carry Color science set to Legacy, so that the earlier color management settings and the effect of their color transformations on your work are preserved. To read more about how the prior generation of RCM behaves, consult the September 2020 version of the DaVinci Resolve 16 Manual.

The Custom Color Management controls within Resolve Color Management, in their revised form as of DaVinci Resolve 17

### Single Setting vs. Dual Setting RCM

RCM can be set up in two ways. With the “Use Separate Color Space and Gamma” checkbox switched off, the Color Management panel of the Project Settings shows a single drop-down apiece for the Input, Timeline, and Output Color Space settings. Each setting transforms gamut and gamma together, according to the option you pick. That makes arranging the transform you want a touch simpler.

### Single setting Resolve Color Management

Switch the “Use Separate Color Space and Gamma” checkbox on, and the Color Management panel shifts so that the Input, Timeline, and Output Color Space settings each show two popups. The first drop-down sets the gamut on its own, while the second sets the gamma on its own. That makes it plainer to see exactly which pair of transforms applies at each stage of RCM.

### Dual setting Resolve Color Management

On top of that, Dual Setting RCM lets you assign a clip in the Media Pool its own gamut transform and its own gamma transform, kept apart. Dual setting Resolve Color Management assignments as applied to Media Pool clips

### Setting the Input Color Space

This setting is the default color space that every clip in the Media Pool not otherwise identified will adopt, unless you identify the color space of these clips by hand — right-clicking them and picking an Input Color Space (and, if you like, an Input Gamma) from the contextual menu. The setting leaves media in camera raw formats alone, and likewise media carrying embedded color space metadata.

### Choosing a Timeline Color Space

The Timeline Color Space is the “working” color space that settles the way a clip’s contrast and its color get mapped for adjustment, and that in turn shapes how responsive the effects and grading controls feel while you work. Some colorists like the classic “video” color space of Rec. 709, since its controls feel familiar and comfortable, above all when mastering SDR content. Others, accustomed to log-encoded media (most likely with the Log controls), tend to favor a more film-oriented workflow with Cineon, LogC, or other wide gamut, logarithmically encoded formats. For an SDR deliverable, any color space you are at ease with will turn out fine. But for an HDR deliverable, it serves you well to pick a wide gamut Color Space (and Gamma) for the strongest results on output. Here, DaVinci Wide Gamut is an excellent pick (more on it below). Whichever Timeline Color Space you settle on, every clip in an edit is transformed out of the Input Color Space assigned to it — automatically or by hand — and into the Timeline Color Space setting to yield the final output. This is what lets you grade inside a Log-encoded timeline color space yet view a normalized or de-logged image. IMPORTANT: Once you settle on a Timeline Color Space and start grading, leave that Timeline Color Space alone, or you will alter every grade built on the mathematics it defines. The Output Color Space can always be changed to make a fresh deliverable, though every grade leans on the Timeline Color Space for a correct render. DaVinci Wide Gamut Color Space and DaVinci Intermediate Gamma Built by Blackmagic Design, DaVinci Wide Gamut (DaVinci WG) and DaVinci Intermediate serve as Timeline Color Space and Gamma settings that furnish a dependable universal internal working color space, one reaching a practical ceiling of whatever image data any camera might record. The DaVinci Wide Gamut color space is larger than BT.2020, ARRI Wide Gamut, and even ACES, so image data is never lost wherever your media originates.

### The DaVinci Wide Gamut color space

Beyond that, the primary color values of the DaVinci WG color space are positioned so that mapping source media from various cameras into this gamut automatically is highly accurate as part of the Input to Timeline Color Space conversion, while tone and saturation mapping between color spaces can run more accurately in the Timeline to Output Color Space conversion. It also helps deliver greater consistency across media from different cameras as you make manual grading adjustments (though some variation owing to differences in camera and lens systems will linger). The DaVinci Intermediate OETF gamma setting was built to pair with DaVinci Wide Gamut, supplying a fitting internal luminance mapping of high precision image data, readying it for mastering toward either HDR or SDR standards, as your needs dictate, without surrendering image data.

### The DaVinci Intermediate OETF seen encoding HDR levels

### The DaVinci Intermediate OETF encoding SDR levels

Resolve Color Management bends to your needs, so you are under no obligation to adopt DaVinci Wide Gamut/ DaVinci Intermediate as your Timeline color space if that is not your wish. Still, it carries plenty of upsides and merits a trial to see whether it improves your workflow. To read more, consult the “DaVinci Resolve Wide Gamut Intermediate” document at https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion.

### Timeline Working Luminance

This control surfaces only while the Resolve Color Management presets menu sits on Custom Settings. The Timeline Working Luminance drop-down menu lets you decide how the Input DRT (covered below) maps a source image’s maximum level into the Timeline Color Space currently chosen. The setting also fixes the maximum highlight level you can output into the Output Color Space currently chosen by way of the Output DRT. While it is usual to set this to suit the mastering standard you are grading toward, through a collection of SDR and HDR labeled settings, extra settings are on hand that let you build in more automatic highlight compression while grading. SDR 100: The customary choice for grading SDR material whose ceiling is 100 nits. HDR 500-4000: Customary choices for grading HDR material across a spread of maximum mastering levels. Provided output DRT is anything but None, the highlights will roll off in some fashion, except where inverse DRT is switched on, in which case there is no rolloff. SDR and HDR ER settings: Each of these “extended range” settings names a pair of values and opens up more headroom for bold highlight grading, since DaVinci Resolve can then compress a broader band of out-of-bounds image data without clipping, often for a smoother look. Here is the way it operates. Say you pick the setting “HDR ER 1000/2000.” In that case, the Input DRT maps the maximum brightness of each source image into the range set by the first value, 1000 nits. Then, as you grade, the signal stays unclipped until it hits the maximum range set by the second value, 2000 nits. That supplies a further 1000 nits of out-of-bounds headroom before RCM’s image processing pipeline hard clips the image data. The Output DRT next maps from the maximum brightness set by the second number (2000 nits) down to the output value defined by the Output Color Space currently chosen, compressing this out-of-bounds headroom along the way to keep as much highlight detail as the range you picked allows. Custom: Exposes a field where you can enter a specific nit value.

### 203 Nit Support for SDR to HDR

This control surfaces only while the Resolve Color Management presets menu sits on Custom Settings. Resolve Color Management can remap SDR content to HDR by mapping 100 nits to 203 nits (set as the diffuse white level) in line with the BT.2100 recommendation. That lets the peak highlights of SDR material hold their own against the markedly brighter highlights of HDR content in programs blending the two (documentaries, say), so SDR whites keep reading as white rather than gray when set beside diffuse white in HDR.

By default the checkbox that switches this on stays hidden. Whenever the Output is set to an HDR standard yet the Timeline still rests at SDR, a checkbox labeled “Use 203 nits reference for Rec.2100 HDR” — the one that remaps SDR highlights up into HDR — appears in two places: within the RCM settings on the Color Management panel under Project Settings, and within the Color Space Transform Resolve FX plugin.

The “Use 203 nits reference for Rec.2100 HDR” checkbox, found in Resolve Color Management, used to scale SDR levels suitably up into HDR color space

### Gamut Limiting, Restricting Values Within a Larger Gamut

This control surfaces only while the Resolve Color Management presets menu sits on Custom Settings. As larger gamuts for distribution take hold, delivery specifications more and more call for output to a large gamut, such as Rec. 2020, while still demanding that image values be held inside a smaller gamut, such as P3. The aim is delivery to “future-proofed” standards while heading off saturation values too high to show on consumer displays that cannot reach the full extent of those standards. In this situation, you will pick a larger gamut in Output Color Space, then pick a smaller gamut in “Limit Output Gamut To.” Once you do, every image value lying beyond the named “Limit Output Gamut To” standard is hard clipped. This setting defaults to None.

Pick an entry from the Limit Output Gamut To menu so image values stay confined inside a larger gamut
