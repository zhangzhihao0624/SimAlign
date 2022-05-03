import numpy as np
import matplotlib.pyplot as plt
f=open('D:/SimAlign/venv/f1.txt','r')
data=f.read()
print(data)

data=data.split('/')
print(data)

eng_ces=[]
eng_deu=[]
eng_fas=[]
eng_fra=[]
eng_fra2=[]
eng_hin=[]
eng_ron=[]
eng_ron2=[]
fin_grc=[]
fin_heb=[]
print(fin_heb)
print(data[3])
for i in range(13):
    eng_ces.append(data[0+i*10])
    eng_deu.append(data[1+i*10])
    eng_fas.append(data[2+i*10])
    eng_fra.append(data[3+i*10])
    eng_fra2.append(data[4+i*10])
    eng_hin.append(data[5+i*10])
    eng_ron.append(data[6+i*10])
    eng_ron2.append(data[7+i*10])
    fin_grc.append(data[8+i*10])
    fin_heb.append(data[9+i*10])
# #
print(eng_ces)
eng_ces=np.array(eng_ces)
eng_ces=eng_ces.astype(np.float).tolist()
eng_deu=np.array(eng_deu)
eng_deu=eng_deu.astype(np.float).tolist()
eng_fas=np.array(eng_fas)
eng_fas=eng_fas.astype(np.float).tolist()
eng_fra=np.array(eng_fra)
eng_fra=eng_fra.astype(np.float).tolist()
eng_fra2=np.array(eng_fra2)
eng_fra2=eng_fra2.astype(np.float).tolist()
eng_hin=np.array(eng_hin)
eng_hin=eng_hin.astype(np.float).tolist()
eng_ron=np.array(eng_ron)
eng_ron=eng_ron.astype(np.float).tolist()
eng_ron2=np.array(eng_ron2)
eng_ron2=eng_ron2.astype(np.float).tolist()
fin_grc=np.array(fin_grc)
fin_grc=fin_grc.astype(np.float).tolist()
fin_heb=np.array(fin_heb)
fin_heb=fin_heb.astype(np.float).tolist()

x=np.arange(0,13)

l1=plt.plot(x,eng_ces,'r--',label='eng-ces')
l2=plt.plot(x,eng_deu,'g--',label='eng-deu')
l3=plt.plot(x,eng_fas,'b--',label='eng-fas')
l4=plt.plot(x,eng_fra,'c--',label='eng-fra')
l5=plt.plot(x,eng_fra2,'m--',label='eng-fra2')
l6=plt.plot(x,eng_hin,'y--',label='eng-hin')
l7=plt.plot(x,eng_ron,'k--',label='eng-ron')
l8=plt.plot(x,eng_ron2,'w--',label='eng-ron2')
l9=plt.plot(x,fin_grc,color='pink',label='fin-grc')
l10=plt.plot(x,fin_heb,color='orange',label='fin-heb')

# plt.figure(figsize=(20,5),dpi=80)
plt.plot(x,eng_ces,'ro-',x,eng_deu,'g+-',x,eng_fas,'b^-',x,eng_fra,'cv-',x,eng_fra2,'m*-',x,eng_hin,'y<-',x,eng_ron,'k>-',x,eng_ron2,'wx-')
plt.plot(x,fin_grc,color='pink',marker='+')
plt.plot(x,fin_heb,color='orange',marker='o')
plt.title('f1 value in different layers(xlmr)')
plt.xlabel('layer')
plt.ylabel('f1')
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.show()
