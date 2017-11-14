data = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42
lst=[]
lst.extend (data)
result=map(str,lst)
#print result
print "\n".join("%-20s %s"%(result[i],result[i+len(result)/2])
	for i in range(len(result)/2))
# if len(result) %2 != 0:
# 	result.append(" ")
# split=len(result)/2
# result1=result[0:split]
# result2=result[split:]
# for key, value in zip(result1,result2):
# 	print '%-20s %s'%(key,value)
	#print i[0]