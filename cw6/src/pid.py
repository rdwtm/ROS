#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32
import math
from cw6.srv import Dodaj, DodajResponse
e=0.0

def handle_dodaj(req):
  ki = rospy.set_param('ki', 1)
  return 

def callback(data):
    global e
    e = data.data
    rospy.loginfo('{}'.format(e))
    
    
    
def main():
  rospy.init_node("params1")
  kp = rospy.get_param('kp', 1)
  ki = rospy.get_param('ki', 1)
  kd = rospy.get_param('kd', 1)
  pub = rospy.Publisher('u', Float32, queue_size=10)
  t0 = rospy.Time.now()
  rate = rospy.Rate(10)
  e_int= 0.0
  s = rospy.Service('reset', Dodaj, handle_dodaj)

  while not rospy.is_shutdown():
    sub = rospy.Subscriber('/y', Float32, callback)
    kp = rospy.get_param('kp', 1)
    ki = rospy.get_param('ki', 1)
    kd = rospy.get_param('kd', 1)
    e_prev=e
    e_int=e_int+e/0.1
    e_der=(e-e_prev)/0.1
    u=kp*e + ki*e_int + kd*e_der
    msg = Float32()
    msg.data = u
    pub.publish(msg)
    rate.sleep()

if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass
