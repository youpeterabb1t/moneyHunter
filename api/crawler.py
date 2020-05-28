# EVSIM LOAD
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

#CONFIG LOAD
from api.config import *
from api.instance.config import * #인스턴스로 덮어쓰기
#email module

from api.e_mail import send_async_email
#google sheet
import pygsheets
gc = pygsheets.authorize(service_file=GOOGLE_SERVICE_KEY)
sh = gc.open(GOOGLE_SPREADSHEET_NAME)

#parsing
import os#
import http
import urllib.request
from urllib.parse import quote

import json

class Crawler(BehaviorModelExecutor):
	def __init__(self, instance_time, destruct_time, name, engine_name):
		BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
		self.init_state("IDLE")
		self.insert_state("IDLE", Infinite)
		self.insert_state("PROC", CRAWLING_TIME)
				#in,output 포트 설정
		self.insert_input_port("process")
		self.insert_output_port("alert")


	def ext_trans(self,port, msg):
		if port == "process":
			self._cur_state = "PROC"
			data = msg.retrieve()
	def output(self):
		if self._cur_state == "PROC":
			url = PUBLIC_DATA_REQUEST_URL.format(quote(STATION), PUBLIC_DATA_SERVICE_KEY)
			request = urllib.request.Request(url)
			response = urllib.request.urlopen(request)
			rescode = response.getcode()

			if (rescode == 200):
				try:
					response_body = response.read()
				except (http.client.IncompleteRead) as e:
					response_body = e.partial
				try:			
					parse = json.loads(response_body)
					for ret in parse['list']:
						values = list(ret.values())
						wks = sh.worksheet('title', GOOGLE_WORKSHEET)
						wks.insert_rows(row=1, values=values)
					if int(values[15])>=2 or int(values[19]) >=2: #보통알림     #이부분 다른 모델로 사용가능
						send_async_email.delay("peterscience@naver.com", "Current Air Stat", "email/inform", list=values[2:29])
					elif int(values[15])>=3 or int(values[19]) >=3: #나쁨경고
						send_async_email.delay("peterscience@naver.com", "Current Air Stat", "email/warning", list=values[2:29])
				except:
					send_async_email("peterscience@naver.com", "Service Unavailable", "email/stoped")	

				
				

			else:
				print("Error Code:" + rescode)
				# select the first sheet
	def int_trans(self):
		if self._cur_state == "PROC":
			self._cur_state="PROC"


