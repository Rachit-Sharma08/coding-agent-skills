# Chain FX and chorus

Version: DaVinci Resolve 20.3 Reference Manual. Context: Chain FX, Chorus.
[Chapter index](INDEX.md) / [Previous section](ducking-music-voice-and-audio-chain-effects.md) / [Next section](chorus-and-de-esser-and-de-hummer-and-delay.md) / [Chain FX](ducking-music-voice-and-audio-chain-effects.md)
<a id="source-add-to-plugin-chain-menu-option"></a> <a id="source-building-an-fx-chain"></a> <a id="source-chain-fx-plugin"></a> <a id="source-chorus"></a> <a id="source-master-controls"></a> <a id="source-sidechain-sc-section"></a>

### Chain FX plugin

### Master Controls

Along the upper part of the interface, the Chain FX window carries the controls below.

- Preset Menu: The spot where Chain FX settings get saved and recalled.
- To store a Chain FX combination as a preset, click the Plus button left of the Preset menu; to bring one back, open the menu and pick it.
- You can also page through the presets by clicking the left or right “arrow” ( < or >) sitting to the right of the drop-down menu.
- To make a Chain FX configuration the default, choose Set as Default from the Options menu (three dots) over in the upper-right corner, just right of the Reset button.
- For a quicker workflow, Chain FX presets copy and paste across to other instances of the plugin.

TIP: Another route to a Chain FX preset is to click the plus sign on an insert slot and then choose Chain FX.

- Compare Buttons (A and B): A quick way to pit two different Chain FX settings against one another.
- Build a Chain FX setting or load a preset while button A glows red, then click button

B and craft a different setting or load a different preset; from there, clicking between the buttons jumps you swiftly from one to the other.

- Bypass Button: Toggles the Fairlight EQ on or off.
- Reset Button: A click on the round Reset icon at the EQ’s upper-right corner reverses the last action you made in the plugin interface.

### Sidechain (SC) Section

- On Button: A click here switches on the plugin’s Sidechain section, then prompts you, by way of the Source drop-down menu, to pick an audio track or buss to serve as the input source.

To read more about Sidechaining, see Chapter 180, “Audio Effects.”

- Listen Button: Click this to monitor the incoming audio signal by itself — useful for confirming that the right audio signal is reaching the Sidechain module.
- Source: This button chooses the track or buss that the incoming audio signal comes from.

### Building an FX Chain

To assemble an effect chain inside a Chain FX instance: 1 On a Mixer Channel Strip, click a vacant Effects slot, then travel to Multi Effect > Fairlight FX > Chain FX to bring up a blank Chain FX plugin. Make sure the plugin is active. 2 In the Plugin Chain section, click the plus sign and choose an effect off the menu to add your first Fairlight FX or compatible third-party plugin. With it active, either recall a saved preset or work the controls until the settings are where you want them. 3 Do that step over and over until you have an FX chain of up to six plugins that suits you. 4 Save the resulting plugin combination, just as it stands, as a Chain FX Preset by clicking the Plus button left of the Preset menu. TIP: Clicking any plugin’s name in the effect chain pops open that plugin’s own window.

A fresh effects chain can also be started from any compatible plugin — a compressor, say — by clicking the three dots at the plugin window’s upper-right corner and choosing Add to Plugin Chain off the menu.

### Add to Plugin Chain menu option

Doing so spins up a new Chain FX instance with the plugin you began from (the compressor, here) already dropped into the first slot.

- In the mixer channel insert, the Chain FX plugin takes the compressor’s place.
- To pile on more plugins, click the plus sign in the Plugin Chain

section and choose a plugin off the menu.

### Chorus

A time-honored Chorus effect, it stacks voices or sounds against modulated copies of themselves to lend harmonic interest in assorted ways. An animated graph reflects what happens as you move this plugin’s Modulation parameters, showing you the warble or tremolo about to be layered onto the signal as you tweak.
