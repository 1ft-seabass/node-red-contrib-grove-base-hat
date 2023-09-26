#!/usr/bin/env python

import os # add for node-red
import sys # add for node-red
import json # add  for node-red
import time

from grove.grove_temperature_humidity_sensor_sht3x import GroveTemperatureHumiditySensorSHT3x

def main():
    # get address
    arguments = sys.argv

    # print disable
    # sys.stdout = open(os.devnull, 'w')

    sensor = GroveTemperatureHumiditySensorSHT3x()

    # print enable
    # sys.stdout = sys.__stdout__

    temperature, humidity = sensor.read()
    print(json.dumps({"temperature":'{:.2f}'.format(temperature), "humidity":'{:.2f}'.format(humidity)}))


if __name__ == "__main__":
    main()
