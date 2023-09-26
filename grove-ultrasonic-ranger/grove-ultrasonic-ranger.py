#!/usr/bin/env python

import sys
import os # add for node-red
import time
import json # add for node-red

from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

def main():
    
    # print disable
    # sys.stdout = open(os.devnull, 'w')

    argvs = sys.argv #add for node-red

    pin = int(argvs[1])
    sonar = GroveUltrasonicRanger(pin)

    # print enable
    # sys.stdout = sys.__stdout__

    print(sonar.get_distance())

if __name__ == '__main__':
    main()

