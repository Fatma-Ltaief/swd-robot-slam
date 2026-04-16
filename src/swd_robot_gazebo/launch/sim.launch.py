import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    description_pkg = get_package_share_directory('swd_starter_kit_description')
    gazebo_pkg = get_package_share_directory('swd_robot_gazebo')

    urdf_file = os.path.join(description_pkg, 'urdf', 'swd_starter_kit.urdf')
    world_file = os.path.join(gazebo_pkg, 'worlds', 'empty.world')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'swd_robot', '-topic', 'robot_description'],
            output='screen'
        ),
    ])