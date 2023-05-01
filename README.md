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
## Convert YOLO weight to onnx/trt format
* [Tensorrt_demos](https://github.com/benson840722/tensorrt_demos) 

`$ git clone git@github.com:benson840722/tensorrt_demos.git`
1. install "pycuda"
```
$ cd ${HOME}/project/tensorrt_demos/yolo
$ ./install_pycuda.sh
```
2. install onnx
`$ sudo pip3 install onnx==1.9.0`

3. Go to the "plugins/" subdirectory and build the "yolo_layer" plugin. When done, a "libyolo_layer.so" would be generated.
``` 
$ cd ${HOME}/project/tensorrt_demos/plugins
$ make
```
4. Convert the targeted model to ONNX and then to TensorRT engine.
```
$ cd ${HOME}/project/tensorrt_demos/yolo
$ pytohn3 yolo_to_onnx.py -m fake_mango_3000pics/yolov4-tiny
$ pytohn3 onnx_to_tensorrrt.py -m fake_mango_3000pics/yolov4-tiny
```
5. Test the TensorRT "yolov4-tiny" engine with the " file1.jpg" and "1.mp4".
```
#image
$ cd ${HOME}/project/tensorrt_demos
$ python3 trt_yolo.py --image file1.jpg --model fake_mano_3000pics/yolov4-tiny
#video
$ cd ${HOME}/project/tensorrt_demos
$ python3 trt_yolo.py --video 1.mp4 --model fake_mano_3000pics/yolov4-tiny
```
6. Test the TensorRT "yolov4-tiny" engine with the live stream

`$ python3 trt_yolo.py --usb 0 --model fake_mano_3000pics/yolov4-tiny`

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

* Test the IMX219-83 stereo camera
```
    $ cd D219-9dof/03-double-camera-display
    
    # Build:
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make

    #Run:
    $ ./double-camera-display
```
* If you find that the image captured is red. You can try to copy .isp file to nvidia setting:
```
  $ sudo cp camera_overrides.isp /var/nvidia/nvcam/settings/
  $ sudo chmod 664 /var/nvidia/nvcam/settings/camera_overrides.isp
  $ sudo chown root:root /var/nvidia/nvcam/settings/camera_overrides.isp
```
---
## Tools
Convert video to picture  
* [video2pic](https://github.com/benson840722/video2pic)

YOLO txt to VOC format or json to YOLO txt  
* [yolo2voc/json2txt](https://github.com/benson840722/yolotxt2voc-json2txt)  



  
