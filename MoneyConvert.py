#MoneyConvert.py
MoneyStr=input("please input the account of money:")
if MoneyStr[:3]in["RMB"]:
    USD=eval(MoneyStr[3:])/6.78
    print("USD{:.2f}".format(USD))
elif MoneyStr[:3]in["USD"]:
    RMB=6.78*eval(MoneyStr[3:])
    print("RMB{:.2f}".format(RMB))
else:
    print("error")



#CurStr = input()
#if CurStr[:3] == "RMB":
 #   print("USD{:.2f}".format(eval(CurStr[3:])/6.78))
#elif CurStr[:3] in ['USD']:
    #print("RMB{:.2f}".format(eval(CurStr[3:])*6.78))
