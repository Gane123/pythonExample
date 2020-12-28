import random
import pandas as pd
first_names=['A','B','C','D','E','F','G','H']
last_names=['a','b','c','d','e','f','g','h']
names=[]
scores=[]
for i in range(50):
    name=random.choice(first_names)+random.choice(last_names)+random.choice(last_names)+random.choice(last_names)
    names.append(name)
    scores.append(random.randint(0,100))
dict={'姓名':names,'分数':scores}
df=pd.DataFrame(dict)
df.to_excel('E:/output/成绩表.xlsx')