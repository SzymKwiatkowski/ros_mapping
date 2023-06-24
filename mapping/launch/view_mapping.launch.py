from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    rviz_config = os.path.join(get_package_share_directory('mapping'), 'rviz', 'rviz2_config.rviz')

    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/mapping.launch.py'])),
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=['-d', rviz_config],
        )
    ])
