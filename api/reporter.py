# EVSIM LOAD
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *


#CONFIG LOAD
from config import *
from instance.config import *

class Reporter(BehaviorModelExecutor):
	def __init__(self, instance_time, destruct_time, name, engine_name):
		BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
		self.init_state("IDLE")
		self.insert_state("IDLE", Infinite)
		self.insert_state("REPORT", 0)

		self.insert_input_port("report")


	def ext_trans(self,port, msg):
		if port == "report":
			self._cur_state = "REPORT"
			data = msg.retrieve()

	def output(self):
		if self._cur_state=="REPORT":
			print("Send email",data)

	def int_trans(self):
		if self._cur_state == "REPORT":
			self._cur_state="IDLE"