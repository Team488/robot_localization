#!/usr/bin/env python3

import ament_index_python.packages
import launch
import launch_ros.actions

def generate_launch_description():

  # TODO: Port ROS 1 test launch params: clear_params="true" time-limit="100.0"
  return launch.LaunchDescription([
    launch_ros.actions.Node(
      package='robot_localization',
      node_executable='test_robot_localization_estimator',
      node_name='test_rle',
    ),
  ])
