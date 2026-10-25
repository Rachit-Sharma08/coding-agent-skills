# User interface and user interface preferences

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](timeline-preferences-and-filter-filter-to-use.md) / [Next section](fit-margin-and-display-lut-plugins.md)
<a id="source-appearance"></a> <a id="source-color-picking-area-size"></a> <a id="source-control-colors"></a> <a id="source-controls"></a> <a id="source-displayed-depth-range"></a> <a id="source-saved-view-settings"></a> <a id="source-settings-for-view"></a> <a id="source-stereo-mode"></a> <a id="source-the-user-interface-preferences"></a> <a id="source-the-video-monitoring-preferences"></a> <a id="source-the-view-preferences"></a> <a id="source-touch-scrolling-and-mouse-wheel"></a> <a id="source-user-interface"></a> <a id="source-video-monitoring"></a> <a id="source-video-output"></a> <a id="source-view"></a>

### User Interface

The User Interface preferences set how the user interface window looks and how the Inspector is shown.

### The User Interface preferences

### Appearance

Switched on, the Use Gray Background Interface checkbox shifts the background color across Fusion’s panels to a lighter, more neutral gray.

### Controls

This cluster of checkboxes governs how the controls in the Inspector are shown.

- Auto Control Open: Switched off, only the header of the selected node shows in the Inspector. You then double-click the header to bring up the parameters. Switched on, the parameters come up automatically once the node is selected.
- Auto Control Hide: Switched on, only the parameters for the currently active tool (red outline) are made visible. Otherwise every tool header stays visible and is shown according to the Auto Control Open setting.
- Auto Control Close Tools: Switched on, only the active (red outlined) tool in the Node Editor has its controls shown. Any earlier active node’s tools get closed in the Inspector. Switched off, any number of tools may be opened to show parameters at once. This setting does nothing when the Auto Control Hide checkbox is ticked.
- Auto Control Close Modifiers: Switched on, only one modifier’s parameters show for the active node. Any extra modifiers on the active node show only their header.
- Auto Control Advance: With the Auto Control Advanced checkbox ticked, the Tab key and Return/Enter key push the keyboard focus on to the next edit box within the Inspector. Switched off, Return/Enter accepts the value you entered, yet the keyboard focus holds where it is, inside that control’s edit box. You can still rely on the Tab key to push the keyboard focus along.
- Show Controls for Selected: With this option switched off, only the active tool’s parameters show in the Inspector. By default it’s switched on, showing controls for the active tool as well as every selected tool.
- Combined Color Wheel: While the Color Corrector tool shows in the Inspector, ticking this checkbox brings up one color wheel with buttons to flip between the master, shadow, midtones, and highlight channels. Otherwise four color wheels show in the Inspector.
- Gamma Aware Color Controls: This setting adjusts color correction nodes whenever a non-color managed project holds Rec. 709 images. Rec. 709 images read correctly on the computer monitor because monitors carry a built-in gamma adjustment. While working in the Rec. 709 color space with no color management, switching on Gamma Aware color strips the gamma, applies the color correction as though it were linear, and then puts the gamma back. Where Rec. 709 images are concerned, switch the Gamma Aware setting on and key in a Gamma value of 2.4. Within a color managed linear project, leave this at Off or a value of 1.0. When mixed color spaces are in play, Fusion reads the image’s metadata and sets the Aware gamma value from whatever metadata is on hand.
- Grab Distance: This slider runs from 1 to 10 and defaults to 5. It marks the active area around the mouse pointer and can be changed when you struggle to select points for adjustment in paths and spline curves. Smaller values demand a more precise selection with the mouse pointer.

### Touch Scrolling and Mouse Wheel

This cluster of settings lets you set which keyboard modifiers, if any, are needed to pan or zoom a panel while using a trackpad or middle mouse wheel.

### Video Monitoring

This setting shows up only in Fusion Studio. Control over video hardware for the Fusion Page is handled in the DaVinci Resolve preferences. The Video Monitoring preferences serve to configure Blackmagic Design capture and playback gear — DeckLink PCIe cards and UltraStudio i/O units among them.

### The Video Monitoring preferences

### Video Output

This cluster of drop-down menus lets you choose your installed video I/O device type along with the output resolution and the pixel format. None of these settings touch your rendered output; they bear only on your display hardware. The Output HDR over HDMI settings serve to send the needed metadata when high dynamic range signals go out over HMDI 2.0a so an HDR capable video display decodes them correctly. The Auto setting reads the image’s values and outputs HDR. This leaves non HDR images alone. The Always setting keeps HDR forced on at all times. That can come in handy while checking non HDR and HDR grades. Once Auto or Always is picked, the “nit” level (slang for cd/m2) is yours to set, matched to whatever peak luminance level your HDMI connected HDR display can manage.

### Stereo Mode

This cluster of settings sets up the output hardware for showing stereo 3D content.

- Mono will output a single non stereo eye.
- Auto will detect which method with which the stereo images are stacked.
- Reach for the Vstack option when your stereo images sit one above the other — left up top, right beneath.
- Reach for the Hstack option when your stereo images sit beside each other — left then right.

The Swap eyes checkbox will swap the eyes if stereo is reversed.

### View

The View preferences serve to manage settings and default controls for viewers.

### The View preferences

### Saved View Settings

The area atop the view preferences lists the saved settings you’ve created from the viewer’s contextual menu. You can lean on the Rename and Delete buttons to manage whichever entries you’ve picked in the list. To dig further into the viewer and its contextual menu, turn to Chapter 69, “Using Viewers.” within the DaVinci Resolve Reference Manual, or to Chapter 7 in the Fusion Reference Manual.

### Settings for View

Every viewer carries its own preferences. The Settings for View drop-down menu serves to pick the viewer you want to set up.

### Control Colors

The Control Colors setting lets you fix the color of the active/inactive onscreen controls.

### Color Picking Area Size

You can use these width/height controls to fix how many pixels get sampled while using the Color Picker in the viewers.

### Displayed Depth Range

The Displayed Depth Range setting steers the view normalization of the Z-Channel.
