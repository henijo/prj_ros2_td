import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')
        self.subscription = self.create_subscription(
            Range,
            '/sensor/range',
            self.range_callback,
            10
        )

        self.DANGER_THRESHOLD = 0.5
        
        self.get_logger().info('[INFO] Start Control node')
    
    def range_callback(self, msg):
        distance = msg.range
        
        if distance <= self.DANGER_THRESHOLD:
            warning_msg = f"[경고] 장애물 감지: {distance:.2f}m"
            self.get_logger().warn(warning_msg)
            print(warning_msg)
        else:
            safe_msg = f"안전 거리 유지 중: {distance:.2f}m"
            self.get_logger().info(safe_msg)
            print(safe_msg)

def main(args=None):
    rclpy.init(args=args)
    control_node = ControlNode()
    
    try:
        rclpy.spin(control_node)
    except KeyboardInterrupt:
        self.get_logger().debug(f'[ERROR] Invalid Input')
        pass
    finally:
        control_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()