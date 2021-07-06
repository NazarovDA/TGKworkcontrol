# coding: utf-8

import os
import json
import datetime as dt
from time import sleep
import logging

logging.basicConfig(filename="logs.log", level=logging.INFO)


__PROGRAMMS__ = dict()

with open("settings.json", "r") as ReadFile:
    __PROGRAMMS__ = json.load(ReadFile)

data: dict = dict()

def process_reboot(filepath, process):
    os.system(f"taskkill /im {process} /F")
    logging.info(f"Process {process} has been killed {dt.datetime.now()}")
    sleep(10)
    os.startfile(filepath)
    logging.info(f"Process with root {filepath} has been started {dt.datetime.now()}")


while True:
    for programm in __PROGRAMMS__:
        delta = dt.datetime.now() - dt.datetime.fromtimestamp(os.path.getctime(__PROGRAMMS__[programm]["file"]))
        if delta.total_seconds()/60 > 2:
            process_reboot(__PROGRAMMS__[programm]["root"], programm)
    
    sleep(20)
