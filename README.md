# Mask RCNN for sofa recognition

## Installation

1. Clone repo
2. `cd` to project directory
3. `python -m venv venv`
4. Activate venv
5. `git submodule init`
6. `git submodule update`
7. Follow "installation" section of [this](https://github.com/matterport/Mask_RCNN) repo (it seems like COCO weights can be auto-downloaded).
8. Copy mrcnn folder from `matterport/` to root directory

Most code created following [this](https://github.com/matterport/Mask_RCNN/blob/master/samples/shapes/train_shapes.ipynb) notebook