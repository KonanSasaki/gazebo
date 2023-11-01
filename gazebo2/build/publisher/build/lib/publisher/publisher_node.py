import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class Publisher(Node):
    
    def __init__(self):
        super().__init__("publisher_node")
        self.pub = self.create_publisher(String,'topic',10)
        self.timer = self.create_timer(1,self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World:{self.i}'
        self.pub.publish(msg)
        self.get_logger().info(f'Publish: {msg.data}')
        self.i += 1
def main():
    rclpy.init()
    node = Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
