# Best match tracking

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Previous section](tracking-transport-analysis-and-pattern-selection.md) / [Next section](obscured-and-out-of-frame-tracking-patterns.md)
<a id="source-best-match-tracking"></a> <a id="source-using-the-tracker-node-part-2"></a>

### Best Match Tracking


Best Match operates along similar lines to Every Frame, with one key distinction: it declines to reacquire a pattern whenever the gap between the original and the candidate grows too wide. That behavior guards against situations where momentary shifts in the picture would otherwise confuse the Tracker. To contrast the pair of Adaptive modes, picture a shadow sweeping across the tracker point — under Every Frame, the analysis may latch onto the shadow rather than the intended subject. Best Match, by contrast, recognizes that the departure from the prior frame’s pattern was too severe and refuses to capture a fresh pattern there. As you track, the Adaptive mode affects every pattern that is currently active. To limit it to a subset, switch off the remaining patterns in the list before you begin tracking.
