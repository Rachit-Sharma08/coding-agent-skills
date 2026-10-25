# DaVinci control panels setup icon and DaVinci control panels setup layout

Version: DaVinci Resolve 20.3 Reference Manual. Context: DaVinci control panels setup.
[Chapter index](INDEX.md)
<a id="source-connected-control-panels-popup"></a> <a id="source-customizing-display-brightness-settings"></a> <a id="source-davinci-control-panels-setup"></a> <a id="source-davinci-control-panels-setup-1"></a> <a id="source-davinci-control-panels-setup-layout"></a> <a id="source-ethernet-connection"></a> <a id="source-firmware"></a> <a id="source-network"></a> <a id="source-reset"></a> <a id="source-settings"></a> <a id="source-the-control-panels-popup"></a> <a id="source-the-davinci-control-panels-setup-icon"></a> <a id="source-the-firmware-update-dialog-box"></a> <a id="source-the-firmware-updating"></a> <a id="source-the-settings-for-the-davinci-resolve-mini-panel"></a> <a id="source-using-davinci-control-panels-setup"></a>

### DaVinci Control Panels Setup

A number of dedicated hardware control interfaces exist to streamline the workflow on particular pages within DaVinci Resolve. Hooking up and configuring those interfaces all happens in the DaVinci Control Panels Setup app.

Numerous distinct hardware interfaces ship with DaVinci Resolve to make you more productive on specific pages. You can attach specialized keyboards, color control surfaces, and audio mixing panels to your system, and the DaVinci Control Panels Setup is the place you configure them. That DaVinci Control Panels Setup utility installs automatically as its own separate application next to DaVinci Resolve. To reach it from inside DaVinci Resolve, pick Help > DaVinci Control Panels Setup, or alternatively start the program straight from the DaVinci Resolve folder in your operating system. Before you open the application, confirm that your hardware is plugged in and switched on.

### The DaVinci Control Panels Setup icon

### DaVinci Control Panels Setup Layout

Opening DaVinci Control Panels Setup brings up an interface that displays whatever hardware device it found on your system. When several devices are present, the Left and Right Arrows along the edges of the window let you page through them. Should nothing be detected, the interface reports “No DaVinci control panels found.”

The DaVinci Control Panels Setup window with a DaVinci Editor Keyboard connected. A second attached device is indicated by the two dots underneath and the triangle off to the right.

The DaVinci Control Panels Setup with no hardware found

### Using DaVinci Control Panels Setup

Through a straightforward interface, DaVinci Control Panels Setup lets you link up your devices, refresh their firmware, and change their settings.

The DaVinci Control Panels Setup with the Fairlight Desktop Console connected

### Firmware

Each time it starts, the DaVinci Control Panels Setup application reaches out to the Blackmagic Design servers on its own to look for any firmware updates that might apply to your device. Should it locate a newer firmware build, it prompts you to either update the device or cancel and stay on the firmware version you already have. While the update runs, take care not to disconnect or power-down the device, since doing so risks corrupting the firmware. Such updates carry bug fixes and, at times, are necessary before your device can work with newer DaVinci Resolve features. Keeping your device on the newest firmware is advised unless you have a particular reason to hold back.

### The firmware update dialog box

### The firmware updating

### Ethernet Connection

When the connection runs over Ethernet, you might have to supply the device’s IP address before DaVinci Control Panels Setup can configure it. Do this by clicking the “+” icon at the interface’s lower left corner. An Add DaVinci Control Panel window then opens so you can enter the device’s IP address. Keep in mind the device has to share the same Ethernet network as the computer it links to.

Adding an Ethernet-connected device by hand is just a matter of entering its IP address.

### Settings

Reach your device’s settings by clicking the setup icon located just beneath that device. The available settings vary from one piece of hardware to another, yet they typically fall into these groupings: Setup

- Name: Assign a distinct name to your hardware device so it stands apart in the interface and in the bluetooth selection preferences.
- Software: The firmware version the device is currently running.

### Network

A device with an ethernet connection lets you configure its networking options. For anyone unfamiliar with networking, the recommendation is to keep the Protocol setting on DHCP and let the computer sort it out. Within a larger facility, though, you might instead check with your IT department about the correct manual values.

- Protocol: Decide whether the device’s IP address should be handed out automatically through DHCP or whether you’ll enter your own manual static IP address below.
- P Address: Lets you set the device’s IP address by hand.
- Subnet Mask: Lets you set the device’s Subnet Mask by hand.
- Gateway: Lets you set the device’s Gateway address by hand.

### Reset

- Factory Reset: Returns the device to its original factory defaults, which can come in handy during certain troubleshooting scenarios.

The DaVinci Control Panels Setup with the DaVinci Resolve Mini Panel connected

### The Settings for the DaVinci Resolve Mini Panel

### Customizing Display Brightness Settings

To tune the display on your Blackmagic Design control panels, head to DaVinci Resolve > Preferences > User > Control Panels.

- LCD brightness: Governs how bright the DaVinci control panel displays appear overall.
- Key backlighting: According to whichever control panel is currently selected, you get two controls letting you

set LCD Brightness and Key backlighting on the DaVinci Resolve Mini panel, or three controls for tuning the color balance of the illuminated buttons on the DaVinci Resolve Advanced control panel (red being the default).

### Connected Control Panels Popup

A Control Panels popup box sits in the lower-right corner of the DaVinci Resolve interface. Click that icon to see every control panel attached at the moment, the way each one connects, and its battery status.

### The Control Panels popup
