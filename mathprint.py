from numpy import random
import datetime
print 'ready for print'
max_number = 100;
count = 100;
days = 27;
i = 0;
d1 = datetime.datetime.now()
d2 = d1+datetime.timedelta(days=1)

def day_quiz():
	for i in range(1,count+1):
		#print i,
		a = random.randint(10,max_number-1) 
		if random.randint(1,10)%2 == 0:
			b = random.randint(1,a-1)
			print '%d-%d=		' % (a,b),
		else:
			b = random.randint(1,max_number-a)
			print '%d+%d=		' % (a,b),
		
		if(i%5==0):
			print
			
def day_complex_quiz():
	for i in range(1,count+1):
		#print i,
		a = random.randint(10,max_number) 
		b = random.randint(1,a-1)
		print '%d-%d=		' % (a,b),
		if(i%5==0):
			print




for j in range(days):
	print 'No.%d Date:___________ Time cost:__________' % (j+1)
	day_quiz()
	print
	#print d2.strftime("%Y-%m-%d")
	
