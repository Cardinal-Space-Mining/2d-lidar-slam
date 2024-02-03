import pickle
import unittest
import numpy
import time

from FastPyRpLidar import RPLidar


class TestRPLidar(unittest.TestCase):
    def test_construction(self):
        l = RPLidar("/dev/ttyUSB0",1000000)


    def test_scan(self):
        l = RPLidar("/dev/ttyUSB0",1000000)
        l.start_motor()
        l.get_scanline()


def lidarThings():
    l = RPLidar("/dev/ttyUSB0",1000000)
    l.start_motor()
    time.sleep(1) # do not remove this sleep

    def scanningTime():
        data = l.get_scanline()
        for x in data:
            print(x[1])

    while(True):
        scanningTime()
        time.sleep(1)



if __name__ == '__main__':
    lidarThings()
    # unittest.main()
 
