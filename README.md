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
---
## IMX219-83 Stereo Camera

### Hardware connection
* Connect the camera to the CSI interfaces of Jetson NX. Set the metal side of FFC into Heat-sink
* Connect an HDMI LCD to Jetson Nx
* Connect the I2C interface (only the SDA and SCL pins are required) of the Camera to I2C interface of the Jetson Nx Developer Kit (the Pin3, and Pin5)
### Software setting
* Power on Jetson Nx and open the Terminal (Ctrl+ALT+T)
* Check the video devices with command:  
  `$ ls /dev/video*`  

Check if both video0 and video1 are detected
  * Test video0  
  `$ video-viewer csi://0`
  * Test video1  
  `$ video-viewer csi://1`

Get c/c++ code to test
  `$ cd D219-9dof/03-double-camera-display
    #Build:
    $mkdir build
    $cd build
    $cmake ..
    $make

    #Run:
    $./double-camera-display`

## Tools
Convert video to picture  
* [video2pic](https://github.com/benson840722/video2pic)

YOLO txt to VOC format or json to YOLO txt  
* [yolo2voc/json2txt](https://github.com/benson840722/yolotxt2voc-json2txt)  



  
