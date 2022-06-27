#!/usr/bin/python3

import rospy
from cw6.srv import Dodaj, DodajResponse

def handle_dodaj(req):
  ki = rospy.set_param('ki', 1)
  return res

def main():
  rospy.init_node('serwis')
  s = rospy.Service('reset_calka', Dodaj, handle_dodaj)
  rospy.spin()
  
if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass
