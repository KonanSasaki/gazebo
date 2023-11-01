import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Controle(Node):
    def __init__(self):
        super().__init__('move_node')
        self.pub = self.create_publisher(Twist,'/cmd_vel',10)
        self.twist = Twist()
        l = input("Linear :")
        a = input("angular :")

        self.ru(l,a)

    def ru(self,l,a):
        self.twist.linear.x = float(l)
        self.twist.angular.z = float(a)

        self.pub.publish(self.twist)

def main():
    rclpy.init()
    node = Controle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
