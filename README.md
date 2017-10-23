# Face ID Detector
Detect and identify the face of a specific person(owner).

## Requirements

* WebCamera
* Python 3.5
* Anaconda
* OSX
* Images of the owner and others

Please put owner's images into [data/owner](https://github.com/davidchai21/Face-ID-Detector/data/owner) and others' images [data/others](https://github.com/davidchai21/Face-ID-Detector/data/others).

## How to run the code
### First, train the images.

```
$ python3 face_train.py
```


### Second, start the detector

```
$ python3 camera_reader.py
```

## Installation
First install OpenCV, PyQt4, Anaconda, then using pip to install the requirement.txt.

## Author

[davidchai21](https://github.com/davidchai21)
