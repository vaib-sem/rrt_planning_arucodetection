#!/usr/bin/env python
import cv2
import numpy as np
import rcply 
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from client_arucotag.msg import ArUcoDetection 

class aurodetectorserver:
    def __init__(self,package_name):
        self.bridge = CvBridge()
        self.image_subscriber = rcply.Subscriber('/marker_detection/webcam'.format(package_name),Image, self.image_call)
        self.arucotags_publisher = rcply.Publisher("/marker_detection/aruco_codes".format(package_name),ArUcoDetection)
   
    def image_call(self,msg):
        cvimage =self.bridge.imgmsg_to_cv2(msg,"bgr8")
        ids,corners = self.detection_fn(cvimage)
        detection = ArUcoDetection()
        detection.bounding_box = []
        detection.id = []
        for id,corner in zip(ids,corners):
            detection.bounding_box.append(id)
            detection.id.append(corner)
        self.arucotags_publisher.publish(detection)

    def detection_fn(self,image):
        aruco_dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        parameters = cv2.aruco.DetectorParameters_create()
        corners,ids, _ = cv2.aruco.detectMarkers(image, aruco_dictionary, parameters = parameters)
        return ids,corners
    

    def main():
        rcply.init_node('aruco_detector_server')
        package_name = rcply.get_param('', 'default')
        detector = aurodetectorserver(package_name)
        rcply.spin()
    
    if __name__== '__main__':
        main()







