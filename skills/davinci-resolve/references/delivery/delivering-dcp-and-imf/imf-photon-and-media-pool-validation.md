# Photon validation of imf packages and validating in the media pool

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering dcp and imf.
[Chapter index](INDEX.md) / [Previous section](dcp-imf-supplemental-packages-and-import.md)
<a id="source-a-validation-report"></a> <a id="source-easydcp-color-management"></a> <a id="source-easydcp-output-in-the-deliver-page"></a> <a id="source-enabling-photon-validation-on-export"></a> <a id="source-importing-your-server-certificate-set"></a> <a id="source-kdm-generation-and-management"></a> <a id="source-license-x-x-x-x"></a> <a id="source-limitations-of-the-demo-version-of-easydcp"></a> <a id="source-photon-validation-of-imf-packages"></a> <a id="source-playing-your-digital-cinema-package"></a> <a id="source-publishing-your-encrypted-digital-cinema-package"></a> <a id="source-requesting-your-server-certificate-set"></a> <a id="source-server-certificate--x"></a> <a id="source-signer-certificate-x-x"></a> <a id="source-switching-between-native-dcp-and-easydcp-encoding"></a> <a id="source-using-and-licensing-easydcp"></a> <a id="source-validating-an-imf-in-the-media-pool"></a> <a id="source-validating-in-the-media-pool"></a> <a id="source-validating-on-export"></a>

### Photon Validation of IMF Packages

For IMF App2/App2e packages, Photon is Netflix's validation software. The Photon validation option appears only on Resolve Studio when JDK/JRE version 1.8 or higher is installed, available at https://github.com/Netflix/photon. NOTE: Please switch off “Use easyDCP decoder” under “Preference,” since decoding IMF packages can run into trouble without an easyDCP license.

### Validating in the Media Pool

To validate an existing IMF package with Photon, bring it into the Media Pool, then right-click it and pick “Perform Photon Validation” from the context menu.

### Validating an IMF in the Media Pool

A report dialog shows up once validation wraps.

### A validation report

### Validating on Export

You can switch Photon validation on in the File panel of the Deliver page Render Settings; picking the “IMF Netflix” preset turns this option on as well. Once enabled, DaVinci Resolve runs Photon validation after exporting the IMF package. The validation report saves to a text file inside the IMF package folder, and a report dialog appears should any error turn up.

### Enabling Photon validation on export

### Using and Licensing EasyDCP

A demo version of easyDCP ships with both DaVinci Resolve and DaVinci Resolve Studio. You'll find the demo version's operation details and restrictions later in this chapter. The fully functional easyDCP runs on licensing modules bought from http://www.easyDCP.com (info@ easyDCP.com), and every new DaVinci Resolve system (server) requires its own license plus specific certificates for DCP and KDM generation and for DCP playback.

### Requesting Your Server Certificate Set

Before your DaVinci Resolve system can produce DCPs and KDMs, you must request a particular set of configuration files known as the Server Certificate Set. Start by buying your encoding, encryption, decoding, and decryption modules from easyDCP. They'll hand you a password for your easyDCP account. Next, from the DaVinci Resolve File menu, pick easyDCP > Request Server Certificate Set. Complete the details on the request form and save it to your desktop or wherever you can find it readily. You can email this html file to info@easyDCP.com. Once the html is sent, a Server Certificate Set tailored to your installation gets generated and posted for download in your easyDCP Website User Account. The Server Certificate Set built for your DaVinci Resolve holds files keyed to your purchased modules and your particular DaVinci Resolve server hardware. The table below lists the modules along with the licenses and certificates produced, then a short rundown of each item.

DCP Encoder DCP Encoder with Encryption DCP Player DCP Player with Encryption

### License X X X X

### Server Certificate ­ X

X

### Signer Certificate X X

License: The License serves to activate the purchased modules on one specific hardware server. Server Certificate: Every DCP render (the industry calls it an “Instance”) that uses encryption or decryption carries its own server certificate. You need this certificate to receive Key Delivery Messages (KDMs), the things that unlock encrypted DCPs. Signer Certificate: A Signer Certificate signs particular files inside a DCP package and/or Key Delivery Message (KDM) to confirm which authority generated the DCP instance.

### Importing Your Server Certificate Set

Once it's been generated and downloaded onto your DaVinci Resolve server, the Server Certificate Set has to be imported into DaVinci Resolve.

To import your server certificate: 1 Pick File > easyDCP > Import License and Certificates. 2 Through the Import Server Certificate dialog, select the file, type your Certificate Set password, and click Import. 3 To confirm your easyDCP license and the Server Certificates, pick easyDCP > About easyDCP. From here on out, the controls within the Settings window, the Deliver page, and the File menu let you master and play DCPs.

### Limitations of the Demo Version of easyDCP

In the demo version, the DCP encoder bakes visible DaVinci Resolve and easyDCP logo watermarks into the rendered Digital Cinema Package (DCP) images. Since the demo version offers no encryption, these DCPs are fine for screening in a digitally equipped cinema. The demo version's DCP playback module runs 15 seconds at full quality. Past that, playback quality drops sharply. What's more, no audio renders beyond 15 seconds of playback.

### Switching Between Native DCP and EasyDCP Encoding

