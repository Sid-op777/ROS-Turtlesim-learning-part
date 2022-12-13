#!/usr/bin/env python
import rospy
def main():
	#Initialize the new node
	rospy.init_node('node_hello_ros', anonymous=True)
	#  Print info on console.
	rospy.loginfo("Hello World!")

if __name__ == '__main__':

    try:
        main()
    except rospy.ROSInterruptException:
        pass
