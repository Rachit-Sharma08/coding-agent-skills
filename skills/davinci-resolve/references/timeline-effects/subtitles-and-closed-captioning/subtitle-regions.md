# Subtitle regions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Subtitles and closed captioning.
[Chapter index](INDEX.md) / [Previous section](adding-and-deleting-subtitle-regions-overview.md) / [Next section](caption-language-and-country-codes.md)
<a id="source-subtitles-and-closed-captioning-part-2"></a> <a id="source-using-subtitle-regions"></a>

### Using Subtitle Regions


After you have built several regions, the subtitle track behaves much like a small standalone timeline stacked four layers deep. Every subtitle region carries an independent Captions list along with its own Style settings — font among them, and, above all, where the text sits on screen. So you might, for instance, reserve the default region for your ordinary subtitle layout, use Region 2 for speakers positioned to the left of the frame, and assign Region 3 to those on the right. Should two or more regions sit on top of one another within the subtitle track, every subtitle occupying that spot stays on screen together. To shift a caption from one region into another, simply drag its subtitle clip upward or downward within the subtitle track. The illustration that follows shows a pair of subtitles riding a single ordinary subtitle track. Yet because both of these lines belong to one two-shot in which the actors partly overlap, presenting the two subtitles together reads more naturally than showing them one after the other. Introduce an extra subtitle region and slide the subtitle clip along the timeline to the precise moment the actress overlaps the actor’s line, and you tie the caption’s timing more closely to what is happening on screen. On top of that, the fresh subtitle region had its text position moved over to the right of the frame, the very side where the actress speaking the line stands. Doing so makes clear which of the pair is speaking at any given moment.
