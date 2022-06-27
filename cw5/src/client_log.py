#!/usr/bin/python3

import rospy
from cw5.srv import log

def main():
  rospy.init_node('klient')
  rospy.wait_for_service('autoryzacja')
  try:
    autoryzacja_proxy = rospy.ServiceProxy('autoryzacja', log)
    x = input('login:')
    y = input('password:')
    res = autoryzacja_proxy(x, y)
    if res.pas==True:
        rospy.loginfo("zalogowano")
    else:
        rospy.loginfo("bledny login lub haslo")
  except rospy.ServiceException:
    print (" Blad serwisu: %s" % e)
  
if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass

