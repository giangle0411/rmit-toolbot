Required Hardware: 
	- PC or Laptop running Linux Ubuntu 16.04
	- Specs:
		+ At least a 2 core processor at 1.5 GHz
		+ 8GB RAM (Recommend, 4GB Minimum)
	- USB Webcam (not required if your laptop has an inbuilt camera)

Required package: 
1. ROS Kinetic OS
	1.1 sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
	1.2 sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 
	1.3 sudo apt-get update
	1.4 sudo apt-get install ros-kinetic-desktop-full
	1.5 sudo rosdep init
	1.6 rosdep update
2. ROS Perception (Should Have been added in ROS install)
	2.1 sudo apt-get install ros-kinetic-perception
3. ROS USB webcam interface (Should Have been added in ROS install)
	3.1 sudo apt-get install ros-kinetic-usb-cam
4. ROS turtle simulator (Should Have been added in ROS install)
	4.1 sudo apt-get install ros-kinetic- turtlesim
5. OpenCV
	5.1 sudo apt-get install libopencv-dev python-opencv
6. Teleoperation twist Keyboard
This package is used to test the operation of the Turtlesim.
	6.1 sudo apt-get install ros-kinetic-teleop-twist-keyboard
7. Dos2Unix
This package is only required if you intend to regularly transfer python scripts directly from a windows machine. The way linux and windows process new lines are different, this package converts the file from windows standard to linux.
	7.1 sudo apt-get install dos2unix 
8. Catkin_workspace and MiR100 simulator packages installation (modified for the project, credit for https://github.com/dfki-ric/mir_robot/tree/kinetic)
	8.1 mkdir -p ~/catkin_ws/src
	8.2 cd ~/catkin_ws/src/
	8.3 git clone -b master https://github.com/rmit-s3624420-TruongGiang-Le/capstone_toolbot.git
	8.4 source /opt/ros/kinetic/setup.bash 
	8.5 catkin_init)workspace
	8.6 cd ~/catkin_ws 
	8.7 catkin_make -DCMAKE_BUILD_TYPE=RelWithDebugInfo
	8.8 source ~/catkin_ws/devel/setup.bash


Deployment:
1. MiR-100 Simulator:
	Gazebo demo (VXLab model):
		roslaunch mir_gazebo mir_vxlab_world.launch
	To set up manual control on the simulator, un-comment “rqt_robot_steering” node in “mir_gazebo_common.launch” file.

	Model mapping and navigation on RViz:
		roslaunch mir_navigation hector_mapping.launch.xml
		roslaunch mir_navigation move_base.xml with_virtual_walls:=false
		rviz -d $(rospack find mir_navigation)/rviz/navigation.rviz

2. Robot Vest Tracking:
	Create a new folder in the home directory titled 'robot'
		mkdir -p ~/robot
	traverse to newly created folder
		cd ~/robot
	Download 'robot_tracker' branch from GitHub
		git clone -b robot_tracker https://github.com/rmit-s3624420-TruongGiang-Le/capstone_toolbot.git
	Ensure the folders ‘build’ and ‘devel’ doesn't exist, if they do perform following to delete
		rm -rf ~/robot/build ~/robot/devel
	Run make file, this will create new ‘build’ and ‘devel’ folders for your system.
		catkin_make
	Source the environment
		source ~/robot/devel/setup.bash

Getting Started With the Gazebo Simulator:
Open terminal window, set source environment:
	source ~/catkin_ws/devel/setup.bash
Run the simulator launch file:
	roslaunch mir_gazebo mir_vxlab_world.launch
	
Getting Started With Vest Detection using Turtlesim:
Open another terminal window, set source environment:
	source ~/robot/devel/setup.bash
Run launch file:
	roslaunch robot_tracker vest_detect_turtlesim.launch
	
Getting Started With Face Detection using Turtlesim:
Open another terminal window, set source environment:
	source ~/robot/devel/setup.bash
Run launch file:
	roslaunch robot_tracker face_detect_turtlesim.launch





Github url for the project: https://github.com/rmit-s3624420-TruongGiang-Le/capstone_toolbot
