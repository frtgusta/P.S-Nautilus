import rclpy
from rclpy.node import Node

class SistemaSolarNode(Node):
    def __init__(self):
        super().__init__('sistema_solar_node')
        # Implemente a lógica do sistema solar aqui

def main(args=None):
    rclpy.init(args=args)
    sistema_solar_node = SistemaSolarNode()
    rclpy.spin(sistema_solar_node)
    sistema_solar_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
