import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped
from dynamixel_sdk_custom_interfaces.msg import SetPosition

import serial

class TwistToMotor(Node):
    def __init__(self):
        super().__init__('twist_to_motor')
        self.twist_subscription = self.create_subscription(TwistStamped, 'twist_cmd', self.motor_callback, 1)
        self.twist_subscription  # prevent unused variable warning

        #self.subscription  # prevent unused variable warning
        self.servo_publisher = 	self.create_publisher(SetPosition,'set_position',1)
        #self.motor_publisher = self.create_publisher()#To be defined
        
        #self.ser = serial.Serial('/dev/ttyACM0', 115200)
        
	def motor_callback(self, msg):
		lin_vel = msg.twist.linear.x
		ang_pos = msg.twist.angular.z
		
		# map lin_vel from 0-10 to 1500-1800 then convert to int
		pwm_val = int(self.translate(lin_vel, 0, 10, 1500, 1800))
		print(str(lin_vel) + " m/s -> "+ str(pwm_val) +"us")
		
        pub_msg = SetPosition()
        pub_msg.id = 1
        pub_msg.position = translate(ang_pos, -1.7, 1.7, 0, 4095)
        self.servo_publisher.publish(pub_msg)
		
        # publish to serial
        #self.ser.write(pwm_val.to_bytes(2, byteorder='big'))
		
		
    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        """ https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another/1969274#1969274"""	
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        
        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)
        
        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)


def main(args=None):
    rclpy.init(args=args)
    node = TwistToMotor()
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()
    ser.close() # not sure if it matters where this is


if __name__ == '__main__':
    main()
