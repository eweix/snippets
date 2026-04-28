---
library: opencv
language: python
---

# opencv

## Simple Thresholding

In this Simple Thresholding - For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value.

<!-- cv-thresh-simple -->

```python
ret, threshimg = cv2.threshold(${1:image}, ${2:thresholdValue}, ${3:maxVal}, cv2.${4:thresholdingTechnique})
# Thresholding Technique - cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV etc
```

## Adaptive Thresholding

In Adaptive thresholding, the threshold value is calculated for smaller regions. This leads to different threshold values for different regions with respect to the change in lighting and thus gives better results.

<!-- cv-thresh-adaptive|cv-adaptive -->

```python
threshimg = cv2.adaptiveThreshold(${1:img}, ${2:maxVal}, cv2.${3:adaptiveMethod}, cv2.${4:thresholdType}, ${5:blockSize}, ${6:constant})
# Adaptive Method -  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_GAUSSIAN_C
```

## Dilation

Mainly used with binary images to remove the noise from them. It makes the object in white bigger.

<!-- cv-trans-dilate|cv-dilate -->

```python
kernel = np.ones((${1:size},${1:size}),np.uint8)
dilatedimg = cv2.dilate(${2:image},kernel,iterations = ${3:number})
```

## Erosion

Mainly used with binary images to remove the noise from them. It makes the object in white smaller.

<!-- cv-trans-erode|cv-erode -->

```python
kernel = np.ones((${1:size},${1:size}),np.uint8)
erodedimg = cv2.erode(${2:image},kernel,iterations = ${3:number})
```

## MorphologyEx

Mainly used with binary images to remove the noise from them.

<!-- cv-trans-morphex -->

```python
kernel = np.ones((${1:size},${1:size}),np.uint8)
morphedimg = cv2.morphologyEx(${2:image}, ${3:dst}, cv2.${4:TransformationType}, kernel)
#TransformationType - MORPH_BLACKHAT, MORPH_CLOSE, MORPH_CROSS, MORPH_DILATE, MORPH_ELLIPSE, MORPH_ERODE, MORPH_GRADIENT, MORPH_OPEN, MORPH_RECT, MORPH_TOPHAT, etc
```

## Simple Blurring

Used for smoothning of image.

<!-- cv-blur-simple -->

```python
blurimg = cv2.blur(${1:image},(${2:kernelsize},${2:kernelsize}))
```

## Gaussian Blurring

Gaussian kernel is used to reduce image noise and detail

<!-- cv-blur-gaussian -->

```python
gblurimg = cv2.GaussianBlur(${1:image},(${2:kernelsize},${2:kernelsize}),0)
```

## Median Blur

It is a non-linear digital filtering technique, often used to remove noise from an image or signal.

<!-- cv-blur-median -->

```python
medblurimg = cv2.medianBlur(${1:image}, ${2:kernelSize})
```

## Bilateral Blur

It is a non-linear, edge-preserving, and noise-reducing smoothing filter for images.

<!-- cv-blur-bilateral -->

```python
bilateralimg = cv2.bilateralFilter(${1:image}, ${2:Diameter},${3:sigmaColor}, ${4:sigmaSpace})
```

## Laplacian Edge Detector

Laplacian edge detector uses one kernel and calculates second order derivatives in a single pass.

<!-- cv-edge-lap -->

```python
laplacianimg = cv2.Laplacian(${1:image},cv2.CV_64F,ksize=${2:number})
laplacianimg = np.uint8(np.absolute(laplacianimg))
```

## Sobel Edge Detector

It works on the first order derivatives and calculates the first derivatives of the image separately for the X and Y axes to detect edges.

<!-- cv-edge-sob -->

```python
sobelimg = cv2.Sobel(${1:image},cv2.CV_64F,${2:x},${3:y},ksize=${4:number})
# x=1, y=0 for sobelX edge detector OR x=0, y=1 for sobelY edge detector
```

## Canny Edge Detector

Canny Edge Detection is one of the most popular edge detection algorithm.

<!-- cv-edge-canny -->

```python
cannyimg = cv2.Canny(${1:image},${2:threshold1},${3:threshold2},apertureSize = ${4:number})
```

## Contours

Contours are the line joining all the points along the boundary of an image that are having the same intensity.

<!-- cv-contours -->

```python
contours, hierarchy = cv2.findContours(${1:binaryImg}, cv2.${2:retrievalMode}, cv2.${3:approximation method})
cv2.drawContours(${4:Image}, contours, ${5:contourIdx}, (0, 255, 0), ${6:thickness})       #Colors of contours is kept green by default
#contourIdx = -1 if you want to draw all contours
```

## Shape Detection using Contours

Detects approx shape for each contour detected in the image.

<!-- cv-shapedetect -->

