# Ward specular

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ward.
[Chapter index](INDEX.md) / [Previous section](ward-controls.md) / [Next section](ward-and-common-controls.md) / [Ward 3Wd](ward-controls.md)
<a id="source-3d-material-nodes-part-3"></a> <a id="source-specular-1"></a>

### Specular


How the surface's specular highlight looks is described by the parameters within the Specular section. Each illumination model weighs these values differently. Specular Color Specular Color sets the color of the light bouncing off a glossy surface. The more specular you make a material, the shinier it reads. Plastics and glass usually carry white specular highlights, while metallic surfaces such as gold show specular highlights tinted by the material color itself. When a specular texture map is supplied, the value entered here gets multiplied against the color values pulled from that texture. Specular Intensity Specular Intensity dictates how pronounced the specular highlight becomes. When the specular intensity texture is supplied, this value is multiplied by the texture's Alpha value. Spread U Spread U governs the specular highlight's falloff along the U-axis of the object's UV map. A smaller value yields a sharper falloff, making the material read smoother and glossier in that direction. When the Spread U texture is supplied, this value is multiplied by the texture's Alpha value. Spread V Spread V governs the specular highlight's falloff along the V-axis of the object's UV map. A smaller value yields a sharper falloff, making the material read smoother and glossier in that direction. When the Spread V texture is supplied, this value is multiplied by the texture's Alpha value.
