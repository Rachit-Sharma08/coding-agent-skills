# Live sync and setting up live sync on blackmagic cloud storage

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cloud overview.
[Chapter index](INDEX.md) / [Previous section](storage-tab-showing-the-storage-graph-and-presentations.md)
<a id="source-blackmagic-cloud-projects-panel"></a> <a id="source-clip-upload-status-indicators"></a> <a id="source-editing-live-sync-in-davinci-resolve"></a> <a id="source-live-sync"></a> <a id="source-live-sync-1"></a> <a id="source-live-sync-in-davinci-resolve"></a> <a id="source-logging-into-blackmagic-cloud"></a> <a id="source-setting-up-a-cloud-project-in-davinci-resolve"></a> <a id="source-setting-up-live-sync-on-blackmagic-cameras"></a> <a id="source-setting-up-live-sync-on-blackmagic-cloud-storage"></a> <a id="source-setting-up-live-sync-with-the-blackmagic-camera-app-for-ios-and-android"></a> <a id="source-the-blackmagic-cloud-storage-web-interface"></a> <a id="source-uploading-clips-to-a-blackmagic-cloud-project"></a>

## Live Sync

### Live Sync

What this chapter walks through is editing by way of the Live Sync feature across DaVinici Resolve, Blackmagic Cloud and Blackmagic Cameras.

Live Sync makes it possible to edit camera files almost in real time while they’re still being recorded. The payoff is plain for time-sensitive work like news and live events, yet even scripted drama and documentaries gain from cutting on the fly to hit quick turnarounds. On its own, Live Sync begins uploading an HD H.265 proxy file even as the master clip keeps recording in the camera. That file is instantly reachable from the Media Pool in DaVinci Resolve. While recording carries on in the camera, the clip keeps lengthening in the Media Pool, giving you access to later moments from the very same clip. Each time a clip wraps, the Media Pool fills out with new proxy clips. Depending on what you need, you can either deliver your finished project right away straight from this proxy media, or, for the highestquality output, relink the footage afterward to the camera masters. Live Sync is an integrated system that needs a Blackmagic Camera, Blackmagic Cloud Storage, and DaVinci Resolve all working in concert. This chapter lays out how to get these three pieces cooperating. Cutting a live clip on the Cut page while it’s still recording; down in the lower right sits the Blackmagic Cloud Sync Manager.

### Setting up Live Sync on Blackmagic Cloud Storage

To record and edit Live Sync footage, you first need a spot that both the editor and the camera operator can reach to keep the project and camera files, and that spot is Blackmagic Cloud Storage. At a bare minimum you’ll want enough cloud storage to hold every proxy file coming off the Blackmagic Camera. Should you also intend to upload the camera originals, plan on a good deal more space, the figure depending on the codec the camera runs. To learn how to set up a Blackmagic Cloud Storage account and buy space, turn to Chapter 192, “Blackmagic Cloud Storage.”

### The Blackmagic Cloud Storage web interface

With your Blackmagic Cloud Storage space and project library in place, the moment the first clip records from a Blackmagic Camera a Camera Uploads folder springs into existence. Within it sits a Proxy subfolder (the home for all the Live Sync proxies) alongside a list of the master clips uploaded so far. Keeping this dedicated folder helps you sort and separate your incoming camera footage from whatever other media folders live in your storage. NOTE: Although the Blackmagic Cloud Storage web interface handles basic media management (deleting and organizing clips), the media management tools inside both the Blackmagic Camera and DaVinci Resolve fit the job far better. Better to treat the Cloud Storage as nothing more than a passive sync from these devices.

### Setting up Live Sync on Blackmagic Cameras

Every Blackmagic Camera model carries its own way of uploading clips to the Blackmagic Cloud; check your camera’s documentation for the particulars of that model. What follows are the steps for setting up the Blackmagic Camera app on iOS and Android.

### Setting up Live Sync with the Blackmagic Camera App for iOS and Android

Once you sign into Blackmagic Cloud within your Blackmagic Camera app, you can opt to push clips straight to a DaVinci Resolve Cloud project, or to hand-pick the clips you want uploaded from your camera’s media pool. As another route, clips can go directly into your own private Blackmagic Cloud storage without ever syncing to a Resolve Cloud project. Whether you send up proxy files alone or both proxy and original files is set under Settings > Media > Upload Clips.

### Logging into Blackmagic Cloud

To log into your Blackmagic Cloud account: 1 Navigate via Settings > Blackmagic Cloud > Log in to Blackmagic Cloud, or else tap the Blackmagic Cloud icon at the top right of the Media workspace. 2 Supply your login details, tap ‘login’, and use the touchscreen keyboard to type in your email address and password. After logging in, your Blackmagic Cloud avatar appears across the Media and Chat workspaces. Tapping that avatar lets you view your account details or sign out of your account.

