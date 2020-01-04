#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
#

import time
import os # add for node-red
import sys #add for node-red
import json # add  for node-red
from grove.gpio import GPIO

def main():
    
    v = 0
    pre_v = 0

    # print disable
    sys.stdout = open(os.devnull, 'w')

    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.GPIO)
    pin = sh.argv2pin()
    gpio = GPIO(pin, GPIO.IN)
    v = pre_v = gpio.read()

    # print enable
    sys.stdout = sys.__stdout__

    while True:
        v = gpio.read()
        if v != pre_v:
            print(v)
            pre_v = v
        time.sleep(0.1)


if __name__ == '__main__':
    main()
