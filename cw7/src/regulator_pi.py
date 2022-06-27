#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32

class RegulatorPI:
  def __init__(self):
    self._x = 0.0
    self._t = rospy.Time.now()
    self._sub = rospy.Subscriber("e", Float32, self._cb)
    self._pub = rospy.Subscriber("u", Float32, queue_size=10)
    
  def _cb(msg):
    kp = rospy.get_param("~kp", 1.0)
    ki = rospy.get_param("~ki", 0.0)
    t_now = rospy.Time.now()
    dt = (t_now - self._t).to_sec()
    self._t = t_now
    e = msg.data
    self._x = self._x + dt * e
    y = kp*e + ki*self._x
    self._pub.publish(y)
    

try:
  rospy.init_node("regulator_pi")
  plant = RegulatorPI()
  rospy.spin()
  
except rospy.ROSInterruptException:
  pass
