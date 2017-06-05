# raspimouse_game_controller
Package for operating Raspberry Pi Mouse with a controller

The script included in this package corresponds to DUALSHOCK 4 and Logicool Wireless Gamepad F710

# scripts

## ps4_cmd_vel.py

This is a script to operate Raspberry Pi Mouse using DUALSHOCK 4. With the square button pressed, you can publish the value of linear by pressing the up and down buttons, and angular values by pressing the right and left buttons.

### Operation Example

* Go to forward

  * □  + ↑

* Go to backward

  * □  + ↓

* Turn to the right

  * □  + →

* Turn to the left

  * □　+ ←

## logicool_cmd_vel.py

This is a script to operate Raspberry Pi Mouse using Logicool Wireless Gamepad F710. With the X button pressed, you can publish the value of linear by pressing the up and down buttons, and angular values by pressing the right and left buttons.

### Operation Example

* Go to forward

  * X + ↑

* Go to backward

  * X + ↓

* Turn to the right

  * X + →

* Turn to the left

  * X + ←

# tested on ...

* Ubuntu 16.04 Server
