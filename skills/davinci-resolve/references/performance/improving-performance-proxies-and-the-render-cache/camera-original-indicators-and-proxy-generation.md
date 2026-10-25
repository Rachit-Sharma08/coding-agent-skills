# Camera original with no icon and creating proxy files with the blackmagic proxy generator

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Previous section](controlling-node-caching-and-controlling-color-output-caching.md) / [Next section](watch-folders.md)
<a id="source-creating-proxy-files-with-the-blackmagic-proxy-generator"></a> <a id="source-the-camera-original-with-no-icon"></a>

### The Camera Original with no icon

No Icon: An absent icon means proxy workflow has been switched off, and every bit of media is Camera Original.

You can pick which media you'd rather use through the Proxy Handling selector, sitting at the Viewer's upper right. Being a global setting, it shifts proxy handling for all the viewers across DaVinci Resolve.

Through the Proxy Handling Selector found in the Viewer you settle which kind of media to draw on.

### Creating Proxy Files with the Blackmagic Proxy Generator

The Blackmagic Proxy Generator stands as a separate program able to turn out proxy media on its own from master video files dropped into a watch folder. It's a small, lightweight application you can leave running in the background while bringing media in. That frees your DaVinci Resolve program up for more creative tasks while the proxies get generated.
