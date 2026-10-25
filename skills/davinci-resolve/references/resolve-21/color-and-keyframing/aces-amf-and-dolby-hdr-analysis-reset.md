# ACES amf improvements and reset dolby vision and HDR analysis from the option menu

Version: DaVinci Resolve 21 New Features Guide. Context: Color and keyframing.
[Chapter index](INDEX.md) / [Previous section](color-and-multimaster-trim-manager.md) / [Next section](resolve-fx-and-resolve-fx-video-collage-updated.md)
<a id="source-aces-amf-improvements"></a> <a id="source-adobe-rgb-colorspace-and-gamma-support"></a> <a id="source-advanced-color-panel-controls-for-239-and-24-safe-area"></a> <a id="source-multiple-user-projects-support-color-management-bypass"></a> <a id="source-openfx-15-color-management-apis-for-colorspace-aware-effects"></a> <a id="source-pasting-tracking-data-between-power-windows-retains-original-shape"></a> <a id="source-reset-dolby-vision-and-hdr-analysis-from-the-option-menu"></a>

### ACES AMF Improvements

Handling of ACES AMF sidecar files picks up further refinements in DaVinci Resolve 21.

- Shows the AMF transform name.
- Lets you point to a custom ACES AMF folder in project settings.
- Offers AMF tree selection via the project settings ACES AMF option menu.
- Adds support for look transforms at the project level.
- Includes an indicator showing the current working location.

### Reset Dolby Vision and HDR Analysis from the Option Menu

Both the Dolby Vision and the other HDR analyses can be cleared from the three-dot option menu sitting in each of their tabs on the Color page.

### Adobe RGB Colorspace and Gamma Support

Alongside the Photo page debut, DaVinci Resolve 21 adds support for the Adobe RGB colorspace and gamma.

### OpenFX 1.5 Color Management APIs for Colorspace Aware Effects

Support for the OpenFX 1.5 Color Management APIs has landed in DaVinci Resolve, promising sturdier, more precise color handling whenever you use or build OpenFX tools.

### Advanced Color Panel Controls for 2.39 and 2.4 Safe Area

For the Safe Area display, the DaVinci Resolve Advanced Panel now offers 2.39 and 2.4 aspect ratios. To get there, use shift down and the A/C Mode (Safe) selection found on the T-Bar panel, after which you select 2.39 or 2.4 directly on the center panel screens.

### Multiple User Projects Support Color Management Bypass

DaVinci Resolve 21 now lets you skip Color Management in a Multi User project exactly as you would in a Single User project. Right-click a clip in the Color timeline and pick Bypass Color Management from the context menu.

### Pasting Tracking Data Between Power Windows Retains Original Shape

With DaVinci Resolve 21, pasting tracking data from one Power Window to another now keeps the shape it started with.