In the System Preferences' Configuration panel, the “Use EasyDCP Encoder” checkbox lets you decide between DaVinci Resolve's native DCP/IMF encoding and your licensed EasyDCP software. Either way, all the setup takes place inside DaVinci Resolve's Deliver page.

### EasyDCP Color Management

The Project Settings' Color Management panel offers a Timeline Colorspace dropdown menu that's active for EasyDCP encoding whether or not DaVinci Resolve Color Management is in use on the current project (the one setting covers both color management jobs). Set it to the color space your current DaVinci Resolve timeline uses. Say you're grading on a Rec. 709 monitor for television deliverables but also want a DCP — pick Rec. 709 Gamma 2.4 and DaVinci Resolve renders the DCP with the proper Rec. 709 to XYZ matrix.

### EasyDCP Output in the Deliver Page

To master a DCP on the Deliver page, walk through the steps below, which cover every easyDCP setting found in the Render Settings list. To master a DCP or IMF: 1 Put “Render timeline as” on Single clip. 2 Pick easyDCP in the Video Format dropdown. 3 In the Codec dropdown, pick whichever option suits your intended output — its type (DCP or IMF), its resolution (2K or 4K), plus its aspect ratio (native, scope, or flat). 4 Set the Composition Name. Into this field goes a standardized name identifying the DCP under encoding. Type a name in directly, or else hit the “...” button, which brings up the easyDCP Composition Name Generator window. An editable Film Title field shows up, together with several dropdown menus that let you pick various DCP attributes — content type, aspect ratio, language of audio and subtitles, and the like. As you fill in each attribute, the name being built appears at the top of the window, and clicking OK copies the finished Composition Name into the Render Settings' Composition Name field. 5 If needed, set the “Maximum DCP bit rate” you want by typing or dragging in the field (its range runs 50 to 250 Mbit/sec). When you're unsure which data rate to pick, check with the client or distributor you're delivering the DCP to. 6 You can output two DCP package types, governed by the “Use Interop packaging” checkbox:

- The standard package follows the “Interop” specifications for DCPs and is on by default. With “Use Interop packaging” on, though, your output's frame rate is capped at either 24fps or 48fps, so make certain your timeline sticks to those frame rates.
- To build DCP packages at other frame rates matching your timeline, switch “Use Interop packaging” off to make a SMPTE-standard DCP. This allows added frame rates such as 25, 30, 50, and 60 fps. That said, SMPTE-Standard-DCPs don't play on every JPEG2000-based playback system, so the Interop standard is generally the safer pick unless you know the player handles SMPTE-Standard DCPs.

7 Switch on the “Encrypt package” checkbox to encode an encrypted DCP. This tells the encoder to build a Digest holding the keys used during encryption. That Digest lets you play the resulting DCP on your system and generate KDMs so the DCP can play on other servers. NOTE: Leave the DCP unencrypted and it plays on any DCP player/decoder freely. 8 Set the Subtitles Path. With a properly formatted subtitle file on hand, click the Browse button to link it. 9 To fold an audio mix into the DCP, head to the Audio section, switch on the Render audio checkbox, and in the “Render channels of audio” dropdown menu pick the channel count matching the number of Audio Mixer output channels set on the Edit page. 10 Click the Browse button beneath the “Render to” field and choose where the resulting DCP goes. Be sure to pick a drive with room enough for the final DCP's estimated size. 11 Pick whatever options you need from the Output Options to get the quality you want. 12 Click the Add Job to Render Queue button, then click Start Render to build your DCP. A DCP gets created and placed where you chose, ready for playback or delivery.

### KDM Generation and Management

Key Delivery Messages (KDMs) are the means by which an encrypted DCP is allowed to run on a named projector, in a given theater, at an appointed time. DaVinci Resolve can create KDMs, which is handy for exporting them for select screenings, but commercial distributors may need thousands of KDMs. Happily, easyDCP lets you tap external Distribution KDM (DKDM) utilities to generate KDMs for your clients, so your DaVinci Resolve workstation isn't tied up doing it.

### Publishing Your Encrypted Digital Cinema Package

You can play your encrypted DCP on the very DaVinci Resolve system that made it, but to publish the DCP so other players can decode and play it, you have to generate a KDM to send the player. Whoever runs the other player, or players, must generate a Server Certificate for each of their players and send it to you, so that when you generate the KDM it's meant for those players alone. Pick the DCP in the Media page Library. Right-click and pick Generate KDMs. From the dropdown, choose where the Server Certificate file lives if the KDM is for a single player, or a folder for several players. Set the start and end dates over which the KDM stays valid, an output folder for the KDM, then pick Generate. Now you can send your DCP and the KDMs to the player you authorized. Its user imports the KDM, and the DCP plays between the start and end dates.

### Playing Your Digital Cinema Package

When you want to play a DCP that DaVinci Resolve produced, head to the Media page, drop it into the Media Pool, and cut it into a timeline just as you would any clip. Decoding the JPEG2000 images held inside the DCP in real time is heavy on computation. On an underpowered system you can drop the files' decoded resolution by choosing Half or Quarter Resolution Decode out of the File > easyDCP menu. A smaller, less bandwidth-hungry version of the JPEG2000 files gets decoded by tossing some levels of the wavelet stage within the decoder, which directly boosts playback performance.
