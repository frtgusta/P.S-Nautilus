import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class PublicadorNode(Node):
    def __init__(self):
        super().__init__('publicador_node')
        self.publisher = self.create_publisher(Twist, 'velocidade', 10)
        self.timer = self.create_timer(1.0, self.publicar_velocidade)

    def publicar_velocidade(self):
        msg = Twist()
        # Defina os valores das componentes x, y e z conforme necessário
        msg.linear.x = 1.0
        msg.linear.y = 0.5
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.1
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PublicadorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
