# Text follower timing tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text.
[Chapter index](INDEX.md) / [Previous section](text-character-level-styling.md) / [Next section](common-controls-background-node-image-tab.md) / [Text+ TXT+](multitext-and-plasma-and-text.md)
<a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-follower-timing-tab"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-inspector-4"></a> <a id="source-text-scramble"></a> <a id="source-text-scramble-modifier-controls-tab"></a> <a id="source-text-timer"></a> <a id="source-text-timer-modifier-controls-tab"></a> <a id="source-time-code"></a> <a id="source-time-code-modifier-controls-tab"></a> <a id="source-timing-tab"></a>

### Inspector

### Follower Timing tab

### Timing Tab

With the text animated via the Modifiers tab controls, the Timing tab serves to pick the animation's direction and offset. Range The Range menu picks whether every character is affected or just a chosen span. To fix the range, you can drag-select across the characters right in the viewer. Order Which direction the characters get affected in is set by the Order menu. Keep in mind that blank spaces count as characters too. The options on hand include:

- Left to right: Across every character, the animation rolls leftward to rightward.
- Right to left: Across every character, the animation rolls rightward to leftward.
- Inside out: The animation ripples symmetrically from the center point of the

characters toward the margin.

- Outside in: The animation ripples symmetrically from the margin toward the center

point of the characters.

- Random but one by one: Picked at random, characters receive the animation, yet it only

influences one character at a time.

- Completely random: The animation is applied to randomly selected characters, influencing

multiple characters at a time.

- Manual curve: The affected characters can be specified by sliders.

Delay Type Sets which kind of delay the animation gets. The options on hand include:

- Between Each Character: The more characters your text holds, the longer the animation runs before finishing. A setting of 1 means character one kicks off the animation, character two follows 1 frame later, character three follows 1 frame after the second, and onward.
- Between First and Last Character: However many characters your text holds, the animation always wraps up within the chosen span of time.

Clear All Character Styling Each character attribute drops back to whatever value it started with.

Text Controls, Alignment, Transform, and Shading Tabs Within these tabs is where the characters' actual animation gets done. Note that merely altering a value in these tabs does nothing at all. For the effect to appear, the value has to be animated. For a full rundown of the various parameters, see the Text+ node documentation.

### Text Scramble

Text Scramble swaps the characters at random for others drawn from a set you define. You apply it by right-clicking into a Text+ node's Styled Text field and picking Text Scramble. The Text Scramble's Controls then get tuned in the Modifiers tab.

### Inspector

### Text Scramble modifier Controls tab

### Controls Tab

The Text Scramble modifier's Controls tab serves to enter text and scramble it via the Randomness control. The scrambled characters come from the Substitute Chars field down at the Inspector's foot. Randomness Sets how many characters get swapped at random. Set 0 and not a single character changes. Set 1 and every character in the text changes. Animate this thumbwheel from 0 to 1 and all the characters get swapped bit by bit. Input Text This mirrors the original text in the Text+ Styled Text field. You can enter text either here or in the Text+ node. Animate on Time Switch this on and the characters get scrambled at random on each new frame. The switch does nothing while Randomness sits at 0. Animate on Randomness Switch this on and the characters get scrambled at random on each new frame whenever the Randomness thumbwheel is animated. The switch does nothing while Randomness sits at 0.

Don't Change Spaces Switch this on and spaces stay unscrambled, so each word keeps its length even as its characters get shuffled around. Substitute Chars This field holds the characters used to scramble the text.

### Text Timer

Text Timer turns the Text+ node into a Countdown, a Timer, or a Clock. That's handy for onscreen real-time displays or for burning a frame's creation time into the picture. You apply it by right-clicking in a Text+ node's Styled Text field and picking Text Timer.

### Inspector

### Text Timer modifier Controls tab

### Controls Tab

The Text Timer modifier's Controls tab serves to set up which kind of time display this modifier turns out. Mode This menu fixes which mode the timer runs in. The choices are CountDown, Timer, and Clock. Under Clock mode, the present system time shows. Hrs, Mins, Secs (Checkboxes) Fixes which parts of the clock should appear onscreen. Hrs, Mins, Secs (Sliders) Fixes the start time for the CountDown and Timer mode. Start Sets the Counter or Timer running. Flips to Stop once the timer is going. Reset Returns the Counter and Timer to the values the sliders set.

### Time Code

Time Code acts on Text+ nodes alone. It makes the Styled text become a counter keyed to the present frame. That comes in quite handy for automating burn-ins on daily renderings. You apply it by right-clicking in a Text+ node's Styled Text field and picking Time Code.

### Inspector

### Time Code modifier Controls tab

### Controls Tab

The Time Code modifier's Controls tab serves to set up the time code display this modifier turns out. Hrs, Mins, Secs, Frms, Flds Switch these options on or off to tailor the time code display so it shows hours, minutes, seconds, frames, and fields, respectively. Switching frames on gives you nothing but a plain frame counter. Start Offset Add a positive or negative offset to Fusion's present time so it lines up with existing time codes. Frames per Second This ought to line up with your composition's FPS setting to give accurate time measurement. Drop Frame Switch this checkbox on to align the time code with footage carrying drop frames—certain NTSC formats, say.
