# Setting up an asaf mix and creating an asaf master bus

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](dragging-a-control-point-and-or-right-click-to-delete-a-point.md) / [Next section](head-and-room-simulation.md)
<a id="source-asaf-master--active-resources"></a> <a id="source-asaf-master-controls"></a> <a id="source-audio-inspector-controls"></a> <a id="source-content-type"></a> <a id="source-creating-an-asaf-master-bus"></a> <a id="source-creating-an-asaf-master-bus-1"></a> <a id="source-panning"></a> <a id="source-sending-audio-to-the-asaf-master"></a> <a id="source-setting-up-an-asaf-mix"></a>

### Setting Up an ASAF Mix

Because Apple Spatial Audio Format is so deeply woven into DaVinci Resolve, building an Apple Immersive mix comes down to little more than adding an ASAF Master bus to your project and pointing your audio tracks and buses at it.

### Creating an ASAF Master Bus

To build your ASAF Master bus: 1 Head to Fairlight > Bus Format. 2 Once the Bus Format dialog appears, either convert the existing Stereo bus into an ASAF master or click the Add Bus button down in the lower left. 3 Should you opt to make a new bus, rename it however you like (say, ASAF), then choose Apple Spatial Audio Format > ASAF Master from the matching dropdown in the Format column and click OK.

### Creating an ASAF Master Bus

A fresh ASAF Master Bus channel strip, marked with an Apple logo across its top, joins the mixer, and a matching track header turns up on the timeline.

ASAF Master Bus Channel Strip (left), ASAF Master Bus Track Header (right)

### Sending Audio to the ASAF Master

As you route audio into the ASAF Master, keep these points in mind: An Ambisonic bus (ASAF Scene or native Ambisonic) sent to the ASAF Master turns into a Scene inside the Master.

- The ASAF master accepts just one Ambisonic bus — meaning either an ASAF Scene bus or a native Ambisonic bus, not both.
- That new scene inside the ASAF Master can take in any number of additional Scenes routed its way.
- As many as 128 mono objects can feed into Scene busses.

Any non-Ambisonic bus pointed straight at the ASAF Master becomes a static Channel Bed matching the source format — stereo, 5.1, or 7.1.4, for instance.

- No more than 8 non-Ambisonic busses may route directly into the ASAF Master.
- Within the Track Index, a Bus can become a Dynamic Object by switching its Type from

Channels to Object. Audio tracks of any format can be routed straight to the ASAF Master as Dynamic Objects.

- As many as 128 mono objects can route directly into the ASAF Master.
- Each stereo object is made up of two mono objects.

### Panning

On every track, the 2D, 3D, Spherical, or Cartesian View Panners let you place your sources along both the horizontal and vertical planes. Any channel-based format will do — mono, stereo, or 7.1.2, say — and you can set them within the spherical sound field. To dig deeper into the 2D and 3D Panners, turn to Chapter 177, "Mixing in the Fairlight Page."

### Audio Inspector Controls

When finer adjustments are called for, pick a track or Bus and open the Inspector’s Audio tab to surface a set of extra controls. For more on the Audio Tab, see Chapter 176, “The Fairlight Inspector.”

### ASAF Master Controls

### Content Type

This section’s drop-down menus let you set the parameters below:

ASAF Master – Content Type section of the Audio Inspector

- Content Kind: Through this dropdown you choose a label for the content the ASAF Master delivers. Your options are Movie or Music.
- Monitor Mix Path: Here you set the playback monitoring path the audio signal takes while you mix the project. The options run: Virtual Reality Virtual Reality + Speakers Headphones Headphones + Speakers Speakers
- Reverb Preset: Lets you drop one of the on-hand reverb settings onto the ASAF Object signals. The categories on offer break down as follows. Under Room Reverbs you’ll find Small, then Medium, Large, and Large 2, followed by Office 50m3 and Office Hallway, then the treated set — Treated Room 133m3, Treated 500m3, and Large Treated Room 800m3 — plus Studio 200m3, Untreated Room 210m3, and the pair Small Tiled Room and Medium Tiled Room

Among Hall Reverbs sit Medium, then Medium 2 and Medium 3, alongside Large and Large 2. There is also a Plate Reverb. The Chamber Reverbs come as Medium or Large, and a Cathedral is offered too. For the open-air choices, Outdoor Environments give you Outdoor and Outdoor Park. TIP: A click on the icon at the upper-right corner brings up the Space View plugin, where you can watch the live positions and scripted movements of audible sound sources. For more, turn to this chapter’s Space View section Active Resources

### ASAF Master – Active Resources

Active resources give you a tally of the audio resources within your ASAF mix, laid out below:

- Objects: How many dynamic objects the current timeline uses. The cap on dynamic objects is 128, across any audio format or mix of formats. Route a 7.1 track to the ASAF Master, though, and it consumes 8 of those 128.
- Headlocked: How many Headlocked objects sit on the current timeline, capped at 15.
- Scene Objects: How many dynamic scene objects on the current timeline are routed into

an ASAF Scene. Scene Objects may be in any audio format, but a project tops out at 128 of them.

- Scenes: Flags when an ASAF Scene (bus) is routed to the ASAF Master. There’s a ceiling of one ASAF Scene per project, yet any number of Scene Objects can route into that ASAF Scene.
- Channels: How many static channel Beds (buses) feed the ASAF Master. A project allows at most 8 Beds. Beds can be in mono, 2.0, LCR, Quad, 5.0, 5.1, 5.1.2, 5.1.4, 7.0, 7.1, 7.1.2, 7.1.4, 7.1.6, or 9.1.6 format.
