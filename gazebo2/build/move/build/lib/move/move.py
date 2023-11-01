import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class move(Node):
    def __init__(self):
        super().__init__("move")
        self.pub = self.create_publisher(Twist,"/cmd_vel")
        self.twist = Twist()
        l = input("Linear :")
        a = input("Angular :")
        self.run(l,a)
    def run(self,l,a):
        self.twist.linear.x = float(l)
        self.angular.z = float(a)
        self.pub.publisher(self.twist)
def main():
    rclpy.init()
    node = move()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