### Blackmagic Cloud Projects Panel

Tapping the sidebar icon up at the top left of the Media workspace opens the Blackmagic Cloud projects panel.

While you’re signed into your Blackmagic Cloud account, the projects you’re able to upload clips to appear under the ‘Blackmagic Cloud’ section of the Viewer.

### Uploading Clips to a Blackmagic Cloud Project

Picking a Blackmagic Cloud project means you can upload proxy files, or both proxies and originals, as clips record to your camera’s media. With a project chosen in the projects panel, a clip uploads the instant you stop recording on your phone. That runs in the background while you keep recording clips, so long as the phone holds its Internet connection and remains signed into the Blackmagic Cloud account you’re using. Uploading to a Blackmagic Cloud project goes like this: 1 Tap a Blackmagic Cloud project to select it. 2 Tap the Camera icon to shut the Media Pool and head back to the HUD. 3 The chosen Blackmagic Cloud project’s name then sits above the timecode display on your phone’s HUD. The next clip you record sees your camera automatically begin uploading media to the selected cloud project. Should your phone’s internet connection drop, the cloud project name grays out and uploads halt. Your camera restarts the uploading on its own once the connection comes back. When recording is done, tap the Media icon to open the Media Pool and check your clips’ upload status. Your Blackmagic Cloud avatar stays on view in the menus and you remain logged in even after you’ve cut the phone off from the internet. This guarantees that whatever recordings sit in your project upload queue pick back up as soon as possible once the phone reconnects. The phone immediately works to reestablish its internet connection and resume any queued uploads. It also means that, when you record straight into a project, you can operate where cellular coverage is spotty without fretting about reconnecting to upload, since the process runs by itself. For instance, you might shoot clips somewhere with no Internet connection or cellular signal whatsoever, then simply connect once you’re back in range or on a wifi Internet connection and swiftly upload your proxies at that point.

Switch this slider on under the Media Settings and a proxy file begins uploading to your Blackmagic Cloud project the moment you record a clip. That clip shows up in your DaVinci Resolve Cloud project and keeps growing in the Media Pool as the recording streams in over the internet. This lets an editor start cutting the opening of a shot even while it’s still being captured in real time. The editor can keep coming back to that same clip over and over for fresh material as it lengthens. How fast the Live Sync clip refreshes hinges on the speed of your internet connection.

### Clip Upload Status Indicators

Having opted to upload clips to a Blackmagic Cloud project, you can review the upload status by picking the project out of the Blackmagic Cloud projects panel. Beside the cloud project name, the overall upload status appears — the number of clips, the completed percentage, the upload speed, and the estimated time remaining.

### Live Sync in DaVinci Resolve

### Setting up a Cloud Project in DaVinci Resolve

Ahead of any Live Sync editing session, you must build a Cloud project in DaVinci Resolve for the camera to link with. Either a brand-new or an existing Cloud project will do. For Live Sync to operate, you must switch on the “Allow Remote Camera Access” button found within the Create New Cloud Project dialog box. To learn how to set up a Cloud Project, turn to Chapter 192, “Blackmagic Cloud Storage.”

### Editing Live Sync in DaVinci Resolve

After you’ve opened your Cloud project in DaVinci Resolve, you can begin cutting live footage as it streams in. Editing works from either the Cut or the Edit page. A folder named Camera Uploads gets created in the Media Pool. That folder is your gateway to all the Live Sync media. Every thumbnail there carries icons signaling each clip’s status. A red dot in a clip’s upper-right corner flags which clip is “live” right now and actively being recorded to.

The Cut page Media Pool, where the proxy and sync state of each clip inside the Camera Uploads Folder is on view. Whichever clip bears the red dot at its upper-right corner is the one being recorded “live” right now. Working with Live Sync Clips Handling Live Sync clips on the Cut or Edit page closely mirrors handling ordinary clips, the one difference being that a Live Sync clip is forever expanding. In practical terms, that means as you scrub the footage and set In and Out points in the Viewer, the Live Sync clip stretches longer on its own as fresh material downloads. None of this asks the editor to “refresh” the clip, so there’s no occasion to step away from the Viewer. As the clip lengthens and something newly compelling unfolds, you can revise the clip with a fresh pair of In and Out points and cut it into the timeline. You’re always free to set the Live Sync clip aside and edit with other shots recorded earlier, and it’ll still be waiting when you come back… quietly growing….

The Edit page, with a Live Sync clip lengthening inside the Source Viewer. As the clip swells in size, you can revise the In and Out points in the Viewer to bring new stretches of it into the timeline. A Live Sync clip’s length is bounded only by your storage capacity, and how quickly it refreshes turns on the internet connection speed at both the Blackmagic Camera and the DaVinci Resolve workstation.
