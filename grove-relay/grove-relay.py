#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from grove.grove_relay import GroveRelay

def main():

    argvs = sys.argv

    pin = int(argvs[1])

    relay = GroveRelay(pin)

    control =  argvs[2]
    if (control == "1"):
        relay.on()
    if (control == "0"):
        relay.off()         

if __name__ == '__main__':
    main()
