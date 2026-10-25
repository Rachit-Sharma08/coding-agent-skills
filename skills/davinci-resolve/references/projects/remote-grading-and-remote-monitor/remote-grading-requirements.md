# Introduction to remote grading and requirements for remote grading

Version: DaVinci Resolve 20.3 Reference Manual. Context: Remote grading and remote monitor.
[Chapter index](INDEX.md) / [Next section](remote-monitor-setup-and-session-joining.md)
<a id="source-davinci-remote-monitor-studio-version-only"></a> <a id="source-introduction-to-remote-grading"></a> <a id="source-remote-grading-and-remote-monitor"></a> <a id="source-remote-grading-and-remote-monitor-1"></a> <a id="source-remote-grading-restrictions"></a> <a id="source-requirements-for-davinci-remote-monitor"></a> <a id="source-requirements-for-remote-grading"></a> <a id="source-setting-up-for-remote-grading"></a>

### Remote Grading and Remote Monitor

The pages ahead walk through configuring Remote Grading with a pair of distinct DaVinci Resolve systems sitting in separate locations and linked over the internet, so that one of them can drive the other remotely for color grading. DaVinci Remote Monitor, by contrast, lets you push a high quality video signal out of one DaVinci Resolve system toward another workstation, whether across the internet or over the same network.

### Introduction to Remote Grading

So that colorists can collaborate live with clients anywhere on the planet, DaVinci Resolve provides a remote grading capability. Two identical DaVinci Resolve systems can be kept in sync over an Internet connection, so any change the colorist makes on their workstation appears at once on the remote client’s workstation. Cue commands stay synchronized too, keeping both systems parked on the very same frame in the Timeline. Begin or halt playback on the colorist’s DaVinci Resolve and the remote client system begins or halts right along with it. For the length of a remote grading session, whatever the user types or clicks at the remote client’s DaVinci Resolve workstation is disregarded. At present the remote grading feature handles color correction alone, with no editing or conforming permitted mid-session. Both the colorist and remote DaVinci Resolve systems are required to carry matching timelines, and the clip count, the clip durations, and the system resolutions all have to line up. A summary of what a remote grading session needs and where it is limited follows below.

### Requirements for Remote Grading

- The same version of DaVinci Resolve must be installed on both systems.
- Before the remote grading session begins, the Timeline you intend to grade has to be conformed on each

grading session.

- Both the count of clips on the Timeline and how long each clip runs have to match exactly.
- Throughout grading, the remote client system keeps its active Timeline and versions continually

updated. Building, removing, or swapping the Timeline on the client’s DaVinci Resolve is forbidden. Should you do it, the remote grading session ends at once.

- No grading tweaks can be made at the remote client’s DaVinci Resolve workstation until the remote grading session is over.

NOTE: Remote grading does not require a shared project library.

### Setting Up for Remote Grading

For a remote grading session to begin, the client’s DaVinci Resolve has to reach the colorist’s system over TCP/IP. 1 On the remote client’s workstation (the machine that gets driven from afar), launch DaVinci Resolve, sign in, and bring up the project slated for remote grading. 2 From that same remote client’s workstation, choose Workspace > Remote Grading (Ctrl-G). Up comes a window bearing text fields for typing the colorist system’s IP address and port number. 3 Put the IP of the colorist’s DaVinci Resolve workstation into the IP address field. Where the colorist’s system already holds a public IP address, you can leave the port number at its default value (15000). Where the colorist’s system sits on a private network, the colorist or their network administrator ought to point the port number at one on the public IP router that routes internally to port 15000 of the colorist’s DaVinci Resolve. 4 As soon as the remote client clicks Connect, the client’s DaVinci Resolve system tries to open a connection to the remote colorist’s workstation.

5 After the connection comes up, the colorist sees a pop-up asking whether to permit an incoming Remote Grading connection. 6 Click OK to accept, shrink this dialog window down, and keep grading as usual. The Remote Grading session stays live until one of the participants opts to disconnect, or until some error forces DaVinci Resolve to shut the session down on its own.

### Remote Grading Restrictions

So that the feature can run across a low-bandwidth, possibly high-latency Internet link, certain limits apply to remote operation.

- After playback begins, the two DaVinci Resolve systems can run at differing playback speeds. Only once playback halts are the frame positions assured to be in sync.
- Input/output/display LUTs set from the Config page on the colorist’s DaVinci Resolve have no bearing on the client system; whatever LUTs are chosen on the client’s DaVinci Resolve take over instead.
- Presets set from the Config/Color pages on the colorist’s system have no bearing on the client’s system; whatever Presets are chosen on the client’s DaVinci Resolve take over instead.

### DaVinci Remote Monitor (Studio Version Only)

With DaVinci Remote Monitor, an accompanying application, you gain a low latency, high quality video signal carried over a network for the sake of monitoring, editing, and color grading. As the host works inside DaVinci Resolve, DaVinci Remote Monitor mirrors the output of that host’s Viewer live. That gives producers a way to keep an eye on a session, while editors and colorists get to operate remotely through the DaVinci Resolve interface fed by a data stream off a remote DaVinci Resolve workstation. That data stream is good enough that the signal can be routed through a Blackmagic DeckLink or UltraStudio device to a grading monitor with the same trust in the output you would place in a local connection. You can tune the stream quality to suit your specific requirements and whatever bandwidth you have. For offline editing an editor, say, might get by with just an HD h.264 8-bit 4:2:0 codec, whereas grading HDR could oblige a colorist to use the full UHD h.265 12 bit 4:4:4 RGB codec. NOTE: To keep things clear throughout this section, the central DaVinci Resolve workstation sitting in the post house or data center and pushing out the video gets called the “Resolve Host,” and whatever gear takes in that stream gets called the “Resolve Clients.” In practice, though, every one of these is simply a device running the same version of the DaVinci Resolve Studio together with the DaVinci Remote Monitoring apps.

### Requirements for DaVinci Remote Monitor

Dependably moving a high-quality video signal from one machine to the next brings a few hardware and software constraints and prerequisites that fall on the Host and Clients. For DaVinci Remote Monitor, the Resolve Host has to satisfy these hardware and software requirements:

- On the Resolve Host there must be an installed copy of the Mac, Linux, or Windows build of

DaVinci Resolve Studio.

- On Linux and Windows the Resolve Host requires that an RTX series NVIDIA GPU

with its drivers be present. AMD and Intel GPUs are currently unsupported.

- The Host must have a Blackmagic Cloud account.

For DaVinci Remote Monitor, the Resolve Client has to satisfy these hardware and software requirements:

- On the Resolve Client there must be an installed copy of the Mac, Linux, or Windows build of DaVinci Resolve

Studio. The DaVinci Remote Monitor App lands automatically in the same folder as DaVinci Resolve.

- As Client platforms, Apple iPhone and iPad devices are supported. Grab the DaVinci Remote Monitor app off the App Store (those devices do not require the Studio Version of DaVinci Resolve).
- On Linux and Windows the Resolve Client requires an RTX series NVIDIA GPU plus its drivers. AMD and Intel GPUs are currently unsupported.
- All Clients must have a Blackmagic Cloud account.
