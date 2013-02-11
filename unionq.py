#!/usr/bin/python


import ConfigParser
import argparse
import sys
import sleekxmpp
import logging
import signal
import zmq
import time

conf = "config.cfg"




def GetArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Specify a configuration file")
    args = parser.parse_args()
    print str(args)
    
    
    
def LoadConfigurations(conf):
    config = ConfigParser.ConfigParser()
    try:
        config.readfp(open(conf))
    except:
        pass
    sections = config.sections()
   # for each in sections:
   #     print each
   #     items = config.items(each)
   #     for item in items:
   #         print " - " + str(item)
        






if __name__ == '__main__':        
    LoadConfigurations(conf)
    GetArguments()