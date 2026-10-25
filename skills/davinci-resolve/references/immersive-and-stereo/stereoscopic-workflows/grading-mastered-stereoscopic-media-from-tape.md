# Grading mastered stereoscopic media from tape

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Previous section](grading-windows-and-a-convergence-adjusted-window-in-stereo.md) / [Next section](stereoscopic-palette-clip-adjustments.md)
<a id="source-grading-mastered-stereoscopic-media-from-tape"></a> <a id="source-stereoscopic-workflows-part-2"></a>

### Grading Mastered Stereoscopic Media From Tape


Suppose someone gives you a stereo 3D muxed tape carrying a finished, mastered program that still needs grading, yet no project file or EDL accompanies it. In that case you can bring it in as separate left- and righteye media files using a supported VTR — for example HDCAM SR running in 4:2:2 x 2 mode — by enabling the “Use left and right eye SDI” checkbox located in the Capture and Playback panel of the Project Settings. As muxed stereoscopic signals come in, the software splits each eye out into its own left-eye and right-eye image files. After ingest, Scene Detection can carve the left-eye media into one bin and, to build an EDL, you can likewise carve the right-eye media into a second bin, giving you an ordered run of stereo clips ready to grade.
