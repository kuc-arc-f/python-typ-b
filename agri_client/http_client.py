# -*- coding: utf-8 -*- 

## リクエストのテスト
import threading
import requests
import json

import com_getparam
import com_getmaster
import com_func
import com_logsave
import com_sensor
import com_valve
import com_appConst

mOK_CODE=1
mNG_CODE=0

ER_STAT_000="000"
ER_STAT_101="101"
ER_STAT_102="102"
ER_STAT_103="103"

#http_client
class httpClientClass:
	def __init__(self):
		print ""
	def init_proc(self):
		query = {
		  'sv_id': '1'
		}
		cls = com_appConst.appConstClass()
#		r = requests.get('http://192.168.1.26/agrisv/php/api_init.php', params=query)
		r = requests.get(cls.mURL_BASE + '/php/api_init.php', params=query)
		print r.status_code
		print r.encoding
	#	print r.text
		print r.json()
		
	def mc_proc(self):
		cls = com_appConst.appConstClass()
		clsMst = com_getmaster.getmasterClass()
		dMst= clsMst.get_mcList()
		sCsv = clsMst.getCsv(dMst)
		query = {
		  'sv_id': '1'
		  ,'dmst': sCsv
		}
#		r = requests.post('http://192.168.1.26/agrisv/php/api_post_ms.php', query )
		r = requests.post(cls.mURL_BASE + '/php/api_post_ms.php', query )
		print r.status_code
		print r.encoding
		print r.text
		
	def sensor_post(self):
		cls = com_appConst.appConstClass()
		clsSens= com_sensor.sensorClass()
		datSen = clsSens.get_senList()
		sCsv = clsSens.getCsv(datSen)
	#	print "ms.len=" + str(len(dMst))
		query = {
		  'sv_id': '1'
		  ,'dsen': sCsv
		}
		r = requests.post(cls.mURL_BASE +'/php/api_post_sensor.php', query )

		print r.status_code
		print r.encoding
		print r.text

	def valve_post(self):
		cls = com_appConst.appConstClass()
		clsValve= com_valve.valveClass()
		datValve = clsValve.get_valveList()
		sCsv     = clsValve.getCsv(datValve)
#	print "ms.len=" + str(len(dMst))
		query = {
		  'sv_id': '1'
		  ,'dvalve': sCsv
		}
		#r = requests.post('http://192.168.1.26/agrisv/php/api_post_valve.php', query )
		r = requests.post(cls.mURL_BASE +'/php/api_post_valve.php', query )
		
		print r.status_code
		print r.encoding
		print r.text	
	
	def proc_complete(self):
		cls = com_appConst.appConstClass()
		query = {
		  'sv_id': '1'
		}
#		r = requests.get('http://192.168.1.26/agrisv/php/api_complete.php', params=query)
		r = requests.get(cls.mURL_BASE + '/php/api_complete.php', params=query)
		print r.status_code
		print r.encoding
		print r.json()
		
	def execute_post(self):
		cls = com_appConst.appConstClass()
		t = threading.Timer( cls.mSpanNum , self.execute_post )
		t.start()
		self.init_proc()
		self.mc_proc()
		self.sensor_post()
		self.valve_post()
		self.proc_complete()
