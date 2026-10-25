# Playing third party digital cinema packages overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Delivering dcp and imf.
[Chapter index](INDEX.md) / [EasyDCP licensing and certificate setup](imf-photon-and-media-pool-validation.md)
<a id="source-delivering-dcp-and-imf-part-2"></a> <a id="source-playing-third-party-digital-cinema-packages"></a>

### Playing Third-Party Digital Cinema Packages

An unencrypted DCP plays back just by picking the DCP in the Media page the same way you would any ordinary clip. For an encrypted DCP that came from a third party, you have to start by handing over your Server Certificate. With that certificate in hand, they can produce KDMs that let their DCP run on your DaVinci Resolve system. Go to the File menu and choose easyDCP > Export Server Certificate, then use the dropdown to pick where the file should be saved. Pass that file along to the third party so they can generate the KDM. Once a KDM or a Digest for the encrypted DCP makes its way back to you, it has to be loaded onto your DaVinci Resolve system before anything else. The menu path for that is File > easyDCP menu > Import KDM/Digest; once you're there, simply point the import at the file you received. After that, just pick the encrypted DCP in the Media Page Library and it will play.
