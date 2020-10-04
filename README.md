# robot

## Installation

cd catkin_ws/src
git clone https://github.com/tg863/robot
catkin build
cd ..
source devel/setup.bash

# visualizing robot

source devel/setup.bash
roslaunch urdf simulate.launch

# using moveitconfig terminal

source devel/setup.bash
roslaunch moveitconfig demo.launch
# using control
source devel/setup.bash
roslaunch control control.launch



source devel/setup.bash
rosservice call /control "mouvement:
 data: 'front'"
