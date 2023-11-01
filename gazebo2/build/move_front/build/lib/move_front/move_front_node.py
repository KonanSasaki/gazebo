import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Controle(Node):
    def __init__(self):
        super().__init__('move_front_node')
        self.pub = self.create_publisher(Twist,'/front/cmd_vel',10)
        self.twist = Twist()
        front_l = input("Linear :")
        front_a = input("angular :")

        self.run(front_l,front_a)

    def run(self,l,a):
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
