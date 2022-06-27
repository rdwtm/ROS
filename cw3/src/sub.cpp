#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Float32.h>

using namespace std;
float suma = 0;

void liczba_cb(const std_msgs::Float32 msg) {
	suma+=msg.data;
  ROS_INFO("Calka wynosi %f", suma);
}

int main(int argc, char* argv[]) {
  ros::init(argc, argv, "moj_subscriber");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe<std_msgs::Float32>("liczba", 10, liczba_cb);
  ros::spin();
  
  return 0;
}
