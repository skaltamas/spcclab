import re
from prettytable import PrettyTable
t = PrettyTable(['Srno', 'Instruction'])
t1 = PrettyTable(['Macro Name', 'MDTP','#PP','#KP','#EV'])
name=""
es,pp,data=([] for i in range(3))
esc,ppc,keypc,mdt=0,0,0,0
fr=open("macro.txt","r")
data=fr.readlines()
for i in range(len(data)):
	data[i]=data[i].upper()
	if 'MACRO' in data[i]:
		i+=1
		mname=re.search("^[A-Z]+",data[i])
		name=mname.group(0)
		if name in data[i]:
			mdt=data.index(data[i])
			strdata=data[i].split()
			for j in range(len(strdata)):
				strdata[j]=strdata[j].replace(',', '')
				strdata[j]=strdata[j].replace(' ', '')
				result=re.findall("&+[A-Za-z]+$",strdata[j])
				ppc=len(result)
				result="".join(result)
				pp.append(result)
				result1=re.findall("&+[\w]+=[\w]+",strdata[j])
				keypc=len(result1)
				result1="".join(result1)
			i+=1		
		if 'LCL' in data[i]:
			strdata1=data[i].split()
			for j in range(len(strdata1)):
				strdata1[j]=strdata1[j].replace(',', '')
				strdata1[j]=strdata1[j].replace(' ', '')
				result3=re.findall("&+[A-Za-z]+$",strdata1[j])
				es.append(result3)


	t.add_row(["#"+str(i),data[i]])
while '' in pp:
    pp.remove('')
while [] in es:
    es.remove([])
ppc=len(pp)
esc=len(es)
t1.add_row([name,mdt,ppc,keypc,esc])
t.del_row(0)
print("********MDT*********\n")
print(t)
print("********MNT*********\n")
print(t1)
