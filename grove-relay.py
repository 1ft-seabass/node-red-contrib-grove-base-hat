#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
'''
This is the code for
    - `Grove - Relay <https://www.seeedstudio.com/s/Grove-Relay-p-769.html>`_
Examples:
    .. code-block:: python
        import time
        from grove.grove_relay import GroveRelay
        # connect to pin 5(slot D5)
        PIN   = 5
        relay = GroveRelay(PIN)
        while True:
            relay.on()
            time.sleep(1)
            relay.off()
            time.sleep(1)
'''
import sys
import os
import time
from grove.gpio import GPIO

__all__ = ["GroveRelay"]

class GroveRelay(GPIO):
    '''
    Class for Grove - Relay
    Args:
        pin(int): number of digital pin the relay connected.
    '''
    def __init__(self, pin):
        super(GroveRelay, self).__init__(pin, GPIO.OUT)

    def on(self):
        '''
        enable/on the relay
        '''
        self.write(1)

    def off(self):
        '''
        disable/off the relay
        '''
        self.write(0)


Grove = GroveRelay


def main():

    # print disable
    sys.stdout = open(os.devnull, 'w')

    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.GPIO)
    pin = sh.argv2pin()
    
    argvs = sys.argv

    relay = GroveRelay(pin)

    # print enable
    sys.stdout = sys.__stdout__

    control =  argvs[2]
    if (control == "1"):
        relay.on()
    if (control == "0"):
        relay.off()         

if __name__ == '__main__':
    main()
