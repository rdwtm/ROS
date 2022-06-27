#!/usr/bin/python3

import threading
import rospy
from std_msgs.msg import Float32

class Sumator:
  def __init__(self):
    self._x1 = 0.0
    self._x2 = 0.0
    self._sub1 = rospy.Subscriber("x1", Float32, self._cb1)
    self._sub2 = rospy.Subscriber("x2", Float32, self._cb2)
    self._pub = rospy.Publisher("y", Float32, queue_size=10)
    self._thread = threading.Thread(target=self.update)
    self._thread.daemon = True
    self._thread.start()
    
  def _cb1(self, msg):
    self._x1 = msg.data
    
  def _cb2(self, msg):
    self._x2 = msg.data
  
  def update(self):
    rate = rospy.get_param("~rate", 10.0)
    loop_rate = rospy.Rate(rate)
    while not rospy.is_shutdown():
      k1 = rospy.get_param("~k1", 1.0)
      k2 = rospy.get_param("~k2", 1.0)
      y = k1 * self._x1 - k2 * self._x2
      self._pub.publish(y)
      loop_rate.sleep()
    

try:
  rospy.init_node("sumator")
  plant = Sumator()
  rospy.spin()
  
except rospy.ROSInterruptException:
  pass
