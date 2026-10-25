# Output scaling and color management

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](blackmagic-cloud-and-project-media-location.md) / [Next section](display-lut-and-raw-image-data.md)
<a id="source-color-management"></a> <a id="source-color-space-and-transforms"></a> <a id="source-dolby-vision"></a> <a id="source-hdr-vivid"></a> <a id="source-hdr10"></a> <a id="source-lookup-tables"></a> <a id="source-output-scaling"></a>

### Output Scaling

Should you wish, these settings let you pick a separate resolution to send out through your video output hardware — whether for monitoring, tape output, or rendering. Specifically, when you set the resolution inside the Render Settings list on the Deliver page to anything besides the Timeline Resolution, these settings carry out that conversion (for instance, when you render a downconversion of the present timeline). It comes in handy when your project sits at a high 4K resolution yet you wish to monitor on an HD display and ship HD media out for sign-off.

- Match timeline settings: On by default, which keeps these settings aligned with the Timeline Resolution, Image Scaling, and Input Image Scaling settings covered above. Clear this checkbox to assign separate settings for monitoring, tape output, or rendering through the remaining controls in this cluster.
- Output resolution: Lets you pick an alternate resolution.
- For: Lets you state a different custom alternate resolution.
- Pixel aspect ratio: Lets you state an alternate pixel aspect ratio matching the alternate

timeline format.

- Mismatched resolution files: Lets you pick an alternate approach to handling mismatched resolution

files, given the alternate resolution you settled on. These options behave exactly like those in the “Input Image Scaling” cluster.

- Super Scale: Engages an extremely processor-heavy, high-quality upscaling algorithm that genuinely fabricates new pixels for the enlarged image. Its allowed values are: None, 2-3-4x, 2-3-4x Enhanced, and Auto.

Additional Super Scale details appear in Chapter 11, “Image Sizing and Resolution Independence.”

### Color Management

The assorted controls in the Color Management panel let you set up DaVinci Color Management (RCM) or ACES once either is switched on, and they additionally let you apply pre- or post-processing to the DaVinci Resolve image processing pipeline through LUTs and Broadcast Safe settings, so a broad spread of color workflows can be supported.

### Color Space and Transforms

Selecting DaVinci YRGB Color Managed or ACES from the Color Science menu up top switches on the remaining drop-down menus throughout this section. To dig deeper into DaVinci Resolve Color Management together with ACES, turn to Chapter 9, “Data Levels, Color Management, and ACES.” Anyone fresh to color or color management is urged to study that chapter. Once you opt for Resolve Color Management (RCM), ACEScc, or ACEScct, the controls in this panel grant broad authority over how color gets transformed: it begins with picking the default color treatment for your project’s source media (through the Input Color Space), moves on to dictating how you want the DaVinci Resolve grading controls to respond (through the Timeline Color Space), and finishes by defining how the final color appears on your monitor and output device (through the Output Color Space).

- Color science: Four selections decide whether color management runs manually or automatically. DaVinci YRGB color science: The founding color science of DaVinci Resolve, where every color transform from one space to another is handled by hand, using LUTs or manual tweaks. DaVinci YRGB Color Managed: Switches on the Resolve color-managed workflow (RCM) for grading. ACEScc or ACEScct: A pair of standardized color-management approaches offered to shops running ACES workflows. Among the options, ACEScct suits most colorists best, since it raises shadows in a way that proves creatively handy.

Further coverage of Color Management plus ACES sits in Chapter 9, “Data Levels, Color Management, and ACES.”

- ACES version: This drop-down surfaces only after you select one of the DaVinci ACES choices in the Color science drop-down menu. It lets you move among the various releases of the ACES specification, so you can pick whichever older ACES version fits when reopening a legacy project.
- Use Separate Color Space and Gamma: While this checkbox stays off (the default), the Color Management panel of the Project Settings shows a single drop-down apiece for the Input, Timeline, and Output Color Space settings, and each one converts gamut and gamma together according to whatever option you pick. Switch the checkbox on and the Color Management panel shifts so the Input, Timeline, and Output Color Space settings each present two pop-ups. The leading drop-down sets the gamut on its own, whereas the second drop‑down sets the gamma on its own.

A dedicated chapter walks through the basic and advanced global controls that Resolve Color Management (RCM) offers, supplying fuller detail. You’ll find it at Chapter 9, “Data Levels, Color Management, and ACES.”

### Dolby Vision™

A GPU-accelerated software build of the Dolby Vision CMU (Content Mapping Unit) ships within DaVinci Resolve, supporting Dolby Vision grading and finishing workflows directly inside either the free edition of DaVinci Resolve or DaVinci Resolve Studio. You switch it on and configure it from the Color Management panel of the Project Settings through the Enable Dolby Vision checkbox.

s Dolby Vision controls shown within the Project Settings Color Management panel; the available count is five:

- Enable Dolby Vision: Switches Dolby Vision on and off. While active, this checkbox surfaces the Dolby Vision palette over in the Color page.
- Dolby Vision version drop-down: Picks which release of the Dolby Vision algorithms is in use. As of this writing, the choices cover 2.9 and 4.0.
- Analysis tuning: Pick among assorted choices governing how Dolby Vision examines and manages highlight retention.
- Master Display drop-down: Picks the nit level and gamut belonging to the master HDR display you grade against.
- Use External CMU: This checkbox decides whether the built-in software CMU or a connected hardware CMU on your DaVinci Resolve workstation does the work.

NOTE: Every DaVinci Resolve user has access to the Dolby Vision controls for monitoring and for auto-generating Dolby Vision metadata, which lets you build additional HDR and SDR deliverables out of the HDR grade you produced. That said, to layer manual trims atop the auto-generated analysis, licensing is required: write to dolbyvisionmastering@dolby.com to learn how one is obtained.

### HDR10+

The fresh HDR10+ HDR format from Samsung is supported by DaVinci Resolve. Be aware that, since this is a new standard, the support remains a work in progress. Once switched on, an HDR10+ palette presents trimming parameters with which you can trim an automatic downconversion of HDR to SDR, producing metadata that dictates how HDR-strength highlights render across the range of compatible televisions and displays. You enable and configure this from the Color Management panel of the Project Settings using the Enable HDR10+ checkbox. Switching HDR10+ on surfaces the Dolby Vision palette within the Color page.

HDR10+ settings in the Color Management panel of the Project Settings

### HDR Vivid

Put out by the China UHD Video Industry Alliance (CUVA), HDR Vivid is an HDR video technology standard. Working in this format guarantees broad compatibility across HDR televisions, phones, computers, and additional devices throughout China.

HDR Vivid settings in the Color Management panel of the Project Settings

### Lookup Tables

This cluster of controls lets you attach LUTs to the Resolve image processing pipeline so that every timeline across the whole project is affected together. Such LUTs serve numerous purposes — trimming Timeline grades, performing Log to Linear conversions, mimicking film output, and clamping the signal to satisfy Broadcast Safe requirements among them. Various options let you slot image processing into separate pipeline stages, illustrated in this diagram: Monitored Image
