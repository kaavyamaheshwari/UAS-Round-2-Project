# UAS-Round-2-Project

Casualty Analysis using a Rover Guided by a UAV

UAS-DTU | Round 2 — Technical Round, Software Department

A computer-vision and path-planning project that simulates a ground rover being guided across a triage site by an aerial (UAV) segmentation map. The program identifies obstacles, traversable terrain, and casualties from the image, then computes an optimal path for the rover to visit casualties (prioritized by age and severity) before reaching the safe zone.

Problem Overview

A UAV surveys a mass-casualty site and returns a color-coded image where:

Black regions — non-traversable obstacles

Three shades of green — traversable terrain at increasing elevation levels
Orange triangle — rover's starting position
Purple triangle — final destination (safe zone)
Colored shapes (circle / star / square) — casualties, where shape encodes age group and color encodes severity

The rover must plan a route through traversable terrain, visit casualties in an order that maximizes total path score, and reach the safe zone — while the program also computes travel time and ranks multiple site images by score and time.

Features Implemented So Far

Image ingestion with OpenCV — loading and inspecting the input segmentation images
Color-based masking — isolating obstacles (black regions) and the water body (blue ellipse) using tuned BGR/HSV thresholds
Background-difference thresholding — instead of standard grayscale thresholding, the program computes each pixel's distance from the known background color. This was necessary because the bright green background has low contrast with some shape colors under plain grayscale thresholding, which caused shapes (like the orange/purple triangles) to be missed
Binary image generation & contour detection — converting the masked output into a binary image and extracting contours for every distinct shape on the map
Casualty coordinate extraction — computing and printing pixel coordinates for every detected casualty via contour centroids
Early shape classification — an in-progress approach using vertex-count approximation (cv2.approxPolyDP) to distinguish circles, squares, and stars from each other
