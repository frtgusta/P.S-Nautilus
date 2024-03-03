import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        Node(
            package='sistema_solar',
            executable='sistema_solar_node',
            name='sistema_solar_node'
        )
    ])
