# Advanced workflows and workflow integrations

Version: DaVinci Resolve 20.3 Reference Manual. Context: Workflow integration DCTL and transport.
[Chapter index](INDEX.md) / [Next section](creating-dctl-luts-and-about-dctl.md)
<a id="source-advanced-workflows"></a> <a id="source-advanced-workflows-1"></a> <a id="source-codec-plugins-studio-version-only"></a> <a id="source-creating-workflow-integration-plugins"></a> <a id="source-davinci-resolve-renderer-plugin-for-ofx-vfx-applications-studio-version-only"></a> <a id="source-editshare"></a> <a id="source-editshares-flow-integration-plugin"></a> <a id="source-mainconcept"></a> <a id="source-overview"></a> <a id="source-sns-sharebrowser-integration-plugin"></a> <a id="source-studio-network-solutions-sns"></a> <a id="source-workflow-integration-plugins"></a> <a id="source-workflow-integrations"></a> <a id="source-workflow-integrations-1"></a> <a id="source-workflow-integrations-creating-dctl-luts-tcp-protocol-for-davinci-resolve-transport-control"></a> <a id="source-workflow-integrations-in-davinci-resolve-studio-version-only"></a>

## Overview

Topics in this file: Advanced Workflows; Workflow Integrations; Creating DCTL LUTs; and the TCP Protocol for DaVinci Resolve Transport Control.

## Advanced Workflows

### Advanced Workflows

## Workflow Integrations

### Workflow Integrations

The third party Workflow Integration plugins and Codec plugins available for DaVinci Resolve are documented in this chapter.

### DaVinci Resolve Renderer Plugin for OFX VFX Applications (Studio Version Only)

With the Open FX plugin called DaVinci Resolve Renderer, outside applications gain the ability to load and apply the color adjustments from DaVinci Resolve through exported DRX stills. In effect, your DaVinci Resolve Studio installation becomes a single sizable OFX plugin. The benefit shows up clearly during round trips with assorted VFX authoring tools, in situations where preserving the precise look you built inside DaVinci Resolve matters. A DRX still carries far richer grade data than a plain LUT would. Among the things a DRX file may hold are the full set of native color and sizing palettes plus any other elements saved in a Gallery still. As a result, whatever grade the colorist produced gets reproduced precisely within the VFX software. At the time of writing, these attributes WILL transfer via the DaVinci Resolve OFX Renderer Plugin:

- All native color palettes (Primaries, HDR, Curves etc.).
- All native sizing palettes (Input, Output, Node etc.).
- Most Resolve FX.
- Most third-party Open FX.

At the time of writing, these attributes WILL NOT transfer via the DaVinci Resolve OFX Renderer Plugin:

- Resolve and Open FX that are temporal based.
- Magic Mask.

How to configure the DaVinci Resolve OFX Renderer Plugin: 1 During the DaVinci Resolve Studio setup, pick Custom Install and tick the plugin checkbox within the program installer.

Pick Custom Install, and tick DaVinci Resolve Open FX Renderer so the plugin gets installed

2 Build a grade on a clip within the Color page, and then store a still into the Gallery. From within the Gallery, export out a .DRX file. 3 Over in the outside application, apply the DaVinci Resolve Renderer plugin at the spot that suits your composition.

Inserting the DaVinci Resolve Renderer OFX into a Nuke node tree 4 Inside the DaVinci Resolve Renderer plugin running in your application, pick the .DRX file you exported by browsing the file browser. Within the plugin, choose the .DRX file that you had exported out of DaVinci Resolve. Most Open FX-capable VFX software should handle the Color Grade Plugin fine, including Autodesk Flame as well as The Foundry’s Nuke.

In the image, the DaVinci Resolve Renderer OFX Plugin sits inside Nuke (below) and presents a balanced grade carrying green and orange Power Windows drawn from several nodes within DaVinci Resolve (above). IMPORTANT: Running the plugin requires that a DaVinci Resolve Studio license be present on whatever machine hosts the outside application.

### Workflow Integrations in DaVinci Resolve (Studio Version Only)

Through scripting languages, outside parties can build their own bespoke interface plugins for DaVinci Resolve. That capability enables DaVinci Resolve to talk directly to other software titles across a range of purposes. Several Integration plugins may run together simultaneously. Once installed, you turn plugins on inside DaVinci Resolve by heading to Workspace > Workflow Integrations and picking your plugin out of the dropdown menu.

### Creating Workflow Integration Plugins

Anyone can author their own Workflow Integration Plugin (which is an Electron app) by using the Resolve Javascript’s API together with Python or Lua scripts. To learn the details of building a Workflow Integration Plugin, head to Help > Documentation > Developer and open the Workflow Integrations folder, where the technical notes and sample code live.

### Workflow Integration Plugins

A number of Media Asset Management (MAM) systems are now reachable straight from inside DaVinci Resolve by way of the Workflow Integration Plugins.

### EditShare

A workflow integration plugin built by EditShare lets DaVinci Resolve connect straight to their FLOW media management system. Through this plugin you can add comments, run searches, and preview media inside FLOW while staying within DaVinci Resolve. On top of that, you can push up revisions, handle proxy media, and keep full metadata support intact across the whole workflow.

### EditShare’s FLOW Integration Plugin

To learn more about this plugin, and about the way FLOW operates together with DaVinci Resolve, visit: editshare.com/say-hello-to-flow-and-davinci-resolve-studio/

### Studio Network Solutions (SNS)

The ShareBrowser Integration Plugin, built by Studio Network Solutions (SNS), bridges DaVinci Resolve with their ShareBrowser media asset management software that ships alongside SNS EVO media servers. With this plugin your group can search, tag, preview, comment on, organize, and bring in media while never stepping outside the DaVinci Resolve interface. Media can be imported straight into a DaVinci Resolve project by your team, and whatever metadata you typed travels along with the media.

### SNS ShareBrowser Integration Plugin

To learn more about this plugin, and about the way SNS’s high-speed server or cloud offerings operate together with DaVinci Resolve, visit: www.studionetworksolutions.com.

### Codec Plugins (Studio Version Only)

By using Codec plugins, outside parties can add fresh codecs for encoding within the Deliver page that the core DaVinci Resolve software does not currently handle. That capability makes room for highly specialized deliverables which would otherwise demand trips through several separate programs to produce.

### MainConcept

Using the MainConcept Codec Plugin, you can output your DaVinci Resolve Studio timelines across an assortment of fresh codecs:

- AS-11 UK SD plus AS-11 UK HD, bundled with an XML metadata file, so you can produce AS-11 UK DPP compliant content.
- MainConcept’s software HEVC Main and Main 10 profiles, allowing H.265 files in 8-bit/10-bit 4:2:0/4:2:2 at up to 8K resolution.
- The MXF and MP4 formats from MainConcept, which permit encoding into the camera-native formats of Sony XAVC/XDCAM and the Panasonic P2 AVC-based cameras.

More details about the MainConcept Codec Plugin for DaVinci Resolve are available here: www.mainconcept.com/blackmagic-plugins

The MainConcept Codec Plugin for DaVinci Resolve options in the Deliver page