```python
contours, hierarchy = cv2.findContours(${1:binaryImg}, cv2.${2:retrievalMode}, cv2.${3:approximation method})
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, ${4:epsilonValue}, ${5:Boolean(True if closed polygon)})
    cv2.drawContours(${6:Image}, [approx], 0, (0,255,0), ${7:Thickness})
    x,y = approx[0][0]
    if len(approx) == 3:
        cv2.putText(${6:Image}, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, ${8:FontScale}, (0,255,0),${9:thickness})
    elif len(approx) == 4:
        cv2.putText(${6:Image}, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, ${8:FontScale}, (0,255,0),${9:thickness})
    elif len(approx) == 5:
        cv2.putText(${6:Image}, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, ${8:FontScale}, (0,255,0),${9:thickness})
    else:
        cv2.putText(${6:Image}, "Closed Polygon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, ${8:FontScale}, (0,255,0),${9:thickness})
```

## Template Matching

Identifies where the template image is present in the main Image and mark it with a green rectangle.

<!-- cv-matchtemp -->

```python
res = cv2.matchTemplate(${1:grayImage},${2:graytemplateImage},cv2.${3:Method})
# Methods - TM_CCOEFF_NORMED, TM_CCOEFF, TM_CCORR_NORMED
threshold = ${4:thresholdValue}
w,h = ${2:templateImage}.shape
location = np.where( res >= threshold)
for p in zip(*location[::-1]):
    cv2.rectangle(${5:image}, p, (p[0] + w, p[1] + h), (0,255,0), ${6:Thickness})
```

## Standard Hough Line Transform

Detects straight lines in the image even if they are bit distorted.

<!-- cv-trans-hough -->

```python
#Import only if not previously imported
import cv2
import numpy as np
lines = cv2.HoughLines(${1:BinaryImage(Canny)},${2:distanceResolution},${3:angleResolution},${4:threshold})
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(${5:image},(x1,y1),(x2,y2),(0,255,0),${6:thickness})
```

## Probabilistic Hough Line Transform

Detects straight lines of finite length in the image.

<!-- cv-trans-phough -->

```python
lines = cv2.HoughLinesP(${1:BinaryImage(Canny)},${2:distanceResolution},${3:angleResolution},${4:threshold},minLineLength=${5:integer},maxLineGap=${6:integer})
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(${7:image},(x1,y1),(x2,y2),(0,255,0),${8:thickness})
```

## Haar Cascades

Trained models which can be used for identification of various parts of image such as face, eyes etc.

<!-- cv-haarc -->

```python
cascade = cv2.CascadeClassifier('${1:Address of Downloaded Classifier}')
coor = cascade.detectMultiScale(${2:grayimage}, ${3:scaleFactor}, ${4:minNeighbors}, ${5:minSize}, ${6:maxSize})
for (x, y, w, h) in coor:
    cv2.rectangle(${7:image},(x,y),(x+w,y+h),(0,255,0),${8:thickness})
```

## Harris Corner Detector

Detects the corners in the image according the threshold setted.

<!-- cv-det-harrisc -->

```python
grayimg = cv2.cvtColor(${1:image},cv2.COLOR_BGR2GRAY)
grayfloatimg = np.float32(grayimg)
rscores = cv2.cornerHarris(grayfloatimg,${2:blockSize},${3:ksize},${4:freeParameter})
rscores = cv2.dilate(rscores,None)
threshold = 0.01*rscores.max()              # Threshold value can be changed according to the image and conditions.
${1:image}[rscores>threshold] = [0,255,0]    # Corenrs now green Color.
```

## Shi-Tomasi Corner Detector

Detects corners in the image

<!-- cv-det-goodf -->

```python
corners = cv2.goodFeaturesToTrack(${1:grayimg},${2:NoofCorners},${3:quality},${4:minDistance})
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(${5:image},(x,y),${6:radius},(0,255,0),-1)
```

## Perspective Transformation

Changes the perspective of the image or video for getting better insights about the required information

<!-- cv-trans-pers -->

```python
rows,cols,ch = ${1:image}.shape
pts1 = np.float32([[${2:},${3:}], [${4:}, ${5:}], [${6:}, ${7:}], [${8:}, ${9:}]])        #Coordinates of corners of object in original Image.
pts2 = np.float32([[${10:}, ${11:}], [${12:}, ${13:}], [${14:}, ${15:}], [${16:}, ${17:}]])
M = cv2.getPerspectiveTransform(pts1, pts2)
resultimg = cv2.warpPerspective(${1:image}, M, (cols, rows))
```

## Affine Transformation

Linear mapping method that preserves points, straight lines, and planes.

<!-- cv-trans-affn -->

```python
rows,cols,ch = ${1:image}.shape
pts1 = np.float32([[${2:},${3:}],[${4:},${5:}],[${6:},${7:}]])
pts2 = np.float32([[${8:},${9:}],[${10:},${11:}],[${12:},${13:}]])
M = cv2.getAffineTransform(pts1,pts2)
resultimg = cv2.warpAffine(${1:image},M,(cols,rows))
```

## Rotation of Image

Rotates the image by desired angle.

<!-- cv-trans-rotate -->

```python
rows,cols,_ = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),${1:angle},${2:scale})
rotated = cv2.warpAffine(${3:image},M,(cols,rows))
```
