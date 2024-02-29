from setuptools import find_packages, setup

package_name = 'sensor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'geometry_msgs', 'std_msgs'],  # Adicione as dependências necessárias
    zip_safe=True,
    maintainer='root',
    maintainer_email='gustafreitas215@gmail.com',
    description='Pacote para publicar e calcular velocidades em ROS2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publicador = sensor.publicador:main',
            'calculador = sensor.calculador:main',
            'impressao = sensor.impressao:main'
        ],
    },
)
