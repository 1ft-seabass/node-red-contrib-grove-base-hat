#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os # add for node-red
import json # add for node-red
import sys #add for node-red

from grove.grove_led import GroveLed

def main():
  
    # print disable
    # sys.stdout = open(os.devnull, 'w')

    argvs = sys.argv #add for node-red

    pin = int(argvs[1])

    led = GroveLed(pin)

    # print enable
    # sys.stdout = sys.__stdout__

    control = argvs[2]
    # print (control == "1")
    if (control == "1"):
        led.on()
    if (control == "0"):
        led.off()

if __name__ == '__main__':
    main()

