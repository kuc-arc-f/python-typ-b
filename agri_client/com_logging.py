# -*- coding: utf-8 -*- 

import com_appConst
import logging
LOG_FILENAME = '/tmp/agri_client_dbg.log'

#com_func
class loggingClass:

    def __init__(self):
        print ""
        
    def test(self, sStr):
#    	log_fmt = '%(asctime)s- %(name)s - %(levelname)s - %(message)s'
    	log_fmt = '%(asctime)s- %(levelname)s - %(message)s'
    	#"%(asctime)s - %(levelname)s - %(message)s"
    	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format=log_fmt)
    	#logging.debug('This message should go to the log file')
    	logging.debug( sStr)
