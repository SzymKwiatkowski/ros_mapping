from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    slam_params_file = os.path.join(get_package_share_directory('mapping'), 
                                    'config', 'mapper_params.yaml')
    
    start_async_slam_toolbox_node = Node(
        parameters=[
          slam_params_file,
          {'use_sim_time': True}
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen')
    
    map_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "map", "odom"],
    )
    
    odom_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        output="screen",
        arguments=["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "odom", "base_footprint"],
    )
    
    bf2laser_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "base_footprint", "laser"],
    )

    ld = LaunchDescription()

    ld.add_action(start_async_slam_toolbox_node)
    ld.add_action(map_tf)
    ld.add_action(odom_tf)
    ld.add_action(bf2laser_tf)

    return ld
