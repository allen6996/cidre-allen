# Face Processing Pipeline Overview

## 1. Initialization and Loading
- Load two XML files provided by OpenCV.
- These XML files contain pre-trained Haar Cascade classifiers which are used to detect faces.


## 2. Frame Processing Pipeline
- Capture frames from a camera.
- Convert each frame to grayscale because for detection colored frames is not required.
- Apply face detection on the grayscale image to identify facial regions.

## 3. ROI Filtering
- Extract the Region of Interest (ROI) corresponding to the detected face.
- Limit further processing strictly to this ROI to improve accuracy and efficiency.
- ROI filtering helps reduce false positives and unnecessary computations.

## 4. Construction of the “T” Shape
- Use ROI filtering to locate the center point of the detected eyes.
- From the eye center, define a vertical line extending downward to approximately **65%** of the face height.
- This vertical segment, combined with the horizontal eye alignment, forms a “T” shape.
- The constructed “T” region is used for focused facial feature analysis.
