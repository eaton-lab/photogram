
# photogram
photogrammetry pipeline

## Pipeline Overview
0. Collect a set of images from the same sample
1. Convert images to .DNG format *(optional)*
	- command line in bash
	- OR Adobe DNG Converter (free)
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





## 1. Conversion to DNG format
Convert all files to the widely used DNG raw photo format.
```bash
cd photogram/
for file in ./test_data/*.CR3; 
	do dnglab convert $file dng_data/${file%.CR3}.DNG;
done
````


## 2. Apply color calibration to photos
The X-rite color palette is supported in darktable. 
- https://docs.darktable.org/usermanual/3.6/module-reference/processing-modules/color-calibration/#supported-color-checker-targets
This states "If the lighting conditions are peculiar and far 
from standard illuminants, the color checker shot will be only usable as 
an ad-hoc profile for pictures taken in the same lighting conditions."

- https://pixls.us/articles/profiling-a-camera-with-darktable-chart/

```bash
darktable-cli ...
````

## 3. Cluster and organize photos 

### 3.1 by angle-rotation

- https://towardsdatascience.com/how-to-cluster-images-based-on-visual-similarity-cd6e7209fe34
- https://keras.io/examples/vision/semantic_image_clustering/
```bash
# python script using opencv
opencv?
```

### 3.2 by time intervals

Use [ExifTool](https://exiftool.org) to extract the timestamp of photos, indentify to intervals by 1) setting manual threshold, or 2) fitting them into gmm distribution.


### SOFTWARE

- [DNGLAB]
A tool for converting between raw formats, specifically here for CR3 -> DNG,
since very few tools support CR3. Tested and working. Install from .deb or source.

- [EXIFTOOL](https://exiftool.org/)
Command line perl program for editing meta data (EXIF) on various file formats. 
A dependency of ART. Can be installed within conda.

- [ART](https://garridodiaz.com/canon-cr3-support-in-linux-using-art-rawtherapee-clone/)
This is a fork of RawTherapee, a windows-only tool for converting between
different raw file formats. It is the only Linux software I have found that
can load the proprietary Canon raw format CR3. Available install from APT.

- [DARKTABLE]
A lightroom-like raw photo viewer and editor. Can be used to apply color 
corrections. Has a command line utility `darktable-cli` that may be able to 
implement batch processing. Available install from APT.


```
DNGLAB -> DARKTABLE -> 
```


0. Collect a set of images from the same sample.
1. Color correct and convert image to JPG
	- X-RITE software (free but NOT LINUX)
	- CRAW format (.CR3) is not supported by darktable.
	- 
2. Identify sets of images from the same angle.
	- Image clustering analysis
3. Focus stacking of images from the same angle.
	- Helicon Focus
	- photoshop
	- enfuse (free Linux)
4. Background removal
	- Automate... maybe gimp or OpenCV
5. Build mesh model
	- AGISOFT

