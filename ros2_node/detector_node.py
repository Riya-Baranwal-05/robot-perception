"""
This module is a ROS node that subscribes to camera images and 
runs YOLOv8 model on each image and publishes the detection results.
"""

def detect():
    """
    This is going to read subscribed images , feed them to fine tuned model
    Publishes the class of the object , bounding box ,confidence score
    """