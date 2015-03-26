# -*- coding: utf-8 -*- 
import MySQLdb
import xml.dom.minidom
import codecs

import com_appConst

#define

#com_getmaster
class getmasterClass:

    def __init__(self):
        print ""
        
    def getMaster(self, sId):
    	cls = com_appConst.appConstClass()
    	
    	ret = {"mc_id": 0L, "moi_num" : 0
    	, "kai_num_1": 0, "vnum_1": 0
    	, "kai_num_2": 0, "vnum_2": 0
    	, "kai_num_3": 0, "vnum_3": 0
    	, "kai_num_4": 0, "vnum_4": 0
    	, "ck_num":0  , "created":0
    	}
        connection = MySQLdb.connect(host=cls.mHost, db= cls.mDB_NAME, user=cls.mUser, passwd=cls.mPass, charset="utf8")
        cursor = connection.cursor()
        sSql ="select id, moi_num"
        sSql =sSql+", kai_num_1, vnum_1"
        sSql =sSql+", kai_num_2, vnum_2"
        sSql =sSql+", kai_num_3, vnum_3"
        sSql =sSql+", kai_num_4, vnum_4"
        sSql =sSql+", ck_num, created"
        sSql =sSql+" from m_mcs"
        sSql =sSql+" where id="+ sId
        sSql =sSql+" limit 1"
        #print sSql
        cursor.execute( sSql )
        result = cursor.fetchall()
        for row in result:
        	#print row
        	ret["mc_id"]   = row[0]
        	ret["moi_num"] = row[1]
        	ret["kai_num_1"] = row[2]
        	ret["vnum_1"]    = row[3]
        	ret["kai_num_2"] = row[4]
        	ret["vnum_2"]    = row[5]
        	ret["kai_num_3"] = row[6]
        	ret["vnum_3"]    = row[7]
        	ret["kai_num_4"] = row[8]
        	ret["vnum_4"]    = row[9]
        	ret["ck_num"]    = row[10]
        	ret["created"]   = row[11]
        cursor.close()
        connection.close()
        return ret
        
    def get_mcList(self ):
    	retList=[];
    	cls = com_appConst.appConstClass()
    	
        connection = MySQLdb.connect(host=cls.mHost, db= cls.mDB_NAME, user=cls.mUser, passwd=cls.mPass, charset="utf8")
        cursor = connection.cursor()
        sSql ="select id, moi_num"
        sSql =sSql+", kai_num_1, vnum_1"
        sSql =sSql+", kai_num_2, vnum_2"
        sSql =sSql+", kai_num_3, vnum_3"
        sSql =sSql+", kai_num_4, vnum_4"
        sSql =sSql+", ck_num, DATE_FORMAT(created,'%Y-%m-%d %H:%i:%s') as creat_dt, mc_name"
        sSql =sSql+" from m_mcs"
        sSql =sSql+" limit 100;"
        #print sSql
        cursor.execute( sSql )
        result = cursor.fetchall()
#        iCt=0
        for row in result:
        	#print row
	    	item = {"mc_name" : "","mc_id": 0L, "moi_num" : 0
	    	, "kai_num_1": 0, "vnum_1": 0
	    	, "kai_num_2": 0, "vnum_2": 0
	    	, "kai_num_3": 0, "vnum_3": 0
	    	, "kai_num_4": 0, "vnum_4": 0
	    	, "ck_num":0  , "created":0
	    	}
        	
        	item["mc_id"]   = row[0]
        	item["moi_num"] = row[1]
        	item["kai_num_1"] = row[2]
        	item["vnum_1"]    = row[3]
        	item["kai_num_2"] = row[4]
        	item["vnum_2"]    = row[5]
        	item["kai_num_3"] = row[6]
        	item["vnum_3"]    = row[7]
        	item["kai_num_4"] = row[8]
        	item["vnum_4"]    = row[9]
        	item["ck_num"]    = row[10]
        	item["created"]   = row[11]
        	item["mc_name"]    = row[12]
        	#print "name= "+ item["mc_name"]
        	retList.append(item)
#        	iCt= iCt+1
        cursor.close()
        connection.close()
        return retList
        
    def getXml(self ,dMc):
    	sRet=""
    	impl = xml.dom.minidom.getDOMImplementation()
    	doc = impl.createDocument(None, 'top', None)
    	top_element = doc.documentElement
    	
#    		node1_text = doc.createTextNode(u'node1のテキスト')
    	for row in dMc:
    		item = doc.createElement('item')
    		node_mc_id = doc.createElement('mc_id')
    		node_mc_id_text = doc.createTextNode( str(row["mc_id"]))
    		node_mc_id.appendChild(node_mc_id_text)
    		node_moi_num = doc.createElement('moi_num')
    		node_moi_numText = doc.createTextNode( str(row["moi_num"]))
    		node_moi_num.appendChild(node_moi_numText)
    		#mc_name unicode(row["mc_name"], 'utf-8')
    		#node_mc_name = doc.createElement('mc_name')
    		#node_mc_nameText = doc.createTextNode(row["mc_name"])
    		#node_mc_name.appendChild(node_mc_nameText)
    		
    		item.appendChild(node_mc_id)
    		item.appendChild(node_moi_num)
    		#item.appendChild(node_mc_name)
    		top_element.appendChild(item)
    	sRet =doc.toxml('UTF-8')
    	return sRet
    	#print(doc.toxml('UTF-8'))
    	
    def getCsv(self ,dMc):
    	sRet =""
    	for row in dMc:
    		sRet +=  '"' + str(row["mc_id"])     + '","' + str(row["moi_num"])+'"'
    		sRet += ',"' + str(row["kai_num_1"]) + '","' + str(row["vnum_1"]) + '"'
    		sRet += ',"' + str(row["kai_num_2"]) + '","' + str(row["vnum_2"]) + '"'
    		sRet += ',"' + str(row["kai_num_3"]) + '","' + str(row["vnum_3"]) + '"'
    		sRet += ',"' + str(row["kai_num_4"]) + '","' + str(row["vnum_4"]) + '"'
    		sRet += ',"' + str(row["ck_num"])    + '","' + row["created"] + '"'
    		sRet += ',"' + row["mc_name"] + '"'
    		sRet += '\n'
    	return sRet
