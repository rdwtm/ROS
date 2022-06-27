#!/usr/bin/python3
import math 
import rospy
from std_msgs.msg import Float32
from cw5.srv import sinus, sinusResponse
A=1
w=1
p=1
def handle_dodaj(req):
  global A, w, p
  res = sinusResponse()
  A = req.A
  w = req.w
  p = req.p
  return res

def main():
  rospy.init_node('serwis')
  s = rospy.Service('paramerty', sinus, handle_dodaj)
  pub = rospy.Publisher('sinus', Float32, queue_size=10) 
  rate = rospy.Rate(2) # 2 razy na sekunde 

 

  while not rospy.is_shutdown(): 
	
    liczba = A*math.sin(w*rospy.get_time()+p)

    rospy.loginfo("Wysylam liczbe: " + str(liczba)) 

    wiadomosc = Float32() 

    wiadomosc.data = liczba 

    pub.publish(wiadomosc) 


    rate.sleep() 

  
if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass


