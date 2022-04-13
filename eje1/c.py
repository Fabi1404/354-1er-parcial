import numpy as np
import pandas as pa
import matplotlib.pyplot as plt

csv = pa.read_csv('./eje1/caesarian.csv')

columns = ['Age','DeliveryMumber','DeliveryTime','Pressure','HeartProblem','Caesarian']

for i in range(0, 6):
    for j in range(i + 1, 6):
        csv.plot(kind='scatter',x=columns[i],y=columns[j],color='red')
        str = columns[i]+'_'+columns[j]
        plt.savefig('./eje1/'+str)

