# Copyright 1996-2021 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This controller gives to its robot the following behavior:
According to the messages it receives, the robot change its
behavior.
"""

from controller import Lidar
from controller import LidarPoint
from controller import DistanceSensor
from controller import Robot

TIME_STEP = 32

robot = Robot()

# print(point)

lidar = Lidar("lidar")
lidar.enable(TIME_STEP)
lidar.enablePointCloud()

# https://pcl.readthedocs.io/projects/tutorials/en/latest/

# print(temp[10][0])
# while robot.step(1000) != -1:
    # temp = lidar.getPointCloud()
    # for i in temp:
        # print(i)
# print(help(lidar))
# lidar = robot.getDevice("lidar")
# lidar.enable(TIME_STEP)