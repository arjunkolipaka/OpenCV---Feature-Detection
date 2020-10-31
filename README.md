# OpenCV---Feature-Detection

This module gives the operational code for the 5 different feature detection algorithms that currently exist thin the OpenCV library. Specifically, all these algorithms work for the latest release of opencv-contrib-python==4.4.0

For getting your own results be sure to set your own image path in "main.py" and be sure to save your results in the right places too. Change the directories for each function in the "feature_detection.py" module. For low res images(<1000x1000) use 2000<nfeatures<10000 depending upon the amount of detail in the image in ORB. Be sure to enable the nonmaxSupression in FAST. It prevents over crowding.

!IMPORTANT:
  SURF is patented and in-order to use it you need to get the licence for it. And so it has been commented out. It is available in the NON FREE Module.
