import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class CalculadorNode(Node):
    def __init__(self):
        super().__init__('calculador_node')
        self.publisher = self.create_publisher(Float64, 'modulo_velocidade', 10)
        self.subscription = self.create_subscription(Twist, 'velocidade', self.calcular_modulo_velocidade, 10)

    def calcular_modulo_velocidade(self, msg):
        modulo = ((msg.linear.x**2 + msg.linear.y**2 + msg.linear.z**2) +
                  (msg.angular.x**2 + msg.angular.y**2 + msg.angular.z**2)) ** 0.5
        self.publisher.publish(Float64(data=modulo))

def main(args=None):
    rclpy.init(args=args)
    node = CalculadorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
