#!/usr/bin/env python
#
# This code is for Grove - 3-Axis Digital Accelerometer(+/-400g)
# (https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer-400-p-1897.html)
#
# which is a low power high performance 3-axis linear accelerometer belonging
# to the "nano" family, with digital I2C serial interface standard output.
#
# This is the library for Grove Base Hat which used to connect grove sensors for raspberry pi.
#

'''
## License

The MIT License (MIT)

Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
Copyright (C) 2018  Seeed Technology Co.,Ltd. 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_mma7660 as upmMMA7660

def main():
    # Instantiate an MMA7660 on I2C bus 0
    myDigitalAccelerometer = upmMMA7660.MMA7660(
                                            upmMMA7660.MMA7660_DEFAULT_I2C_BUS,
                                            upmMMA7660.MMA7660_DEFAULT_I2C_ADDR);

    ## Exit handlers ##
    # This function stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit, including functions from myDigitalAccelerometer
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    # place device in standby mode so we can write registers
    myDigitalAccelerometer.setModeStandby()

    # enable 64 samples per second
    myDigitalAccelerometer.setSampleRate(upmMMA7660.MMA7660_AUTOSLEEP_64)

    # place device into active mode
    myDigitalAccelerometer.setModeActive()

    ax = upmMMA7660.new_floatp()
    ay = upmMMA7660.new_floatp()
    az = upmMMA7660.new_floatp()

    while (1):
        myDigitalAccelerometer.getAcceleration(ax, ay, az)
        outputStr = ("Acceleration: x = {0}"
                     "g y = {1}"
                     "g z = {2}g").format(upmMMA7660.floatp_value(ax),
        upmMMA7660.floatp_value(ay),
        upmMMA7660.floatp_value(az))
        #print(outputStr)
        print(upmMMA7660.floatp_value(ax), upmMMA7660.floatp_value(ay), upmMMA7660.floatp_value(az))
        time.sleep(.5)

if __name__ == '__main__':
    main()
