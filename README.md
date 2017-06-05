# raspimouse_game_controller

Package for operating Raspberry Pi Mouse with some kinds of game controllers.

This package supports the following controllers:

* DUALSHOCK 4, and
* Logicool Wireless Gamepad F710.

# scripts

## ps4_cmd_vel.py

This is a script for connecting Raspberry Pi Mouse to a DUALSHOCK 4.

### how to control

To give motion command, you must press the button drawn a square.
With the press, you can control the robot with the four arrow buttons.
By pressing the up/down button, you can give the velocity of front/back
direction respectively. Angular velocity can be then given by pressing
the right or left button.

## logicool_cmd_vel.py

This is a script for connecting Raspberry Pi Mouse to a Logicool Wireless
Gamepad F710. 

### how to control

To give motion command, you must press the X button.
With the press, you can control the robot with the four arrow buttons.
By pressing the up/down button, you can give the velocity of front/back
direction respectively. Angular velocity can be then given by pressing
the right or left button.

# supporting distribution

* Ubuntu 16.04 Server (ROS distribution: Kinetic Kame)
