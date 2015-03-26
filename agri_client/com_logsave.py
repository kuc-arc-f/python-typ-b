# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define
mHost = "localhost"
mDB_NAME= "agri_db"
mUser ="agri_user"
mPass ="password"

#com_logsave
class logsaveClass:

    def __init__(self):
        print ""
        
    def saveLog(self, mcDat):
    	ret=False
    	cls = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=mHost, db=mDB_NAME, user=mUser, passwd=mPass, charset="utf8")
    	cursor = connection.cursor()
    	s_log="MC-ID="
    	s_log=s_log+mcDat["mc_id"]
    	s_log=s_log+" ,SNUM-1=" + mcDat["snum_1"]
    	s_log=s_log+" ,SNUM-2=" + mcDat["snum_2"]
    	s_log=s_log+" ,SNUM-3=" + mcDat["snum_3"]
    	s_log=s_log+" ,SNUM-4=" + mcDat["snum_4"]
    	
    	sql =u"INSERT INTO t_mlogs ("
    	sql =sql+"mc_id,txt_log,created"
    	sql =sql+") values ("
    	sql =sql+mcDat["mc_id"]
    	sql =sql+",'"+s_log+"',now()"
    	sql =sql+");"
    	    	
    	cursor.execute(sql)
    	connection.commit()
    	cursor.close()
    	connection.close()
    	ret=True
    	return ret
    	