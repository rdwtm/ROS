#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Float32.h>
#include <cw4/Alarm.h>

using namespace std;

float temp = 0;
void liczba_cb(const std_msgs::Float32 msg) {
	temp = msg.data;

}

int main(int argc, char* argv[]) {
  ros::Duration dt(1);

  ros::init(argc, argv, "moj_subscriber");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe<std_msgs::Float32>("piec", 10, liczba_cb);
  ros::init(argc, argv, "moj_publisher");
  ros::Publisher pub = nh.advertise<cw4::Alarm>("vel", 10);
  ros::Rate rate(10);
  ros::Time t = ros::Time::now();
  while (ros::ok()){ 
    cw4::Alarm wiadomosc;
	if (temp<20 ){
		dt = ros::Time::now()-t;
		wiadomosc.typ_alarmu = "alarm dolny";
		wiadomosc.wartosc = temp;
		wiadomosc.czas = dt.toSec();
		wiadomosc.przekroczenie_dol=20-temp;
		wiadomosc.przekroczenie_gora=0;
		ROS_INFO("ALARM!!! \n %s przekroczono o %f \n czas przekroczenia: %f ", 
		wiadomosc.typ_alarmu.c_str(), wiadomosc.wartosc, wiadomosc.czas );
		pub.publish(wiadomosc);
		
      
	}
	else if (temp>80 ){
		dt = ros::Time::now()-t;
		wiadomosc.typ_alarmu = "alarm górny";
		wiadomosc.wartosc = temp;
		wiadomosc.czas = dt.toSec();
		wiadomosc.przekroczenie_dol=0;
		wiadomosc.przekroczenie_gora=temp-80;
		ROS_INFO("ALARM!!! \n %s przekroczono o %f \n czas przekroczenia: %f ", 
		wiadomosc.typ_alarmu.c_str(), wiadomosc.wartosc, wiadomosc.czas );
		pub.publish(wiadomosc);
		
      
	}
	else{
		wiadomosc.typ_alarmu = "ok";
		t = ros::Time::now();
		ROS_INFO("%s  ", 
		wiadomosc.typ_alarmu.c_str());
		wiadomosc.wartosc = temp;
		wiadomosc.czas = 0;
		wiadomosc.przekroczenie_dol=0;
		wiadomosc.przekroczenie_gora=0;
		pub.publish(wiadomosc);
	}
	
ros::spinOnce();
rate.sleep();

}
  return 0;
}
