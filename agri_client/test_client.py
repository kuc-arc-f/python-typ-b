# -*- coding: utf-8 -*- 

## リクエストのテスト
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


if __name__ == "__main__":
	cls = com_appConst.appConstClass()
	query = {
	  'sv_id': str(cls.SV_ID)
	  ,'user_name': cls.mUSER_NAME
	  ,'password': cls.mPASSWORD
	}
	r = requests.get(cls.mURL_BASE + '/php/api_test.php', params=query , timeout=30)
	print "http-status=" + str(r.status_code)
	sRes= r.json()
	sJson = json.dumps(sRes)
	print "response="+ sJson
	dct = json.loads(sJson)
	# print dct
	print "ret=" + str(dct["ret"])
	print "stat=" + dct["dat"]["stat"]
