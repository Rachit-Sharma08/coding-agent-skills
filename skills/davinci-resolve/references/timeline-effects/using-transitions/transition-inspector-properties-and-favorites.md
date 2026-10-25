# Transition properties in the inspector and favorite transitions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using transitions.
[Chapter index](INDEX.md) / [Previous section](timeline-video-audio-transition-preview.md) / [Continue Iris](iris-transition-presets-and-controls.md)
<a id="source-changing-the-standard-transition"></a> <a id="source-changing-transitions-to-fusion-compositions"></a> <a id="source-creating-transition-presets"></a> <a id="source-dissolve"></a> <a id="source-favorite-transitions"></a> <a id="source-iris"></a> <a id="source-transition-properties-in-the-inspector"></a> <a id="source-video-transitions"></a>

### Transition Properties in the Inspector

Double-click a transition in the Timeline to bring up its Transition tab inside the Inspector. Every transition exposes the editable properties below.

- Transition Type: Whichever transition is active at the moment. Swap in any other installed transition by picking one from the drop-down menu.
- Duration: How long the transition runs, displayed in both seconds and frames.
- Alignment: A drop-down for setting where the transition sits relative to the edit point it’s

attached to. The options are “Start on Edit,” “Center on Edit,” and “End on Edit.” Below those, a separate group holds extra properties unique to each transition type. Because the Cross Dissolve transition sees the most use, its properties serve as the example here.

- Style: The various Dissolve transitions (Cross Dissolve, Additive Dissolve, and the rest) surface this drop-down, which governs how the outgoing clip blends into the incoming one over the dissolve. Six options are available:

Video: A plain linear dissolve where the outgoing clip fades out while the incoming clip fades in. Film: A logarithmic dissolve that mimics the film dissolves an optical printer would produce. Additive: The outgoing and incoming clips cross fade through the Additive composite mode, which makes the transition appear to brighten at its midpoint. Subtractive: The outgoing and incoming clips cross fade through the Subtractive composite mode, which makes the transition appear to darken at its midpoint. Highlights: The outgoing and incoming clips cross fade through the Lighten composite mode, so the brightest portions of each clip stand out during the transition. Shadows: The outgoing and incoming clips cross fade through the Darken composite mode, so the darkest portions of each clip stand out during the transition.

- Start Ratio: Sets how far along the transition already is on its first frame, on a 0 to 100 percent scale. Giving the Start Ratio any value above 0 makes the transition open right away in a more fully cross-dissolved state on that very first frame.
- End Ratio: Sets how far along the transition has gotten by its last frame. Giving the End Ratio any value above 0 keeps the transition from ever resolving completely to the incoming shot on its final frame.
- Reverse: Flips the transition around. Dissolve transitions have this parameter turned off.
- Ease: A drop-down for applying nonlinear acceleration to a transition’s start, finish, or whole

span. It lends inertia to the move from the outgoing clip into the incoming clip and softens how each clip enters and exits the transition. None: The outgoing clip dissolves to the next shot at a steady, linear pace. In: The outgoing clip holds on as the transition’s opening dissolves more slowly than its close. Out: The outgoing clip drops away sooner, the transition’s opening dissolving faster than its close. In & Out: Both clips ease in slowly at the start and end of the dissolve, which leaves the dead center of the transition running faster. Custom: Hands you manual control over the fade’s parameters by way of the Transition Curves below.

- Transition Curve: Lets you place keyframes by hand to steer how the transition advances across its duration. Transitions of other types show properties tied to their own particular effect, all covered in detail in the section coming up.

### Favorite Transitions

Even though DaVinci Resolve ships with a broad assortment of transitions, most editors lean on only a handful of them day to day. It’s also common to stash customized versions of a given transition so that one specific set of transition settings can be reused again and again. To mark a transition or other effect as a favorite in the Effects Library: Hover over any transition and click the star button as it appears to favorite that transition. Click a transition’s star again to “un-favorite” it. Your favorites turn up in the Favorites area of the Effects Library bin list on the Edit page, or in the Favorites tab of the Transitions panel on the Cut page.

### Changing the Standard Transition

One project may call for a different transition to serve as the standard transition than the next. DaVinci Resolve hands you a few ways to manage that. To change the standard transition: Right-click any transition or effect and pick “Set as Standard Transition.” From then on, the standard transition carries an orange indicator just left of its name in the Effects Library.

The Effects Library open on the Edit page, where favorited transitions wear stars and the standard transition shows an orange indicator just left of its name

