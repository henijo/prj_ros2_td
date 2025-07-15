import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from std_msgs.msg import Header
import random
import time

class SensorNode(Node):
    def __init__(self):
            super().__init__('sensor_node')
            
            # default = 1(second)
            self.declare_parameter('publish_interval', 1.0)
            self.publisher_ = self.create_publisher(Range, '/sensor/range', 10)
            interval = self.get_parameter('publish_interval').get_parameter_value().double_value
            self.timer = self.create_timer(interval, self.timer_callback)
            
            # todo: log type 정리 info/warning/error
            self.get_logger().info(f'[INFO] Start Sensor node.  Interval :{interval} s')
        
    def timer_callback(self):
        msg = Range()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "sensor_frame"
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = 0.1  # radian
        msg.min_range = 0.1
        msg.max_range = 2.0
        msg.range = random.uniform(0.1, 2.0)    # 0.1m ~ 2.0m 난수 발생
        
        self.publisher_.publish(msg)

        self.get_logger().debug(f'[INFO] sensor data : {msg.range:.2f}m')

def main(args=None):
    rclpy.init(args=args)
    sensor_node = SensorNode()
    
    try:
        rclpy.spin(sensor_node)
    except KeyboardInterrupt:
        self.get_logger().debug(f'[ERROR] Invalid Input')
        pass
    finally:
        sensor_node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()