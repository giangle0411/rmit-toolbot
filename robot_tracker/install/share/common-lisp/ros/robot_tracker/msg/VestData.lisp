; Auto-generated. Do not edit!


(cl:in-package robot_tracker-msg)


;//! \htmlinclude VestData.msg.html

(cl:defclass <VestData> (roslisp-msg-protocol:ros-message)
  ((x_center
    :reader x_center
    :initarg :x_center
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (y_center
    :reader y_center
    :initarg :y_center
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (area
    :reader area
    :initarg :area
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (rotation_angle
    :reader rotation_angle
    :initarg :rotation_angle
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (cam_height
    :reader cam_height
    :initarg :cam_height
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (cam_width
    :reader cam_width
    :initarg :cam_width
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32)))
)

(cl:defclass VestData (<VestData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VestData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VestData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_tracker-msg:<VestData> is deprecated: use robot_tracker-msg:VestData instead.")))

(cl:ensure-generic-function 'x_center-val :lambda-list '(m))
(cl:defmethod x_center-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:x_center-val is deprecated.  Use robot_tracker-msg:x_center instead.")
  (x_center m))

(cl:ensure-generic-function 'y_center-val :lambda-list '(m))
(cl:defmethod y_center-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:y_center-val is deprecated.  Use robot_tracker-msg:y_center instead.")
  (y_center m))

(cl:ensure-generic-function 'area-val :lambda-list '(m))
(cl:defmethod area-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:area-val is deprecated.  Use robot_tracker-msg:area instead.")
  (area m))

(cl:ensure-generic-function 'rotation_angle-val :lambda-list '(m))
(cl:defmethod rotation_angle-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:rotation_angle-val is deprecated.  Use robot_tracker-msg:rotation_angle instead.")
  (rotation_angle m))

(cl:ensure-generic-function 'cam_height-val :lambda-list '(m))
(cl:defmethod cam_height-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:cam_height-val is deprecated.  Use robot_tracker-msg:cam_height instead.")
  (cam_height m))

(cl:ensure-generic-function 'cam_width-val :lambda-list '(m))
(cl:defmethod cam_width-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:cam_width-val is deprecated.  Use robot_tracker-msg:cam_width instead.")
  (cam_width m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VestData>) ostream)
  "Serializes a message object of type '<VestData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'x_center) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'y_center) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'area) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'rotation_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'cam_height) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'cam_width) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VestData>) istream)
  "Deserializes a message object of type '<VestData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'x_center) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'y_center) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'area) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'rotation_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'cam_height) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'cam_width) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VestData>)))
  "Returns string type for a message object of type '<VestData>"
  "robot_tracker/VestData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VestData)))
  "Returns string type for a message object of type 'VestData"
  "robot_tracker/VestData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VestData>)))
  "Returns md5sum for a message object of type '<VestData>"
  "bd3cd6db93142c19287d94b60eb73095")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VestData)))
  "Returns md5sum for a message object of type 'VestData"
  "bd3cd6db93142c19287d94b60eb73095")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VestData>)))
  "Returns full string definition for message of type '<VestData>"
  (cl:format cl:nil "std_msgs/Float32 x_center~%std_msgs/Float32 y_center~%std_msgs/Float32 area~%std_msgs/Float32 rotation_angle~%std_msgs/Float32 cam_height~%std_msgs/Float32 cam_width~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VestData)))
  "Returns full string definition for message of type 'VestData"
  (cl:format cl:nil "std_msgs/Float32 x_center~%std_msgs/Float32 y_center~%std_msgs/Float32 area~%std_msgs/Float32 rotation_angle~%std_msgs/Float32 cam_height~%std_msgs/Float32 cam_width~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VestData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'x_center))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'y_center))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'area))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'rotation_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'cam_height))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'cam_width))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VestData>))
  "Converts a ROS message object to a list"
  (cl:list 'VestData
    (cl:cons ':x_center (x_center msg))
    (cl:cons ':y_center (y_center msg))
    (cl:cons ':area (area msg))
    (cl:cons ':rotation_angle (rotation_angle msg))
    (cl:cons ':cam_height (cam_height msg))
    (cl:cons ':cam_width (cam_width msg))
))
