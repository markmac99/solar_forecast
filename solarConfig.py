# config file
import os


def getDataDir():
    datadir = 'DATADIRSUBST'
    return os.path.expanduser(datadir)


def getSolarApiKey():
    solarkey = 'CHANGEME'
    return solarkey


def getLocation():
    return 51.88, -1.31


def getArrayDetails():
    decls = [45,46,49,45]
    azims = [-55, 35,145,140]
    kwps = [0.89,0.939,0.5,0.541]
    return decls, azims, kwps
