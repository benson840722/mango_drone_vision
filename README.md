# mango_drone_vision
This project is the vision part of the mango harvesting drone, using F450 and equipped with Jetson NX. We use two lenses, one is logic C922 webcam and stereo camera IMX219-83
---
## Device
* Jetson NX
* Pixhawk 2.4.8
* F450 drone
* Logic c922 webcam
* Stereo camera IMX219-83
---
## Training your own model
* [YOLO](https://github.com/AlexeyAB/darknet)  
  `$ git clone git@github.com:AlexeyAB/darknet.git`

  Training on Jetson NX  
* [Jetson-inference](https://github.com/dusty-nv/jetson-inference)  
  `$ git clone git@github.com:dusty-nv/jetson-inference.git`    
  
  Prepare your own dataset to label  

* [label](https://github.com/heartexlabs/labelImg)  
  `$ git clone git@github.com:heartexlabs/labelImg.git`

  
