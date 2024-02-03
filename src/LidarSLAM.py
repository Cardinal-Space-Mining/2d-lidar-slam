import pickle
import numpy
import time

from FastPyRpLidar import RPLidar



def lidarThings():
    l = RPLidar("/dev/ttyUSB0",1000000)
    l.start_motor()
    time.sleep(1) # do not remove this sleep

    def scanPlease():
        data = l.get_scanline()
        for x in data:
            print("x: [", x[0],"] y: [",x[1],"]")

    while(True):
        scanPlease()
        time.sleep(1)



if __name__ == '__main__':
    lidarThings()
 
