# streetdrone_logitech_demo
Set up required to control the Streetdrone via Logitech G29 Steering wheel + pedals

Different configuration files can be used for different joysticks

```
mkdir joy_ws
cd joy_ws
mkdir src
git clone <repository>

cd ~/joy_ws
colcon build
source install/setup.bash
ros2 launch teleop_twist_joy teleop-launch.py

```
In new terminal window
```
source install/setup.bash
ros2 run twist_to_motor twist_to_motor
```
Need to git clonde the sdk thing again idk y
