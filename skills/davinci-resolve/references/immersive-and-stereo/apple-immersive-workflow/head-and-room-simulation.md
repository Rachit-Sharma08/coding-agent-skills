# Head and room simulation

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](setting-up-an-asaf-mix-and-creating-an-asaf-master-bus.md) / [Next section](offsets-and-asaf-objects-offsets.md)
<a id="source-3d-panner"></a> <a id="source-3d-panner-for-an-asaf-object"></a> <a id="source-apple-immersive-workflow-part-3"></a> <a id="source-asaf-object-controls"></a> <a id="source-head"></a> <a id="source-room-simulation"></a> <a id="source-world"></a>

### Head

This section’s parameters govern how the listener’s head is oriented. ASAF Master – Head section of the Audio Inspector

- Head Yaw: The listener’s head turning left to right, spanning -180 ° to +180°.
- Head Pitch: Governs the listener’s head moving up and down, as though glancing up and

down, spanning -90 ° to +90°.

- Head Roll: The listener’s head tipping side to side, “one shoulder toward the other,” spanning

-180 ° to +180°.

- HRTF: With compatible AirPods in use, this parameter flips between the Personalized

and the System default HRTF profiles. NOTE: The Yaw, Pitch, and Roll parameters refresh on their own to track your head position whenever compatible AirPods or a head-tracker are in use.

### Room Simulation

By way of the parameters below, the Room Simulation section lets you choose among various simulated materials and “build” a virtual room — its walls, its floor, its ceiling — which you then apply to your ASAF Scene Objects, with room size and reflective quality both adjustable. ASAF Master– Room Simulation section of the Audio Inspector

- Size (X): Sets the room’s width, spanning 2 to 20 meters.
- Size (Y): Fixes the room’s length, spanning 2 to 20 meters.
- Size (Z): Sets the ceiling height, spanning 2 to 20 meters.
- Floor Material, Wall Material, and Ceiling Material: Every one of these parameters hands you the same set of materials for its respective surface:

ASAF Master – Room Simulation Floor Materials section of the Audio Inspector

- Absorption: Fixes how reflective the room is.
- Room RT60: Reports how long the sound takes to fall off by 60dB (decay time) once

the audio signal falls silent.

### World

The Grid parameter sets where the Room Simulation sits vertically relative to the listener, all without altering the height of the audio object itself. In effect this raises or lowers the entire room while the listener and the audio object or objects stay put. It comes in handy when, say, you need to mimic a space with a tall ceiling while the listener sits nearer the floor.

ASAF Master – World section of the Audio Inspector Defaults These controls let you set the default panning setup handed to every new audio track.

ASAF Master – Defaults section of the Audio Inspector

- Coordinate System: Pick either the 3D Spherical or the Cartesian panner for all new tracks.
- Range: This control fixes the default value of the Panner’s Range parameter, spanning 1 to 10 meters. A Range of 1m holds panning in the room at unity. Bigger values push objects farther off, dropping their loudness just as distance would in real life.
- Set Global Defaults: A click on this button pushes the Coordinate System and Range out to every newly made Timeline.

### ASAF Object Controls

### 3D Panner

This take on the 3D Panner brings a broader set of parameters for placing an Audio Object, spelled out below.

### 3D Panner for an ASAF Object

TIP: A click on the icon at the upper-right corner brings up the 3D Panner plugin.

For more on the 3D Panner plugin, see Chapter 177, "Mixing in the Fairlight Page."

- Azimuth: Fixes the object’s horizontal angle (left to right) around the listener, spanning -180 ° to +180°. You’ll see this control only where that channel uses a 2D or 3D Spherical Panner plugin in the Fairlight mixer.
- Elevation: Fixes the object’s vertical angle above and below the listener (-90° to +90°). It surfaces solely once the channel’s Fairlight mixer Panner plugin runs in 3D Spherical.
- Radius: The gap between the object and the listener, anywhere from 0 to 10 meters in any direction. This one appears only if the channel’s mixer Panner plugin in Fairlight sits on 2D or 3D Spherical.

The ASAF renderer draws on this value, together with the Offset, to fake shifts in distance by lowering or lifting the audio signal level. An object placed 1 meter off, say, plays at unity gain, while at 10 meters it reads roughly 20dB quieter.

With the 3D Panner's Cartesian view active on an ASAF Object, X, Y, and Z parameters stand in for Azimuth, Elevation, and Radius, as laid out here: X: Drives the panner's Left/Right parameter, ranging from -10m to +10m. Y: Drives the panner's Front/Back parameter, ranging from -10m to +10m. Z: Drives the panner's Down/UP parameter, ranging from -10m to +10m. With the Panner switched to Spherical, this control stays hidden.

The Cartesian View gets a fuller account in Chapter 177, "Mixing in the Fairlight Page."

- Width: Fixes the object width, ranging from 0° to 180°.
- Height: Fixes the object height, ranging from 0° to 180°.
- Directivity: Fixes an object's directivity pattern (radiation pattern), which spells out how the audio shifts according to the object's orientation toward the listener. Say someone speaks with their back to the listener — their voice comes across as though a low-pass filter had been laid over it.
- Yaw: Fixes an object's horizontal orientation, ranging from -180 ° to +180°. With the Directivity parameter bypassed, this setting has no bearing on an object.
- Pitch: Fixes an object's vertical orientation, ranging from -90 ° to +90°. With the Directivity parameter bypassed, this setting has no bearing on an object.
- Roll: Tilts or rolls the scene from side to side.
- Follow Listener: While active, the object turns to face the listener no matter where it sits.
- Headlock: While active, an object's position holds steady even as the listener's head shifts. With Headlock off, the object's perceived location moves as the listener turns or repositions their head.

NOTE: Headlock only affects binaural rendering.

- Externalize Binaural: This parameter surfaces only while Headlock is active. With it active, HRTF kicks in as the Binaural output renders, so the audio seems to sit beyond the listener's head. Switch Externalize Binaural off and HRTF drops out of the rendering, leaving the object panned between the listener's ears.
