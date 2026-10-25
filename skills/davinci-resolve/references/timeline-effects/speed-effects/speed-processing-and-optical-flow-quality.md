# Speed effect processing and optical flow quality settings affecting speed effects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Speed effects.
[Chapter index](INDEX.md) / [Previous section](timeline-speed-controls-and-whole-clip-retiming.md)
<a id="source-optical-flow-quality-settings-affecting-speed-effects"></a> <a id="source-speed-effect-processing"></a>

### Speed Effect Processing

After retiming a clip, you gain the further option of changing how that clip gets processed so its visual playback quality improves — something that matters most for clips that have been slowed down. Two paths let you set this. The first is a project-wide setting found in the Master Settings of the Project Settings. The second is a per-clip setting in the Inspector that adjusts how clips are retimed. To set the Retime Process value across a whole project: 1 Open the Project Settings, then click into the Master Settings panel. 2 Pick an option out of the Frame Interpolation group’s Retime Process pop-up menu. For a single clip’s Retime Process value instead: choose the clip, open the Inspector, and pick an option from the Retime Process pop-up within the Retime and Scaling group. If you go with Optical Flow, you can additionally pick an option from the Motion Estimation pop-up. The various choices you have for processing speed effects are as follows: Retime Process: Lets you set a default way of processing clips in mixed frame rate timelines and those carrying speed effects (fast forward or slow motion), handled clip‑by-clip. Its default value is “Project Settings,” so every speed-affected clip is treated alike. Three options exist — Nearest, Frame Blend, and Optical Flow — each spelled out further in the Frame Interpolation section, see Chapter 4, “System and User Preferences.”

- Nearest: The leanest on the processor and the least refined method; frames simply get dropped for fast motion or duplicated for slow motion.
- Frame Blend: Likewise light on the processor yet capable of smoother output; neighboring duplicated frames are dissolved into one another to even out slow or fast motion effects. It can give better results in cases where Optical Flow throws up unwanted artifacts.
- Optical Flow: The heaviest on the processor but the top-quality way to process speed effects. Through motion estimation, brand-new frames are synthesized from the original source frames to build slow or fast motion. Output can be remarkably smooth when a clip’s motion is linear. That said, two moving elements passing in opposite directions or erratic camera movement may trigger unwanted artifacts.

Motion estimation mode: While Optical Flow handles speed change effects or clips whose frame rate differs from the Timeline’s, the Motion Estimation pop-up lets you settle on the rendering option that looks best for a given clip. Every method carries its own artifacts, and the top-quality option isn’t invariably the right pick for a given clip. Its default value is “Project Settings,” so all speed-affected clips get handled the same. A handful of options are offered.

- “Standard Faster” and “Standard Better” match the options carried over from earlier DaVinci Resolve releases. They lean lighter on the processor and deliver good quality fit for most situations.
- “Enhanced Faster” and “Enhanced Better” ought to outperform in almost every instance where the standard options show artifacts, the trade-off being heavier computation and therefore slower runs on most systems.
- “Speed Warp Faster” and “Speed Warp Better” exist for even higher-quality slow motion built on the DaVinci Neural Engine. How this setting turns out depends on the clip’s content, but under ideal conditions it delivers better visual quality with fewer artifacts than even the Enhanced Better setting.

### Optical Flow Quality Settings Affecting Speed Effects

Found in the Master Settings panel of the Project Settings, the “Motion estimation mode” pop-up lets you weigh quality against processing speed for slow motion and frame rate retiming effects that rely on optical flow. The “Standard Faster” and “Standard Better” settings carry over from earlier DaVinci Resolve releases. They lean lighter on the processor and deliver good quality fit for most situations. By contrast, “Enhanced Faster” and “Enhanced Better” ought to outperform in nearly every instance where the standard options show artifacts, the trade-off being heavier computation and therefore slower runs on most systems.
