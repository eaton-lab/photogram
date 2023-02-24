
# photogram
photogrammetry pipeline

## Overview
### Preparation
- a set of images from the same sample (.CR3)
	- a camera
	- a color checker
	- a turning table
	- a light box
- softwares:
	- Adobe DNG Converter (free, optional)
	- Adobe Lightroom (paid) OR DarkTable (free)
	- Helicon Focus (paid)
	- Agisoft Metashape (paid)

### Procedures
1. photo capture
2. photo format convertion (optional) using `Adobe DNG Converter`
3. photo color calibration based on a color profile using `Adobe Lightroom` or `DarkTable`
4. photo clustering: divide photos based on rotations using `Helicon Focus` or `enfuse`
5. photo focus stacking: combine photos from the same rotation using `python scripts`
6. 3D model building using `Agisoft Metashape`
	- romove photo background
	- align photos from different rotations and angles
	- build mesh
	- build texture
	- scale models based on markers

### Final outputs
Some *Pedicularis* floral [3D models](https://sketchfab.com/yuemeanshappy)

## Detailed notes please refer to the [wiki page](https://github.com/yuemeanshappy/photogram/wiki). 

## Reference
Leménager, M., Burkiewicz, J., Schoen, D.J., Joly, S., 2022. Studying flowers in 3D using photogrammetry. New Phytol. nph.18553. [https://doi.org/10.1111/nph.18553](https://nph.onlinelibrary.wiley.com/doi/full/10.1111/nph.18553)
