# -*- coding: utf-8 -*- 

# DEAMON-クライアント
import threading
import time
import requests
import sys
import traceback

import com_logging2
import com_getparam
import com_getmaster
import com_func
import com_logsave
import com_sensor
import com_valve
import com_appConst

nTimeMax= 600

def init_proc():
	cls = com_appConst.appConstClass()
	clsLog = com_logging2.loggingClass()
	query = {
	'sv_id': str(cls.SV_ID)
	,'user_name': cls.mUSER_NAME
	,'password': cls.mPASSWORD
	}
	try:
		r = requests.get(cls.mURL_BASE + '/php/api_init.php', params=query, timeout=30 )
		print r.status_code
		print r.json()
	except:
		print "failue, init_proc"
		#clsLog.debug("failue, init_proc")
		raise
	finally:
		print "End ,init_proc"
		#clsLog.debug("End ,init_proc")
		
def mc_proc():
	cls = com_appConst.appConstClass()
	clsLog = com_logging2.loggingClass()
	clsMst = com_getmaster.getmasterClass()
	dMst= clsMst.get_mcList()
	sCsv = clsMst.getCsv(dMst)
	query = {
	'sv_id': str(cls.SV_ID)
	,'dmst': sCsv
	,'user_name': cls.mUSER_NAME
	,'password': cls.mPASSWORD
	}
	try:
		r = requests.post(cls.mURL_BASE + '/php/api_post_ms.php', query , timeout=30)
		print r.status_code
		print r.text
	except:
		print "failue, mc_proc"
		#clsLog.debug("failue, mc_proc")
		raise
	finally:
		print "End ,mc_proc"
		#clsLog.debug("End ,mc_proc")
		
def proc_sensor():
	clsLog = com_logging2.loggingClass()
	cls = com_appConst.appConstClass()	
	clsSens= com_sensor.sensorClass()
	datSen = clsSens.get_senList()
	sCsv = clsSens.getCsv(datSen)
	query = {
	  'sv_id': str(cls.SV_ID)
	  ,'dsen': sCsv
	  ,'user_name': cls.mUSER_NAME
	  ,'password': cls.mPASSWORD	}
	try:
		r = requests.post(cls.mURL_BASE +'/php/api_post_sensor.php', query , timeout= 60)
		print r.status_code
		print r.encoding
		print r.text
	except:
		print "failue, proc_sensor"
		#clsLog.debug("failue, proc_sensor")
		raise
	finally:
		print "End ,proc_sensor"
		#clsLog.debug("End ,proc_sensor")

def proc_valve():
	clsValve= com_valve.valveClass()
	clsLog = com_logging2.loggingClass()
	datValve = clsValve.get_valveList()
	sCsv     = clsValve.getCsv(datValve)
	cls = com_appConst.appConstClass()
	query = {
	'sv_id': str(cls.SV_ID)
	,'dvalve': sCsv
	,'user_name': cls.mUSER_NAME
	,'password': cls.mPASSWORD
	}
	try:
		r = requests.post(cls.mURL_BASE +'/php/api_post_valve.php', query , timeout= 60)
		print r.status_code
		print r.encoding
		print r.text
	except:
		print "failue, proc_valve"
		#clsLog.debug("failue, proc_valve")
		raise
	finally:
		print "End ,proc_valve"
		#clsLog.debug("End ,proc_valve")

def proc_complete():
	cls = com_appConst.appConstClass()
	clsLog = com_logging2.loggingClass()
	query = {
	  'sv_id': str(cls.SV_ID)
	  ,'user_name': cls.mUSER_NAME
	  ,'password': cls.mPASSWORD
	}
	try:
		r = requests.get(cls.mURL_BASE + '/php/api_complete.php', params=query , timeout= 60)
		print r.status_code
		print r.encoding
		print r.json()
	except:
		print "failue, proc_complete"
		#clsLog.debug("failue, proc_complete")
		raise
	finally:
		print "End ,proc_complete"
		#clsLog.debug("End ,proc_complete")

def timer_proc():
	clsLog = com_logging2.loggingClass()
	print "#timer_proc"
	try:
		init_proc()
		mc_proc()
		proc_sensor()
		proc_valve()
		proc_complete()
	except:
		print "--------------------------------------------"
		print traceback.format_exc(sys.exc_info()[2])
		print "--------------------------------------------"
		clsLog.debug( traceback.format_exc(sys.exc_info()[2]) )
	
if __name__ == "__main__":
	clsLog = com_logging2.loggingClass()
	time.sleep(30)
	iCt=0
	clsLog.debug("Start , main()")
	
	while True:
		if(iCt >= nTimeMax):
			iCt=0
			tmObj = threading.Timer( 1.0, timer_proc)
			tmObj.start()
		time.sleep(1)
		iCt +=1


