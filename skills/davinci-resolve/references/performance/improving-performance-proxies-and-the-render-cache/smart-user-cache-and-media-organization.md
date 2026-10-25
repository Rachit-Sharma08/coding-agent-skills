# The smart or user cache improves effects performance and how cached media is organized

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Previous section](optimized-media-creation.md) / [Next section](second-node-caching-and-third-the-sequence-cache.md)
<a id="source-how-cached-media-is-organized"></a> <a id="source-improving-performance-proxies-and-the-render-cache-part-2"></a> <a id="source-using-the-smart-or-user-cache-improves-effects-performance"></a>

### Using the Smart or User Cache Improves Effects Performance

One more way to reach real time performance, when the GPU Status indicator goes red because of Timeline effects, Color page grading, or processor-intensive media on the Timeline, is to engage the Render Cache via its Smart Cache or User Cache modes. What DaVinci Resolve terms “caching” other applications occasionally call “rendering.” Both words point to the off-screen creation of new media, with every effect “baked in,” which DaVinci Resolve then plays back in real time in place of the original source media that carries the processor-intensive effects. The payoff is smooth playback free of dropped-frame risk. Acting on their own, the DaVinci Resolve Smart Cache and User Cache render and cache clips — simple video clips, compound clips, Fusion clips, and nested timelines that bear processor-intensive grades and effects, or ones you flag by hand: right-click any clip on the Color page or Edit page timeline and switch on the Render Cache Clip Output option. With the Smart or User Caches active, the frames of every automatically or manually flagged clip are cached either while the Timeline plays or automatically whenever you pause work, into the “Cache files location” named in the Master Settings panel of the Project Settings.

After clips on the Timeline have been cached, they play back in real time right up until you change them, at which point the now-stale cache files for those changed clips are flushed automatically and a re-cache becomes necessary.

The caching controls as they sit in the Project Settings’ Master Settings panel To put clip caching to work on any page, do one of the following:

- Choose Playback > Render Cache > Smart so DaVinci Resolve automatically caches computationally heavy effects and timeline clips whose formats it deems too processor-intensive for real time playback.
- Choose Playback > Render Cache > User so DaVinci Resolve caches the clips and effects you pick by hand, while also automatically caching the processor-intensive effects (transitions, composites, and Fusion Effects) you designate in the Master Settings of the Project Settings.
- Choose Playback > Render Cache > Off to turn off all render caching.
- On the Color and Edit pages, press Option-R to cycle through Off, Smart, and User.

Choosing the Appropriate Cache Media Format for Your Project You’re free to set the Format of the cached media you produce using controls in the Master Settings panel of the Project Settings. Note that the format you select through the “Render Cache Format” menu governs whether out-of-bounds image data (those so-called “overshoots”), as well as Alpha Channels, survive once the clip is cached.

- Preventing Clipping: Reach for 16-bit float, ProRes 4444, ProRes 4444 XQ, or DNxHR

444 whenever you intend to grade with cached media. That holds especially for HDR grading.

- Preserving Alpha Channels: Note as well that your chosen format decides

whether Alpha channels carry through when the clips being cached contain them. At present the formats that retain Alpha channels are DNxHR 444, ProRes 4444 XQ, ProRes 4444, Uncompressed 16-bit Float, and Uncompressed 10-bit.

### How Cached Media Is Organized

In truth, DaVinci Resolve’s cache mechanism is made up of three separately managed media caches that work in tandem. The point is to keep you moving fast by making sure your timeline edits don’t force a grade to be re-cached and your grade edits don’t force the timeline to be re-cached. Caching runs at three levels: First, Fusion Output Caching Known in earlier DaVinci Resolve versions as the “Source Cache.” Switched on either by enabling the Smart Cache, by turning on Render Cache Fusion Output for a single clip, or by enabling automatic caching of clips bearing Fusion Effects in the Project Settings, it caches the slice of each source media file that shows up in the Timeline in its pre-graded state, for clips meeting the following criteria:

- Clips whose media formats DaVinci Resolve regards as processor-intensive to decode, like H.264, HEVC, and assorted raw camera formats
- Clips carrying Fusion Effects that were added on the Fusion page

In practice, this acts as a “pre-Color page” cache. Caching every processor-intensive clip in the Timeline brings you hugely better trimming and grading performance. That said, you can also flip the Fusion Output Cache on or off for individual clips, or for a batch of selected clips together. Doing so lets you flip between drawing on each clip's native source with live effects, or the cached clip held in the cache format you've picked. Where the Fusion Output Cache wins out over Optimized Media is that only clips actually used in a timeline get cached, which suits finishing workflows perfectly. Even so, the Smart and User caches do nothing to speed up work with source media in the Media Pool and Source Viewer right at the outset of an edit; handling that is the job of Optimized Media (covered in the previous section). Where Optimized media is on hand for a given clip, and “Use Optimized Media if available” sits on, then Optimized media steps in ahead of the Fusion Output Cache so long as no Speed effects or Fusion Effects ride on that particular clip.
