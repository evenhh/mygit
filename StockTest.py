#--*--coding:utf-8--*--
'''
   a script for monitor stock price
'''
import tushare as  ts 
import itchat
import datetime
import time
import sys
def send_msg(msg,to_user):
	itchat.auto_login(hotReload=True)
	itchat.send(msg,to_user)

def get_msg(code,price):
	data=ts.get_realtime_quotes(code)
	now_price=float(data.price[0])
	name=data.name[0]
	text=""
	if now_price<price:
		precent="%.2f"%((now_price-price)/price*100)
		#precent=1
		text=data.name[0]+u"\n现价:"+str(now_price)+u"\n买入价:"+str(price)+u"\n涨幅:"+precent+"%"
		print text
	return text

if __name__=="__main__":
	while  True:
		code=sys.argv[1]
		price = float(sys.argv[2])
		to_user= sys.argv[3]
		msg=get_msg(code,price)
		if msg :
			send_msg(msg,to_user)
		time.sleep(10)
