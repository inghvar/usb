#!/usr/bin/env python

"""
list all usb-devices
"""

from __future__ import print_function
import argparse
import sys
import usb


def main():

    busses = usb.busses()
    for bus in busses:
        devices = bus.devices
        for dev in devices:
	    handle = dev.open()
	    print("Device:", dev.filename)
	    print("  VID: 0x{:04x}".format(dev.idVendor))
            print("  PID: 0x{:04x}".format(dev.idProduct))
	    print("  Manufacturer: 0x{:x}".format(dev.iManufacturer), end='')
	    if dev.iManufacturer == 0:
                print('')
            else:
                print(" --> '{}'".format(handle.getString(dev.iManufacturer, 255)))
	    print("  Product: 0x{:x}".format(dev.iProduct), end='')
	    if dev.iProduct == 0:
                print('')
            else:
                print(" --> '{}'".format(handle.getString(dev.iProduct, 255)))

            print("  Serial Number: 0x{:x}".format(dev.iSerialNumber), end='')
            if dev.iSerialNumber == 0:
                print('')
            else:
                print(" --> '{}'".format(handle.getString(dev.iSerialNumber, 255)))


if __name__ == '__main__':
  main()
