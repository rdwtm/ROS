#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Float32.h>
#include <math.h>  
#define PI 3.14159265

using namespace std;

int main(int argc, char* argv[]) {
  ros::init(argc, argv, "moj_publisher");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<std_msgs::Float32>("liczba", 10);
  
  ros::Rate rate(10);
  while (ros::ok()) {
    std_msgs::Float32 wiadomosc;
    wiadomosc.data = (sin (ros::Time::now().toSec()*PI)/2);
    ROS_INFO("Wysylam sinus: %f", wiadomosc.data);
    pub.publish(wiadomosc);
    ros::spinOnce();
    rate.sleep();
  }
  
  return 0;
}
