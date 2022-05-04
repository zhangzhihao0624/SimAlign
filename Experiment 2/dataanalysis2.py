import numpy as np
import matplotlib.pyplot as plt
f=open('D:/SimAlign/venv/f1.txt','r')
data=f.read()
print(data)

data=data.split('/')
print(data)
print(len(data))
eng_ces_1=[]
eng_ces_2=[]
eng_ces_3=[]
eng_ces_4=[]
eng_ces_5=[]
eng_fra_1=[]
eng_fra_2=[]
eng_fra_3=[]
eng_fra_4=[]
eng_fra_5=[]
fin_heb_1=[]
fin_heb_2=[]
fin_heb_3=[]
fin_heb_4=[]
fin_heb_5=[]

for i in range(13):
    eng_ces_1.append(data[0+i*3])
    eng_ces_2.append(data[39+i*3])
    eng_ces_3.append(data[78+i*3])
    eng_ces_4.append(data[117+i*3])
    eng_ces_5.append(data[156+i*3])
    eng_fra_1.append(data[1+i*3])
    eng_fra_2.append(data[40+i*3])
    eng_fra_3.append(data[79+i*3])
    eng_fra_4.append(data[118+i*3])
    eng_fra_5.append(data[157+i*3])
    fin_heb_1.append(data[2+i*3])
    fin_heb_2.append(data[41+i*3])
    fin_heb_3.append(data[80+i*3])
    fin_heb_4.append(data[119+i*3])
    fin_heb_5.append(data[158+i*3])

eng_ces_1=np.array(eng_ces_1)
eng_ces_1=eng_ces_1.astype(np.float).tolist()
eng_ces_2=np.array(eng_ces_2)
eng_ces_2=eng_ces_2.astype(np.float).tolist()
eng_ces_3=np.array(eng_ces_3)
eng_ces_3=eng_ces_3.astype(np.float).tolist()
eng_ces_4=np.array(eng_ces_4)
eng_ces_4=eng_ces_4.astype(np.float).tolist()
eng_ces_5=np.array(eng_ces_5)
eng_ces_5=eng_ces_5.astype(np.float).tolist()
print(eng_ces_4)

eng_fra_1=np.array(eng_fra_1)
eng_fra_1=eng_fra_1.astype(np.float).tolist()
eng_fra_2=np.array(eng_fra_2)
eng_fra_2=eng_fra_2.astype(np.float).tolist()
eng_fra_3=np.array(eng_fra_3)
eng_fra_3=eng_fra_3.astype(np.float).tolist()
eng_fra_4=np.array(eng_fra_4)
eng_fra_4=eng_fra_4.astype(np.float).tolist()
eng_fra_5=np.array(eng_fra_5)
eng_fra_5=eng_fra_5.astype(np.float).tolist()

fin_heb_1=np.array(fin_heb_1)
fin_heb_1=fin_heb_1.astype(np.float).tolist()
fin_heb_2=np.array(fin_heb_2)
fin_heb_2=fin_heb_2.astype(np.float).tolist()
fin_heb_3=np.array(fin_heb_3)
fin_heb_3=fin_heb_3.astype(np.float).tolist()
fin_heb_4=np.array(fin_heb_4)
fin_heb_4=fin_heb_4.astype(np.float).tolist()
fin_heb_5=np.array(fin_heb_5)
fin_heb_5=fin_heb_5.astype(np.float).tolist()

x=np.arange(0,13)

l1=plt.plot(x,fin_heb_1,'r--',label='distortion=0.0')
l2=plt.plot(x,fin_heb_2,'g--',label='distortion=0.1')
l3=plt.plot(x,fin_heb_3,'b--',label='distortion=0.2')
l4=plt.plot(x,fin_heb_4,'c--',label='distortion=0.5')
l5=plt.plot(x,fin_heb_5,'m--',label='distortion=1.0')

plt.plot(x,fin_heb_1,'ro-',x,fin_heb_2,'g+-',x,fin_heb_3,'b^-',x,fin_heb_4,'cv-',x,fin_heb_5,'m*-')
plt.title('The relationship between position embeddings and distortion(dataset:eng-fra)')
plt.xlabel('layer')
plt.ylabel('f1')
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.show()
