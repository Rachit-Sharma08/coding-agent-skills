# Hdmi tunneling using decklink 8k pro g2

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR setup and grading.
[Chapter index](INDEX.md) / [Previous section](dolby-vision-mastering-displays-and-icmu.md) / [Next section](dolby-vision-mapping-analysis-and-licensing.md)
<a id="source-hdmi-tunneling-using-decklink-8k-pro-g2"></a> <a id="source-hdr-setup-and-grading-part-2"></a>

### HDMI Tunneling using DeckLink 8K Pro G2


With HDMI Tunneling you can watch Dolby Vision content on a consumer display in real time. Because every display type and brand brings its own processing quirks, HDMI tunneling is meant less for reference grading and more as a way to gauge, for QC purposes, roughly what home viewers will end up seeing. You can run HDMI tunneling inside DaVinci Resolve through the more affordable Blackmagic DeckLink cards rather than Dolby’s purpose-built eCMU hardware. As things stand, the DeckLink 8K Pro G2 is the single DeckLink card that handles tunneling of this kind. Here is the setup for Dolby Vision HDMI Tunneling inside DaVinci Resolve: 1 Under Preferences > System > Video and Audio I/O, confirm that the Capture Device and Monitor Device are both pointed at the DeckLink 8K Pro. 2 Within Project Settings > Master Settings > Video Monitoring, set up these parameters: Use 4:4:4 SDI: tick its box. Video bit depth: set it to 12 bit. Enable HDR metadata: tick its box as well.

The Project settings under Video Monitoring used to switch on Dolby Vision HDMI tunneling 3 Within Project Settings > Color Management > Dolby Vision, set up these parameters: Enable Dolby Vision: tick its box. Enable Dolby Vision HDMI tunneling: tick its box too. Enable L5 metadata on HDMI: likewise tick its box.

HDR Setup and Grading — within Setup and Workflows, under HDR Viewers

The Project settings under Dolby Vision used to switch HDMI tunneling on 4 On the Color page, inside the Dolby Vision palette, verify that Enable Tone Mapping Preview is turned off (its box left unchecked). Leave that box checked and HDMI tunneling will fail to operate.

Turn off the Enable Tone Mapping Preview box within the Color page’s Dolby Vision palette For further detail on Dolby Vision HDMI tunneling, head to Dolby’s website: https://professionalsupport.dolby.com/s/article/HDMI-Tunneling?language=en_US
