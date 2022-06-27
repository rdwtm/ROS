#!/usr/bin/python
import rospy
import actionlib
import paczka.msg
def feedback_cb(msg):
	rospy.loginfo("Feedback: {}".format(msg.feedback.sekwencja))
def main():
	rospy.init_node("odlicz_klient")
	klient = actionlib.SimpleActionClient("odlicz",
	paczka.msg.OdliczAction)
	sub=rospy.Subscriber("/odlicz/feedback", paczka.msg.OdliczActionFeedback, feedback_cb)
	klient.wait_for_server()
	cel = paczka.msg.OdliczGoal()
	cel.wartosc = 10
	cel.skok = 2

	rospy.loginfo("Wysylam cel: {}".format(cel.wartosc))
	klient.send_goal(cel)
	klient.wait_for_result()
	wynik = klient.get_result()
	print (wynik)
if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
