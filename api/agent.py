import sys,os
# EVSIM LOAD
from evsim.system_simulator import SystemSimulator
from evsim.definition import *

#CONFIG LOAD
from api.config import *
from api.instance.config import *

#API UPDATE MODULE LOAD
from api.crawler import Crawler
#from api.reporter import Reporter
#
from manage import celery


@celery.task
def ssimulate():
    se = SystemSimulator()
    se.register_engine("background", SIMULATION_MODE)
    a= Crawler(0, Infinite, "machine", "background")
    se.get_engine("background").insert_input_port("start")
    se.get_engine("background").register_entity(a)
    se.get_engine("background").coupling_relation(None,"start",a,"process")
    se.get_engine("background").insert_external_event("start", None)
    se.get_engine("background").simulate()

