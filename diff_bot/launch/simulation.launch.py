import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():


    gazebo_pkg='gazebo_ros'
    spwan_node='spawn_entity.py'

    spawn_entity_node = Node(
        package=gazebo_pkg,
        executable=spwan_node,
        arguments=['-topic', 'robot_description', '-entity', 'my_robot']
    )

    pkg_name = 'diff_bot'
    rsp_file ='rsp.launch.py'
    rsp_path=os.path.join(get_package_share_directory(pkg_name),
                                    'launch',rsp_file)
    rsp =IncludeLaunchDescription([rsp_path])


    gazebo_file ='gazebo.launch.py'
    gazebo_path=os.path.join(get_package_share_directory(gazebo_pkg),
                                    'launch',gazebo_file)
    gazebo=IncludeLaunchDescription([gazebo_path])
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity_node
    ])

