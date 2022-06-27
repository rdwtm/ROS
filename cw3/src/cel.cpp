#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Float32.h>
#include <turtlesim/Pose.h>	
#include <geometry_msgs/Twist.h>
#include <cmath>


using namespace std;

float x_zolw = 0 ;
float y_zolw = 0;
float theta_zolw = 0; 
float x_cel = 0 ;
float y_cel = 0 ;

void cel_cb(const turtlesim::Pose msg) {
	x_cel = msg.x;
	y_cel = msg.y;
	
  ROS_INFO("cel to X:%f   ,Y: %f", msg.x,msg.y);
}

void poz_cb(const turtlesim::Pose msg1) {
	x_zolw = msg1.x;
	y_zolw = msg1.y;
	theta_zolw = msg1.theta;
  // ROS_INFO("pozycja zolwia X:%f  Y:%f  Z:%f", msg1.x,msg1.y,msg1.theta);
}

int main(int argc, char* argv[]) {
  ros::init(argc, argv, "moj_subscriber1");
  ros::init(argc, argv, "moj_subscriber2");
  ros::NodeHandle nh;
  ros::Subscriber sub1 = nh.subscribe<turtlesim::Pose>("cel", 10, cel_cb);
  ros::Subscriber sub2 = nh.subscribe<turtlesim::Pose>("/turtle1/pose", 10, poz_cb);
  ros::init(argc, argv, "moj_publisher");
  ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
  
  // ros::spin();
  
  
  
  ros::Rate rate(10);
  while (ros::ok()) {
	 
    geometry_msgs::Twist wiadomosc;


    float dist = sqrt(pow((x_cel-x_zolw),2)+
                      pow((y_cel-y_zolw),2));
    
    float angle = atan2(y_cel-y_zolw, x_cel-x_zolw);
     





    if (dist>0.5){
      wiadomosc.linear.x= 0.2*dist;
      wiadomosc.linear.y= 0;
      wiadomosc.linear.z= 0;
      wiadomosc.angular.x= 0;
      wiadomosc.angular.y= 0;
      wiadomosc.angular.z= 1.2*(angle-theta_zolw);

    }
  
    ROS_INFO("predkosc %f   ", wiadomosc.angular.z);
    pub.publish(wiadomosc);
    ros::spinOnce();
    rate.sleep();
  }
  return 0;
}

