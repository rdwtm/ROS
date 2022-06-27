#!/usr/bin/python3

import rospy
from cw5.srv import Dodaj, DodajResponse

def handle_dodaj(req):
  res = DodajResponse()
  res.suma = req.liczba1 + req.liczba2
  return res

def main():
  rospy.init_node('serwis')
  s = rospy.Service('dodaj', Dodaj, handle_dodaj)
  rospy.spin()
  
if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass
