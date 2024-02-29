import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ImpressaoNode(Node):
    def __init__(self):
        super().__init__('impressao_node')
        self.create_subscription(Float64, 'modulo_velocidade', self.imprimir_velocidade, 10)

    def imprimir_velocidade(self, msg):
        self.get_logger().info('Módulo da Velocidade: %f' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ImpressaoNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
