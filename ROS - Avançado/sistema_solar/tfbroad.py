import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import math

class TFBroadcaster(Node):
    def __init__(self):
        super().__init__('tf_broadcaster')
        self.br = self.create_publisher(TransformStamped, 'tf', 10)
        self.timer = self.create_timer(0.1, self.broadcast_tf)

    def broadcast_tf(self):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'frame1'
        transform.child_frame_id = 'frame2'
        transform.transform.translation.x = 1.0
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 0.0
        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = math.sin(math.pi / 4)
        transform.transform.rotation.w = math.cos(math.pi / 4)
        self.br.publish(transform)

def main(args=None):
    rclpy.init(args=args)
    tf_broadcaster = TFBroadcaster()
    rclpy.spin(tf_broadcaster)
    tf_broadcaster.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
