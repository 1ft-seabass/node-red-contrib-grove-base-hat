#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
'''
This is the code for
    - `Grove - Red LED    <https://www.seeedstudio.com/Grove-Red-LED-p-1142.html>`_
    - `Grove - Green LED  <https://www.seeedstudio.com/Grove-Green-LED-p-1144.html>`_
    - `Grove - Purple LED <https://www.seeedstudio.com/Grove-Purple-LED-3m-p-1143.html>`_
    - `Grove - White LED  <https://www.seeedstudio.com/Grove-White-LED-p-1140.html>`_

Examples:

    .. code-block:: python

        import time
        from grove.grove_led import GroveLed

        # connect to pin 5(slot D5)
        PIN   = 5
        led = GroveLed(PIN)

        while True:
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
'''
import time
import os # add for node-red
import json # add for node-red
import sys #add for node-red
from grove.gpio import GPIO

__all__ = ['GroveLed', 'GPIO']

class GroveLed(GPIO):
    '''
    Class for Grove - XXXX Led

    Args:
        pin(int): number of digital pin the led connected.
    '''
    def __init__(self, pin):
        super(GroveLed, self).__init__(pin, GPIO.OUT)

    def on(self):
        '''
        light on the led
        '''
        self.write(1)

    def off(self):
        '''
        light off the led
        '''
        self.write(0)


Grove = GroveLed


def main():

    # print disable
    sys.stdout = open(os.devnull, 'w')

    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.GPIO)
    pin = sh.argv2pin()
    argvs = sys.argv #add for node-red

    led = GroveLed(pin)

    # print enable
    sys.stdout = sys.__stdout__

    control =  argvs[2]
    # print (control == "1")
    if (control == "1"):
        led.on()
    if (control == "0"):
        led.off()

if __name__ == '__main__':
    main()

