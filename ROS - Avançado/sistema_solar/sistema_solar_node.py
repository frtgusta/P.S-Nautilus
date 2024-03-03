import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import math
import yaml

class SistemaSolarNode(Node):
    def __init__(self):
        super().__init__('sistema_solar_node')
        self.load_parameters()
        self.planeta_publishers = {}
        for planeta, raio_orbita in self.parametros_planetas.items():
            self.planeta_publishers[planeta] = self.create_publisher(PoseStamped, f'posicao_{planeta}', 10)
        self.timer = self.create_timer(0.1, self.atualizar_posicoes_planetas)

    def load_parameters(self):
        with open('parametros.yaml', 'r') as file:
            parametros = yaml.safe_load(file)
            self.parametros_planetas = parametros['parametros_planetas']

    def atualizar_posicoes_planetas(self):
        tempo_atual = self.get_clock().now().to_msg()
        for planeta, raio_orbita in self.parametros_planetas.items():
            posicao_planeta = PoseStamped()
            posicao_planeta.header.stamp = tempo_atual
            posicao_planeta.header.frame_id = 'estrela'
            posicao_planeta.pose.position.x = raio_orbita * math.cos(tempo_atual.sec)
            posicao_planeta.pose.position.y = raio_orbita * math.sin(tempo_atual.sec)
            self.planeta_publishers[planeta].publish(posicao_planeta)

def main(args=None):
    rclpy.init(args=args)
    sistema_solar_node = SistemaSolarNode()
    rclpy.spin(sistema_solar_node)
    sistema_solar_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
