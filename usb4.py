#!/usr/bin/env python

import sys, usb.core

dev = usb.core.find(idVendor=0x093a, idProduct=0x2510)

try:
    if dev.is_kernel_driver_active(0) is True:
        dev.detach_kernel_driver(0)
except usb.core.USBError as e:
    sys.exit("Kernel driver won't give up control over device: %s" % str(e))

try:
    dev.set_configuration()
    dev.reset()
except usb.core.USBError as e:
    sys.exit("Cannot set configuration the device: %s" % str(e))


endpoint = dev[0][(0,0)][0]
for attempts in xrange(100):
    try:
        data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        #print data
        RxData = ''.join([chr(x) for x in data])
        print RxData

    except:
        data = None
if data is None: 
    raise RuntimeError("no data found")
    print 'got data', data
