#!/usr/bin/python
import rospy
import actionlib
import paczka.msg
from std_msgs.msg import Float32
skok=1
class OdliczSerwer:
	def __init__(self, name):
		self._name = name
		self._as = actionlib.SimpleActionServer(self._name, paczka.msg.OdliczAction, execute_cb=self.odlicz_cb, auto_start= False)
		self._as.start()
	def odlicz_cb(self, cel):
		rospy.loginfo("Otrzymalem cel: {}".format(cel.wartosc))
		x = 0
		feedback = paczka.msg.OdliczFeedback()
		feedback.sekwencja.append(x)
		wynik = paczka.msg.OdliczResult()
		rate = rospy.Rate(1)
		success = True
		while x < cel.wartosc:
			if self._as.is_preempt_requested():
				rospy.loginfo('Otrzymalem zadanie przedwczesnego zakonczenia')
				self._as.set_preempted()
				success = False
				break
		
			x = x + cel.skok
			rospy.loginfo("Odliczam %d", x)
			feedback.sekwencja.append(x)
			self._as.publish_feedback(feedback)
			rate.sleep()
		if success:
			wynik = feedback
			self._as.set_succeeded(wynik)
#def callback_od_liczby(wiadomosc): 
#	global skok
#	skok = wiadomosc.data 

def main():
	rospy.init_node("odlicz_serwer")
#	sub = rospy.Subscriber('liczba', Float32, callback_od_liczby) 
	odlicz_serwer = OdliczSerwer("odlicz")
	rospy.spin()
if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
