// Auto-generated. Do not edit!

// (in-package robot_tracker.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class VestData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_center = null;
      this.y_center = null;
      this.area = null;
      this.rotation_angle = null;
      this.cam_height = null;
      this.cam_width = null;
    }
    else {
      if (initObj.hasOwnProperty('x_center')) {
        this.x_center = initObj.x_center
      }
      else {
        this.x_center = new std_msgs.msg.Float32();
      }
      if (initObj.hasOwnProperty('y_center')) {
        this.y_center = initObj.y_center
      }
      else {
        this.y_center = new std_msgs.msg.Float32();
      }
      if (initObj.hasOwnProperty('area')) {
        this.area = initObj.area
      }
      else {
        this.area = new std_msgs.msg.Float32();
      }
      if (initObj.hasOwnProperty('rotation_angle')) {
        this.rotation_angle = initObj.rotation_angle
      }
      else {
        this.rotation_angle = new std_msgs.msg.Float32();
      }
      if (initObj.hasOwnProperty('cam_height')) {
        this.cam_height = initObj.cam_height
      }
      else {
        this.cam_height = new std_msgs.msg.Float32();
      }
      if (initObj.hasOwnProperty('cam_width')) {
        this.cam_width = initObj.cam_width
      }
      else {
        this.cam_width = new std_msgs.msg.Float32();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type VestData
    // Serialize message field [x_center]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.x_center, buffer, bufferOffset);
    // Serialize message field [y_center]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.y_center, buffer, bufferOffset);
    // Serialize message field [area]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.area, buffer, bufferOffset);
    // Serialize message field [rotation_angle]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.rotation_angle, buffer, bufferOffset);
    // Serialize message field [cam_height]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.cam_height, buffer, bufferOffset);
    // Serialize message field [cam_width]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.cam_width, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type VestData
    let len;
    let data = new VestData(null);
    // Deserialize message field [x_center]
    data.x_center = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    // Deserialize message field [y_center]
    data.y_center = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    // Deserialize message field [area]
    data.area = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    // Deserialize message field [rotation_angle]
    data.rotation_angle = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    // Deserialize message field [cam_height]
    data.cam_height = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    // Deserialize message field [cam_width]
    data.cam_width = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_tracker/VestData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bd3cd6db93142c19287d94b60eb73095';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Float32 x_center
    std_msgs/Float32 y_center
    std_msgs/Float32 area
    std_msgs/Float32 rotation_angle
    std_msgs/Float32 cam_height
    std_msgs/Float32 cam_width
    
    ================================================================================
    MSG: std_msgs/Float32
    float32 data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new VestData(null);
    if (msg.x_center !== undefined) {
      resolved.x_center = std_msgs.msg.Float32.Resolve(msg.x_center)
    }
    else {
      resolved.x_center = new std_msgs.msg.Float32()
    }

    if (msg.y_center !== undefined) {
      resolved.y_center = std_msgs.msg.Float32.Resolve(msg.y_center)
    }
    else {
      resolved.y_center = new std_msgs.msg.Float32()
    }

    if (msg.area !== undefined) {
      resolved.area = std_msgs.msg.Float32.Resolve(msg.area)
    }
    else {
      resolved.area = new std_msgs.msg.Float32()
    }

    if (msg.rotation_angle !== undefined) {
      resolved.rotation_angle = std_msgs.msg.Float32.Resolve(msg.rotation_angle)
    }
    else {
      resolved.rotation_angle = new std_msgs.msg.Float32()
    }

    if (msg.cam_height !== undefined) {
      resolved.cam_height = std_msgs.msg.Float32.Resolve(msg.cam_height)
    }
    else {
      resolved.cam_height = new std_msgs.msg.Float32()
    }

    if (msg.cam_width !== undefined) {
      resolved.cam_width = std_msgs.msg.Float32.Resolve(msg.cam_width)
    }
    else {
      resolved.cam_width = new std_msgs.msg.Float32()
    }

    return resolved;
    }
};

module.exports = VestData;
