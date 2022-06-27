#!/usr/bin/python3

import rospy
from cw5.srv import Dodaj

def main():
  rospy.init_node('klient')
  rospy.wait_for_service('dodaj')
  try:
    dodaj_proxy = rospy.ServiceProxy('dodaj', Dodaj)
    res = dodaj_proxy(1.0, 2.0)
    rospy.loginfo("%f" % res.suma)
  except rospy.ServiceException as e:
    print ("Blad serwisu: %s" % e)
  
if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass
