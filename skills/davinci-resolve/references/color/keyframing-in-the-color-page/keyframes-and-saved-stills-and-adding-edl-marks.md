# Keyframes and saved stills and adding edl marks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing in the color page.
[Chapter index](INDEX.md) / [Previous section](deleting-keyframes-and-copying-keyframes.md)
<a id="source-adding-edl-marks"></a> <a id="source-keyframes-and-saved-stills"></a>

### Keyframes and Saved Stills

When you grab a still off a clip whose grade includes keyframes, the keyframes are left out by default. Even so, the still and grade you store hold the parameter values defined by the closest keyframe sitting to the left of where the playhead rests. Say a clip dynamically keyframes a move from a saturation of 50 down to a saturation of 0, and the playhead happens to sit halfway between those two keyframes as you grab the still: the resulting grade and still come out at a saturation of 50. On the other hand, if you right-click in the empty area of the Gallery, pick an entry from the “Apply Grades Using” submenu, and select the right “Keyframes Aligning…” choices, then any grade stored inside a still keeps its keyframes, and those keyframes point at the source timecode, or the start frame, of the clips they came from. As a result, applying such a stored grade with keyframes to a clip makes Resolve drop the keyframes onto frames that align with the source timecode or start frame of the original clip. That makes it simple to reuse a keyframed grade on the same clip somewhere else in the Timeline, though the outcome may not be what you want if the destination is a completely unrelated clip.

### Adding EDL Marks

In the same way that clip grades stand apart from the timeline grade you can lay over the whole Timeline, clip keyframes also stand apart from timeline keyframes. Any keyframes you set on the timeline grade behave precisely the way clip keyframes do. There is, though, one additional choice available when you keyframe the timeline grade. Whenever you want to tweak a timeline grade on its own to account for shifts from clip to clip, the Add EDL Marks on Tracks command drops a Static keyframe (mark) into the Keyframe Editor at each edit point across the whole Timeline. To add EDL marks: 1 From the Node Editor’s mode drop-down menu, pick Timeline. 2 If your plan is to keyframe a grade, then build whichever grade you want laid across the entire Timeline. If instead you plan to keyframe Sizing settings, no further setup is needed. 3 In the Keyframe Editor, right-click either the Corrector track or the Sizing track, and pick Add EDL Marks on Tracks. A mark shows up at every edit point's frame throughout the Timeline. Widening the Keyframe Editor often helps when you have this many keyframes to handle. Once the EDL marks are in place, you are free to remove them later should you change your mind. To delete EDL marks:

- In the Keyframe Editor, right-click the Corrector track and pick Delete EDL Marks on Tracks.

Should you have placed keyframes of your own alongside the EDL marks, the Delete EDL Marks on Tracks command clears out only the EDL marks. The keyframes you added by hand stay untouched.
