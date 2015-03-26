# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define


#com_sensor
class sensorClass:

    def __init__(self):
        print ""
        
    # @return TRUE: nothing.dat
    def Is_addSensor(self, mc_id, nSec):
    	ret=False
    	iCt=0
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	
    	dic = {"id": 0L, "creat_dt" : ""}
    	sSql="select id, DATE_FORMAT(created,'%Y-%m-%d %H:%i:%s') as creat_dt"
    	sSql=sSql+" from t_sensors where mc_id ="+mc_id
    	sSql=sSql+" ORDER BY created desc limit 1"
    	#print( "sSql="+ sSql)
    	cursor.execute( sSql )
    	result = cursor.fetchall()
    	for row in result:
    		iCt=iCt+1
    		dic["id"]        =row[0]
    		dic["creat_dt"]  =row[1]
    		
    	cursor.close()
    	if iCt==0:
    		return True
    		
    	cursor = connection.cursor()
    	sSql="SELECT  TIMESTAMPDIFF(SECOND, '" +dic["creat_dt"] + "', now()) as sec_num;"
    	#print( "sSql="+ sSql)
    	cursor.execute( sSql )
    	result = cursor.fetchall()
    	dfSec=0
    	for row in result:
    		dfSec        =row[0]
    	#print("dfSec="+str(dfSec))
    	
    	cursor.close()
    	connection.close()
    	if(dfSec > nSec ):
    		return True
    		
    	return ret
    	
    def saveSensor(self, getDat, datMc):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	if(datMc["vnum_1"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_sensors (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",snum"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",1"
    		sSql=sSql+","+getDat["snum_1"]
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()
    	if(datMc["vnum_2"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_sensors (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",snum"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",2"
    		sSql=sSql+","+getDat["snum_2"]
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()
    	if(datMc["vnum_3"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_sensors (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",snum"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",3"
    		sSql=sSql+","+getDat["snum_3"]
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()
    	if(datMc["vnum_4"]==1):
    		cursor = connection.cursor()
    		sSql=u"INSERT INTO t_sensors (mc_id"
    		sSql=sSql+",vnum"
    		sSql=sSql+",snum"
    		sSql=sSql+",created"
    		sSql=sSql+") values ("
    		sSql=sSql+getDat["mc_id"]
    		sSql=sSql+",4"
    		sSql=sSql+","+getDat["snum_4"]
    		sSql=sSql+",now() );"
    		cursor.execute(sSql)
    		connection.commit()
    		cursor.close()
    		
    	connection.close()
    	ret=True
    	return ret
    def get_senList(self ):
		retList=[]
		cls = com_appConst.appConstClass()
		connection = MySQLdb.connect(host=cls.mHost, db= cls.mDB_NAME, user=cls.mUser, passwd=cls.mPass, charset="utf8")
		cursor = connection.cursor()
		sSql="select mc_id, vnum, snum ,DATE_FORMAT(created,'%Y-%m-%d %H:%i:%s') as creat_dt, id from t_sensors"
#		sSql=sSql+" where created > (NOW() - INTERVAL 24 HOUR)"
		sSql=sSql+" where created > (NOW() - INTERVAL "+str(cls.mMinSen)+" MINUTE)"
		sSql=sSql+" limit 3000;"
		cursor.execute( sSql )
		result = cursor.fetchall()
		for row in result:
			item = {"mc_id" : 0 ,"vnum":0, "snum":0 , "created":""}
			item["mc_id"]   = row[0]
			item["vnum"]    = row[1]
			item["snum"]    = row[2]
			item["created"] = row[3]
			item["id"] = row[4]
			retList.append(item)
		cursor.close()
		connection.close()
		return retList
		
    def getCsv(self ,dMc):
    	sRet =""
    	for row in dMc:
    		sRet +=  '"' + str(row["mc_id"])    + '","' + str(row["vnum"])+'"'
    		sRet += ',"' + str(row["snum"])     + '"'
    		sRet += ',"' + row["created"]       + '","' + str(row["id"]) + '"'
    		sRet += '\n'
    	return sRet
