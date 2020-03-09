;; Auto-generated. Do not edit!


(when (boundp 'robot_tracker::VestData)
  (if (not (find-package "ROBOT_TRACKER"))
    (make-package "ROBOT_TRACKER"))
  (shadow 'VestData (find-package "ROBOT_TRACKER")))
(unless (find-package "ROBOT_TRACKER::VESTDATA")
  (make-package "ROBOT_TRACKER::VESTDATA"))

(in-package "ROS")
;;//! \htmlinclude VestData.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass robot_tracker::VestData
  :super ros::object
  :slots (_x_center _y_center _area _rotation_angle _cam_height _cam_width ))

(defmethod robot_tracker::VestData
  (:init
   (&key
    ((:x_center __x_center) (instance std_msgs::Float32 :init))
    ((:y_center __y_center) (instance std_msgs::Float32 :init))
    ((:area __area) (instance std_msgs::Float32 :init))
    ((:rotation_angle __rotation_angle) (instance std_msgs::Float32 :init))
    ((:cam_height __cam_height) (instance std_msgs::Float32 :init))
    ((:cam_width __cam_width) (instance std_msgs::Float32 :init))
    )
   (send-super :init)
   (setq _x_center __x_center)
   (setq _y_center __y_center)
   (setq _area __area)
   (setq _rotation_angle __rotation_angle)
   (setq _cam_height __cam_height)
   (setq _cam_width __cam_width)
   self)
  (:x_center
   (&rest __x_center)
   (if (keywordp (car __x_center))
       (send* _x_center __x_center)
     (progn
       (if __x_center (setq _x_center (car __x_center)))
       _x_center)))
  (:y_center
   (&rest __y_center)
   (if (keywordp (car __y_center))
       (send* _y_center __y_center)
     (progn
       (if __y_center (setq _y_center (car __y_center)))
       _y_center)))
  (:area
   (&rest __area)
   (if (keywordp (car __area))
       (send* _area __area)
     (progn
       (if __area (setq _area (car __area)))
       _area)))
  (:rotation_angle
   (&rest __rotation_angle)
   (if (keywordp (car __rotation_angle))
       (send* _rotation_angle __rotation_angle)
     (progn
       (if __rotation_angle (setq _rotation_angle (car __rotation_angle)))
       _rotation_angle)))
  (:cam_height
   (&rest __cam_height)
   (if (keywordp (car __cam_height))
       (send* _cam_height __cam_height)
     (progn
       (if __cam_height (setq _cam_height (car __cam_height)))
       _cam_height)))
  (:cam_width
   (&rest __cam_width)
   (if (keywordp (car __cam_width))
       (send* _cam_width __cam_width)
     (progn
       (if __cam_width (setq _cam_width (car __cam_width)))
       _cam_width)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Float32 _x_center
    (send _x_center :serialization-length)
    ;; std_msgs/Float32 _y_center
    (send _y_center :serialization-length)
    ;; std_msgs/Float32 _area
    (send _area :serialization-length)
    ;; std_msgs/Float32 _rotation_angle
    (send _rotation_angle :serialization-length)
    ;; std_msgs/Float32 _cam_height
    (send _cam_height :serialization-length)
    ;; std_msgs/Float32 _cam_width
    (send _cam_width :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Float32 _x_center
       (send _x_center :serialize s)
     ;; std_msgs/Float32 _y_center
       (send _y_center :serialize s)
     ;; std_msgs/Float32 _area
       (send _area :serialize s)
     ;; std_msgs/Float32 _rotation_angle
       (send _rotation_angle :serialize s)
     ;; std_msgs/Float32 _cam_height
       (send _cam_height :serialize s)
     ;; std_msgs/Float32 _cam_width
       (send _cam_width :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Float32 _x_center
     (send _x_center :deserialize buf ptr-) (incf ptr- (send _x_center :serialization-length))
   ;; std_msgs/Float32 _y_center
     (send _y_center :deserialize buf ptr-) (incf ptr- (send _y_center :serialization-length))
   ;; std_msgs/Float32 _area
     (send _area :deserialize buf ptr-) (incf ptr- (send _area :serialization-length))
   ;; std_msgs/Float32 _rotation_angle
     (send _rotation_angle :deserialize buf ptr-) (incf ptr- (send _rotation_angle :serialization-length))
   ;; std_msgs/Float32 _cam_height
     (send _cam_height :deserialize buf ptr-) (incf ptr- (send _cam_height :serialization-length))
   ;; std_msgs/Float32 _cam_width
     (send _cam_width :deserialize buf ptr-) (incf ptr- (send _cam_width :serialization-length))
   ;;
   self)
  )

(setf (get robot_tracker::VestData :md5sum-) "bd3cd6db93142c19287d94b60eb73095")
(setf (get robot_tracker::VestData :datatype-) "robot_tracker/VestData")
(setf (get robot_tracker::VestData :definition-)
      "std_msgs/Float32 x_center
std_msgs/Float32 y_center
std_msgs/Float32 area
std_msgs/Float32 rotation_angle
std_msgs/Float32 cam_height
std_msgs/Float32 cam_width

================================================================================
MSG: std_msgs/Float32
float32 data
")



(provide :robot_tracker/VestData "bd3cd6db93142c19287d94b60eb73095")


