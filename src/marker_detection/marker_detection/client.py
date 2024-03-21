#!/usr/bin/env python
import cv2
import rcply
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from client_arucotag import ArUcoDetection as msg

class aurodetectorclient(Node):
    def __init__(self):
        super.__init__('aruco_detection_client')
        self.bridge = CvBridge()
        self.image_publisher = self.create_publisher(Image,'video_image',10)
        self.aruco_subscriber = self.create_subscription(msg,'aruco_detection',self.detection_callback,10)
        self.video_file = cv2.VideoCapture('/video_file') # enter the path to the video or img file
    
    def detection_callback(self):
        for i,corners in enumerate(msg.bounding_boxes):
            print("aruco_id: ", msg.ids[i])
            print("bounding coordinate", msg.bounding_boxes[i])
    
    def convert_ros_image(self) :
        capture = cv2.VideoCapture(0)
        while True:
            ret,frame = capture.read()
            if ret : 
                ros_image = self.bridge.cv2_to_imgmsg(frame,encoding='bgr8')
                self.image_publisher.publish(ros_image)
   
    def main(args = None):
        rcply.init(args = args)
        aruco_tag = aurodetectorclient()
        aruco_tag.convert_ros_image()
        rcply.spin(aruco_tag)
        aruco_tag.destroy_node
        rcply.shutdown()
    
    if __init__ == '__main__':
        main()
    



        




