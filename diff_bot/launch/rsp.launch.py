import os

from ament_index_python.packages import get_package_share_directory
from launch.substitutions import command
import xacro
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
      
      urdf_file_name = 'robot.urdf.xacro'
      package_name = 'diff_bot'
      rviz_name='robot.rviz'


      robot_description_path = os.path.join(get_package_share_directory(package_name),
                             'urdf', urdf_file_name)
      
      xacro_file = xacro.process_file(robot_description_path)
      rviz_config_path = os.path.join(get_package_share_directory(package_name),
                                    'rviz', rviz_name)
      robot_state_publisher_node = Node(
      package='robot_state_publisher',
      executable='robot_state_publisher',
      name='robot_state_publisher_node',
      parameters=[{'use_sim_time': True, 'robot_description': xacro_file.toxml()}],  # Pass processed URDF XML
      output="screen"
      )

      joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
         name='joint_state_publisher_gui_node',
        output="screen"
    )
      rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
        )
      return LaunchDescription([
        robot_state_publisher_node,
        rviz2_node
    ])