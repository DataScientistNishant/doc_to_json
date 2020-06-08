
# My first Program in python using pandas
#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
gk = pd.read_fwf('GK-13.txt')
gk


# In[61]:


gk = list(gk["ï»¿[hello]"])
gk


# In[62]:


temp  =[]

final = ""
quesline  = ""

for line in gk:
    if line.startswith("Q"):
        if quesline != "" or final != "":
            temp.append((quesline + final))
            final = ""        
        quesline = line;
    else:
        final += ","+line
        

#df = pd.DataFrame(new_arr,columns=["Qno", "Ques"])

temp


# In[63]:


new_arr  =[]


for line in temp:
    if ";" in line:
        questn = line.split(";") 
                   
        if "[" in questn[1]:
            ops = questn[1].split("[")
            news = [questn[0]]
            if "Answer:" in ops[4]:
                ans = ops[4].split("Answer:")
            
            opttemp = ops[0:-2]
            news.extend(opttemp)
            news.extend(ans)
            new_arr.append(news)

new_arr


# In[64]:


df = pd.DataFrame(new_arr, columns=['Qno','Que','op1','op2','op3','op4','ans'])
df


# In[65]:


df['op1'] =  df['op1'].str.replace('A]','')
df['op1']


# In[66]:


df['op2'] = df['op2'].str.replace('B]','')
df['op2']


# In[67]:


df['op3']=df['op3'].str.replace('C]','')
df['op3']


# In[68]:


df['op4']=df['op4'].str.replace('D]','')
df['op4']


# In[69]:


arr = []

leng=len(df['Qno'])

for idx in range(leng+1):
    if idx > 0:
        arr.append(idx)
df['Qno'] = arr
df


# In[168]:


import re
list1 = list([df['Que'],df['op2'],df['op3'],df['op4']])

for idx in range(len(list1)):
    for idx2 in range(len(list1[idx])):
        if list1[idx][idx2][-1]==",":
            list1[idx][idx2]=list1[idx][idx2][0:-1]
        
#df['op2'],df['op3'],df['op4'] = list1
ques = df['Que'].copy()
ques
qu = []
for spec in ques:
    qu.append(re.sub("[^A-Za-z0-9,.?]"," ",spec))
    
df['Que'] = qu
df['Que'][13]
           


# In[189]:


import json

dictarr= []


for i in range(len(df["Qno"])):
    tempdic = {
        "qno":"",
        "ques":"",
        "op0":"",
        "op1":"",
        "op2":"",
        "op3":"",
        "ans":""
    }
    tempdic["qno"] = df.iloc[i][0]
    tempdic["ques"] = df.iloc[i][1]
    tempdic["op0"] = df.iloc[i][2]
    tempdic["op1"] = df.iloc[i][3]
    tempdic["op2"] = df.iloc[i][4]
    tempdic["op3"] = df.iloc[i][5]
    tempdic["ans"] = df.iloc[i][6]    
    dictarr.append(tempdic)
    


file = open("myoutput.json", "w")
file.write(str(dictarr))
file.close()


# In[190]:


dictarr


# In[ ]:




