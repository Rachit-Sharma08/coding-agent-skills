# High dynamic range HDR grading in DaVinci resolve and HDR isnt just for televisions

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Next section](dolby-cinema-and-sdr-peak-luminance.md)
<a id="source-10000"></a> <a id="source-analyzing-hdr-signals-using-video-scopes"></a> <a id="source-hdr-isnt-just-for-televisions"></a> <a id="source-hdr-setup-and-grading"></a> <a id="source-hdr-setup-and-grading-part-1"></a> <a id="source-high-dynamic-range-hdr-grading-in-davinci-resolve"></a> <a id="source-minimum-standard-for-an-ultrahd-oled-display"></a> <a id="source-no-commercially-available-display"></a> <a id="source-oled-mobile-phone-brightness"></a> <a id="source-outdoor-led-displays"></a> <a id="source-professional-sdr-displays-in-hdr-preview-mode"></a> <a id="source-the-different-ways-of-mastering-hdr"></a> <a id="source-virtual-production-wall-panels"></a> <a id="source-what-do-i-do-with-hdr"></a>

### HDR Setup and Grading

For cinema, television, and streaming, High Dynamic Range (HDR) grading represents the newest stage in how consumers experience media. Although HDR pipelines are already established in premium cinema and television, the spread of this mastering approach into cheaper programming has historically lagged. That said, recent advances together with a widening selection of affordable, HDR-capable consumer hardware are set to make HDR mastering of visual material far more commonplace. For anyone new to the subject, this chapter explains what HDR actually is and walks through the practical steps for configuring DaVinci Resolve to perform HDR grading.

The Dolby and Dolby Vision names, plus the double-D symbol, are registered trademarks belonging to Dolby Laboratories Licensing Corporation.

### High Dynamic Range (HDR) Grading in DaVinci Resolve

The HDR capabilities in DaVinci Resolve ship only with DaVinci Resolve Studio. High Dynamic Range (HDR) video refers to a developing set of encoding and distribution technologies built so that the latest television displays can show footage with extremely bright highlights and richer saturation. Broadly speaking, most of an HDR picture is graded much the way a Standard Dynamic Range (SDR) picture is today, since the shadows and midtones stay largely consistent between conventionally SDR-graded and HDR-graded images. That holds true partly because shadows are by nature dark; beyond that, keeping them aligned preserves a comfortable viewing experience and makes backward compatibility simpler whenever both an SDR and an HDR version of a program must be produced. Where HDR differs is in offering generous extra headroom for very bright highlights and color saturation well past anything SDR television and cinema could previously show. That headroom lets the colorist craft more vivid, lifelike highlights — think sunsets, lit clouds, firelight, explosions, sparkles, and similarly brilliant, saturated subjects. Put differently, you can now “open up” an image’s highlights exactly as you’ve always been able to open up, or expand, shadow detail. Beyond delivering more natural lighting intensity and saturation, this also greatly widens the contrast a scene can contain. As an illustration, a properly calibrated SDR display should peak at a luminance of 100 nits (cd/m2), whereas current HDR displays can reach peak luminance levels of 700, 1000, or even 4000 nits. Yet because the technology keeps evolving, the published technical standards reach well beyond what today’s consumer televisions, projectors, phones, and tablets can actually deliver. As things stand today, a consumer television can typically put out somewhere between 700 and 1600 nits. On top of that, consumer displays frequently include automatic brightness limiting (ABL) circuitry that caps power draw at levels appropriate for the home, so only a portion of the picture can hit those peak values simultaneously. That limitation is acceptable, since HDR isn’t about brightening the whole frame — it’s about reserving headroom for select bright highlights and added saturation. For all these reasons, HDR standards concentrate on defining what a display must be able to do, rather than dictating how those levels get used. That remains a creative decision.

### HDR Isn’t Just for Televisions

In case you assume that living-room televisions and projectors are the sole route to HDR content, several flagship iOS and Android phones and tablets now include HDR playback that can match — or even surpass — the UltraHD requirements for HDR content on an OLED display. As a result, HDR has, perhaps unexpectedly, become a broadly accessible mobile experience.

### The Different Ways of Mastering HDR

Even though each HDR technology takes its own route to mapping your program’s video levels onto an HDR display’s range, every one of them emits a “near-logarithmically” encoded signal that depends on a compatible television to stretch it correctly back into its “normalized” form for viewing. Consequently, if you view an HDR signal coming out of your grading workstation’s video interface on an SDR display, it appears flat, desaturated, and unappealing right up until it reaches your chosen HDR display. On output, a graded HDR picture resembles a log-encoded one in appearance As things stand now, DaVinci Resolve can support five main routes to HDR mastering, namely:

- Dolby Vision®
- HDR10
- HDR10+
- HDR Vivid
- Hybrid Log-Gamma (HLG) Every one of these HDR standards specifies how an HDR signal gets encoded for export and is subsequently mapped to the visible output of an HDR or SDR display. Grading toward any of them calls for a measure of color management, and DaVinci Resolve offers three principal approaches to it:
- The simplest route is to switch on Resolve Color Management (RCM) or ACES in the Color Management

panel of the Project Settings, then apply the Color Space conversion options provided there. Each supported flavor of HDR has its own option in that list.

- The same transforms RCM provides are also exposed as Resolve FX operations, should you prefer to assemble your grading pipeline by hand using the Color Transform Resolve FX adjustment.
- LUTs likewise handle each of these color space conversions, in case you want to build a bespoke image processing pipeline around custom-made LUT or DCTL transforms. On the whole, Resolve Color Management and ACES are the dependable, recommended way to tackle HDR grading in DaVinci Resolve for most situations.

To dig deeper into Resolve Color Management, refer to Chapter 9, “Data Levels, Color Management, and ACES.”

### What Do I Do With HDR?

Although these standards enable HDR mastering and distribution, they say nothing about how the HDR-strength levels ought to be employed for creative effect. That decision falls to you, because making use of the wide headroom for brightness and saturation that HDR opens up sits squarely in the colorist’s hands — a sequence of creative choices about how to map the range of highlights present in your source media onto the above-100 nit HDR levels you’re mastering toward as you grade, within the peak luminance level you’ve been assigned. The particular HDR peak luminance level you target (1000 nit, 3000 nit, 4000 nit) likely comes down to which display you can access and who is distributing the finished program.

### Analyzing HDR Signals Using Video Scopes

With any flavor of waveform scope — parade and overlay scopes included — the way HDR is encoded causes the signal to sit within the 10-bit scale used for analysis very differently than you might expect. The chart of values below should clarify how each level in “nits” (i.e., cd/m2) maps to a code value on the 10-bit image scale:

10-Bit Code 1019† 948 920 889 844 824 767 728 691 635 528 520 4†

Nearest Value in cd/m2 HDR Display Peak Luminance Capability

### 10,000

### No commercially available display

### Outdoor LED Displays

Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.

Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.

Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.

### Virtual Production Wall Panels

Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.

### OLED mobile phone brightness

### Minimum standard for an “UltraHD” OLED display

### Professional SDR displays in “HDR preview mode”

BT.2408 recommended diffuse-white value when SDR content is intercut 203 against 1000 nit max HDR content
