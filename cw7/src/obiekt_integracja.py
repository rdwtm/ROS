#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32

class Integracja:
  def __init__(self):
    self._x = 0.0
    self._t = rospy.Time.now()
    self._sub = rospy.Subscriber("u", Float32, self._cb)
    self._pub = rospy.Subscriber("y", Float32, queue_size=10)
    
  def _cb(msg):
    self.T = rospy.get_param("~T", 1.0)
    t_now = rospy.Time.now()
    dt = (t_now - self._t).to_sec()
    self._t = t_now
    u = msg.data
    self._x = self._x + dt * 1.0/self.T * u
    y = self._x
    self._pub.publish(y)
    

try:
  rospy.init_node("obiekt_integracja")
  plant = Integracja()
  rospy.spin()
  
except rospy.ROSInterruptException:
  pass
