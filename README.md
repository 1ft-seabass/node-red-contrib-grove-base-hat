# node-red-contrib-grove-base-hat

The node for Grove Base HAT for Raspberry Pi.

## Note

![2019-07-30_17h51_25.jpg (218.9 kB)](https://img.esa.io/uploads/production/attachments/3062/2019/08/02/8131/6f65c5d3-d0cd-4585-b2e9-9a22104e9cec.jpg)

Developing Grove Base HAT for Raspberry Pi at the time of 2019/08/02.

https://www.seeedstudio.com/Grove-Base-Hat-for-Raspberry-Pi.html

The node don't support Grove Base HAT for Raspberry Pi Zero **yet**.

## Install and Setup

### 0. Setup Grove Base HAT

Install Online one-click installation flow at basic Grove Base HAT setup page.

http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/

* Tips
    * Require pip,pip3 added install if your using Raspbian Lite.

Try to work various Grove parts before starting Node-RED of Grove Base HAT node :)

### 1. Install Grove Base HAT node

Execute following command. npm install node-red-contrib-grove-base-hat

then the node may be installed in "/home/pi/.node-red".

OR

Adding nodes to the palette
https://nodered.org/docs/user-guide/runtime/adding-nodes

## How to use

## Prepare and connect Grove LED

Connect Grove LED to Grove Base HAT's D18 port.

## Import the sample flow

![image.png (12.0 kB)](https://img.esa.io/uploads/production/attachments/3062/2019/08/02/8131/c031c378-04cb-40e4-a3b9-c0037734c469.png)

Import this flow.

```
[{"id":"3ab363a8.b5975c","type":"grove-led","z":"67547794.3ec478","name":"","port_number":"18","x":460,"y":700,"wires":[]},{"id":"ca04ad9.009385","type":"inject","z":"67547794.3ec478","name":"","topic":"","payload":"0","payloadType":"num","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":310,"y":740,"wires":[["3ab363a8.b5975c"]]},{"id":"4d045af6.e1cca4","type":"inject","z":"67547794.3ec478","name":"","topic":"","payload":"1","payloadType":"num","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":310,"y":660,"wires":[["3ab363a8.b5975c"]]},{"id":"c0a7f102.46dbe","type":"comment","z":"67547794.3ec478","name":"Grove LED","info":"","x":300,"y":620,"wires":[]}]
```

* The detail about Node-RED flow import way
    * https://nodered.org/docs/user-guide/editor/workspace/import-export

## Check port setting

![image.png (12.2 kB)](https://img.esa.io/uploads/production/attachments/3062/2019/08/02/8131/34a16f71-8dd1-4429-8303-90264856d347.png)

Look  Grove LED node setting. Check port number in node setting and connecting port number.

Generally the sample flow default port setting is D18. If your setting port is defferent from sample flow D18. Fit port your connecting port and node setting port number.

Click Node-RED inject nodes written 1 and 0.  When inject nodes as 1, Grove LED will turn on. When inject nodes as 0, it will 
 turn off.

## Grove working to each node

* grove-led
    * Grove - Red LED
        * https://www.seeedstudio.com/Grove-Red-LED-p-1142.html
    * Grove - Green LED
        * https://www.seeedstudio.com/Grove-Green-LED-p-1144.html
    * Grove - Purple LED
        * https://www.seeedstudio.com/Grove-Purple-LED-3m-p-1143.html
    * Grove - White LED
        * https://www.seeedstudio.com/Grove-White-LED-p-1140.html
* grove-button
    * Grove - Button
        * https://www.seeedstudio.com/s/Grove-Button-p-766.html
* grove-ultrasonic-ranger
    * Grove - Ultrasonic Ranger
        * https://www.seeedstudio.com/Grove-Ultrasonic-Ranger-p-960.htm
* grove-light-sensor-v1_2
    * Grove - Light Sensor
        * https://www.seeedstudio.com/Grove-Light-Sensor-v1.2-p-2727.html
* grove-temperature-sensor
    * Grove - Temperature Sensor
        * https://www.seeedstudio.com/Grove-Temperature-Sensor-p-774.html
* grove-4-digit-display
    * Grove - 4 Digit Display
        * https://www.seeedstudio.com/Grove-4-Digit-Display.html
* grove-relay
    * Grove - Relay
        * https://www.seeedstudio.com/s/Grove-Relay-p-769.html
* grove-gesture-sensor
    * Grove - Gesture Sensor v1.0
        * http://www.seeedstudio.com/depot/Grove-Gesture-p-2463.html
* grove-oled-display-128x64
    * Grove - OLED Display 0.96
        * https://www.seeedstudio.com/Grove-OLED-Display-0.96%22-p-781.html
* grove-i2c-color-sensor-v2
    * Grove - I2C Color Sensor V2
        * https://www.seeedstudio.com/Grove-I2C-Color-Sensor-V2-p-2890.html
* grove-temperature-humidity-sensor-sht3x
    * Grove - Temperature & Humidity Sensor (SHT31) 
        * https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-SHT3-p-2655.html
* grove-magnetic-switch
    * Grove - Magnetic Switch
        * https://www.seeedstudio.com/Grove-Magnetic-Switch-p-744.html

