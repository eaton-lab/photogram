
# photogram
photogrammetry pipeline

## Pipeline Overview
0. Collect a set of images from the same sample
1. Convert images to .DNG format ***(optional)***
	- command line in bash\
	- OR Adobe DNG Converter (free)\
2. Color correction
	- Darktable (free)
	- OR Adobe Lightroom (paid)
	- OR command line in bash and darktable
3. Image clustering: identify sets of images from the same angle
	- python scripts
4. Focus stacking of images from the same angle
	- command line in Helicon Focus (paid)
	- enfuse? (free in linux)
5. Build 3d model\
	Agisoft Metashape (paid)
	- remove image background
	- align images from different angles
	- build mesh
	- build texture
	- scale models based on markers


## Detailed notes please refer to the [wiki page](https://github.com/yuemeanshappy/photogram/wiki). 
