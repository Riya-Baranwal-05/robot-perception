"""
This module is a ROS node that subscribes to camera images and 
runs YOLOv8 model on each image and publishes the detection results.
"""
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from ultralytics import YOLO

class DetectorNode(Node):
    """
    This is going to read subscribed images , feed them to fine tuned model
    Publishes the class of the object , bounding box ,confidence score
    """
    def __init__(self):
        super().__init__('detector_node')
        self.subscription=self.create_subscription(Image,'/camera/image_raw',self.detect,10)
        self.publisher_ = self.create_publisher(String,'/detections',10)
        self.model = YOLO('best.pt')

    def detect(self,msg):
        msg = self.model(msg)
        self.publisher_.publish(msg)


    
    
