# Setting up DaVinci remote monitor and DaVinci remote monitor app join screen

Version: DaVinci Resolve 20.3 Reference Manual. Context: Remote grading and remote monitor.
[Chapter index](INDEX.md) / [Previous section](remote-grading-requirements.md)
<a id="source-davinci-remote-monitor-restrictions"></a> <a id="source-davinci-remote-monitoring-using-ip-address-connections"></a> <a id="source-davinci-remote-monitoring-via-user-specified-turn-servers"></a> <a id="source-setting-up-davinci-remote-monitor"></a> <a id="source-the-davinci-remote-monitor-app-join-screen"></a>

### Setting Up DaVinci Remote Monitor

Getting a Remote Monitor session going is easy from within the DaVinci Resolve Studio interface; beyond that, the Host along with each Client has to hold Blackmagic Cloud accounts. To begin a DaVinci Remote Monitor session while acting as the Resolve Host: 1 Have the Resolve Host run the complete DaVinci Resolve Studio edition of the program. 2 Select Workspace > Remote Monitor. 3 If needed, sign into your Blackmagic Cloud account. 4 Within the Remote Monitor Window, choose the Video Codec along with the Bitrate you plan to use this session. Keep in mind your chosen Video Codec must be supported by every client device. When broad compatibility is the priority, H.264 4:2:0 8-bit serves well, yet exact color monitoring may demand some other 10- or 12-bit codec in its place. As additional clients connect, the bandwidth required rises. Running Remote Monitoring over the internet is feasible, although a wired ethernet connection yields the best results.

The DaVinci Remote Monitor Session Setup 5 Tick the “Automatically accept connections” box so that anybody holding the Session Code can join straight away. Leave that box unticked if you would rather approve every connection by hand. 6 Click the Start Session button. 7 Copy the generated Session Code out of its field, and pass it along to all the Resolve Clients by email, text message, and so on. Your Remote Monitor is now up, and a timer reports how long the current session has run. Down in the lower right of the DaVinci Resolve interface a Remote Monitor icon appears, and the top of that icon turns red once at least one Client has joined and you have gone “live.” Who is presently connected as a Client is shown in a Session Participants field.

The DaVinci Remote Monitor showing the time connected and the participants involved

To join a DaVinci Remote Monitor session while acting as a Resolve Client: 1 Have either the complete DaVinci Resolve Studio edition installed on the Resolve Client, or else the iOS app. 2 Fire up the DaVinci Remote Monitor app on whatever device you are using. It sits inside the DaVinci Resolve folder on the machine that received the software install. 3 Log into your Blackmagic Cloud account. 4 Drop the Session Code the Resolve Host gave you into the field provided. 5 Choose whichever Output Device you wish to monitor through. That could be a connected computer display, or a Blackmagic Decklink or UltraStudio device when you need color accurate monitoring. 6 Click the Join button.

### The DaVinci Remote Monitor app Join screen

Your Remote Monitor window now opens, letting you watch and listen to whatever sits in the Resolve Host’s current viewer as that person works. NOTE: To set up connections between DaVinci Resolve Studio and several clients, Remote Monitoring relies on WebRTC. That said, certain tightly locked-down network arrangements might still stop a session from starting, in which case a VPN could be needed. For top performance a wired connection is advised. To finish a DaVinci Remote Monitor session while acting as the Resolve Host: 1 Click the DaVinci Remote Monitor icon down at the lower right of the interface. 2 Press the End Session button to shut the Remote Monitor down for all users, or click the X beside any Client’s name to cut that one user’s session. To Leave a DaVinci Remote Monitor session as a Resolve Client: 1 Bring the DaVinci Remote Monitor app to the front (rather than the Remote Monitor window). 2 Press the Leave button to wrap up your session.

To switch the Codec and Bitrate partway through a DaVinci Remote Monitor session while acting as the Resolve Host: 1 Click the DaVinci Remote Monitor icon down at the lower right of the interface. 2 Up at the upper right of the Remote Monitor window, click the Settings icon. 3 Choose a fresh Codec plus a fresh Bitrate for the video stream. 4 Press the Save button. Doing so switches the streaming settings over to the new codec and bitrate you selected. Clients already attached are reconnected to the new stream automatically, with nothing required of them on their side. That gives you an easy way to adjust the video stream’s quality mid-session to work around bandwidth and hardware troubles.

### DaVinci Remote Monitoring Using IP Address Connections

There is also the option of running Remote Monitoring over plain IP Address Connections rather than logging in through Blackmagic Cloud. Taking that path, however, asks for a little technical skill in getting your network set up properly. Setting up Remote Monitoring over IP connections on the Resolve Host Walk through what follows to get your host grading computer ready for others to monitor. 1 Confirm that you have signed out of Blackmagic Cloud under Preferences > Internet Accounts. 2 Under Preferences > System > General, tick the box labeled “Use Remote Monitoring without Blackmagic Cloud.” 3 Select Workspace > Remote Monitoring. 4 Dial in the codec and bit-rate parameters however you prefer, then click Start Session. 5 Pass along to every client the IP Address or set host name belonging to the Resolve host. Setting up Remote Monitoring over IP connections on the Resolve Clients Walk through what follows to get your client computer ready for keeping watch on the host’s workstation. 1 Launch the DaVinci Remote Monitor application. 2 Within the Remote Monitor setup dialog, pick “Use Remote Monitor without Blackmagic Cloud.” 3 On the iOS or iPadOS versions of the App, head to the iOS Settings > DaVinci Monitor, then switch on “Use Remote Monitor without Blackmagic Cloud.” 4 Type the Resolve host’s server IP Address or Host Name into the Host field. 5 Click Join. To operate this mode you will need to configure firewall exceptions and the proper port forwarding yourself. Starting a session and taking connections proceeds exactly as before. For its traffic this mode relies on TCP server port 16410 plus, per client, TCP/UDP port 16411, 16412, etc.

Where the Use Remote Monitor without Blackmagic Cloud settings live across the computer and iOS versions

### DaVinci Remote Monitoring via User Specified TURN Servers

For teamwork across intricate network-security arrangements that clamp down on the WebRTC STUN protocol, you can now opt to put self-hosted or cloud-based TURN servers in charge of routing and relaying the monitoring streams. To turn this on, tick the box at Preferences > System > General > Use TURN server for Remote Monitoring. Then supply the URL of your own TURN server.

### DaVinci Remote Monitor Restrictions

A handful of limitations on the DaVinci Remote Monitor application are worth keeping in mind at the moment.

- Over an internet link, limited bandwidth can drag performance down. Should the bandwidth sink too far or drop out altogether, the Host disconnects and shows an error message.
- For now, the only pages where DaVinci Remote Monitor functions are Media, Cut, Edit, Color, and Deliver.
- Currently Audio is limited to only 2 channels.