The Transitions tab open on the Cut page, where favorited transitions wear stars and the standard transition shows an orange indicator just left of its name To change the standard transition duration: Head into the User Preferences, open its Editing panel, and revise the “Standard transition duration” setting, with the length expressible in either Seconds or Frames. Click Save once you’re done.

### Creating Transition Presets

When you keep reaching for one transition tweaked a certain way throughout your work, you can build a Preset of it for quick recall. After it’s saved, a Preset can be favorited or named the Standard Transition to keep it close at hand. To save a transition preset for future use: 1 Drop a transition onto the Timeline, then double-click it to open it in the Inspector and dial its settings in exactly as you need them. 2 (Optional) where it matters, open the transition’s Curve Editor and choose the curve shape you want the transition to follow; that customized transition curve gets stored within the transition’s preset. 3 Right-click the transition you’re saving and pick Create Transition Preset. 4 Enter a name for the transition preset in the dialog that appears, then click OK. The transition then lands in the User section at the foot of the Toolbox Video Transitions area, ready to be applied just as you would any built-in transition. To remove a transition preset: give any preset a right-click and pick Delete Transition Preset.

### Changing Transitions to Fusion Compositions

When you want a transition more intricate than the Inspector can deliver, you can now turn any transition into a Fusion Composition right on the Edit page Timeline. The conversion from a Resolve transition into a Fusion composition goes like this: 1 Place a transition between two clips on your Timeline. 2 Right-click that transition and choose “Convert to Fusion Cross Dissolve.” 3 Right-click it once more and choose “Open in Fusion Page.” A fresh Fusion composition opens with the base Cross Dissolve nodes and tools already in place. From there, the full arsenal of Fusion page tools is yours to customize the transition.

The starting node tree produced once a transition has been converted into a Fusion cross dissolve

### Video Transitions

Listed below are the transitions DaVinci Resolve includes out of the box, each shown with the parameters the Inspector exposes for it:

### Dissolve

Within film’s visual grammar, a dissolve usually signals that time or place has moved on. It tells your audience that one scene has wrapped up while another gets under way.

- Additive Dissolve: Start Ratio tunes how far into the transition you are at its outset. End Ratio tunes how far the transition reaches by its close.
- Blur Dissolve: Horizontal/Vertical Strength controls how much blurring happens along the X and Y axes over the span of this transition. Start Ratio tunes how far into the transition you are at its outset. End Ratio tunes how far the transition reaches by its close.
- Cross Dissolve: Style lets you select the kind of cross dissolve, with choices including: Video, Film, Additive, Subtractive, Highlights, Shadows. Start Ratio tunes how far into the transition you are at its outset. End Ratio tunes how far the transition reaches by its close.
- Dip to Color Dissolve: Start Ratio tunes how far into the transition you are at its outset. End Ratio tunes how far the transition reaches by its close. Color lets you select which color the dissolve dips through at its midpoint.
- Non-Additive Dissolve: Start Ratio tunes how far into the transition you are at its outset. End Ratio tunes how far the transition reaches by its close.
- Smooth Cut: A purpose-built transition for softening short jump cuts that fall in the middle of a clip. It leans on AI powered Speed Warp processing to align matching features on both sides of a cut, automatically morphing a subject from one position into another across the length of the transition.

A Mode drop-down menu offers two settings: Faster and Better. Better is the default; it delivers excellent quality and can hold onto subject motion throughout the transition. Faster, by contrast, morphs between stills of the outgoing and incoming frames. For most real-world cases Better mode yields the stronger result, though some cuts or effects come out better under Faster. Smooth Cut shines on footage like sit-down interviews and tight head shots where background and subject movement stays minimal and the subject barely shifts position across the cut. A textbook use is paring pauses, partial repeats, filler words such as “um” or “you know,” and similar speech disfluencies from an interview clip to tighten its dialog, all while wiping out the small “jump” the cut introduces and never resorting to a B-roll cutaway. Laying a brief two- or four-frame Smooth Cut transition over the edit can render that kind of edit invisible, provided the speaker doesn’t move much during the cut. As background motion grows and the speaker shifts more, getting a usable Smooth Cut result becomes tougher. Even though any transition defaults to one second, Smooth Cut transitions fare far better kept short; 2- to 6-frame Smooth Cut transitions often do the best job of disguising jump cuts. NOTE: Starting with DaVinci Resolve 20, the transition is carried out by a new AI powered Speed Warp inside Smooth Cut. If you’d rather fall back on the earlier optical flow version, simply clear the Speed Warp box in the Transition inspector.
