#!/usr/bin/python3

import rospy
from cw5.srv import log, logResponse

def handle_dodaj(req):
  res = logResponse()
  if (req.login=='123' and req.password=='456'):
    res.pas = True
  else:
    res.pas = False
  return res

def main():
  rospy.init_node('serwis')
  s = rospy.Service('autoryzacja', log, handle_dodaj)
  rospy.spin()
  
if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass

