import numpy as np
import pandas as pa

csv = pa.read_csv('./eje1/caesarian.csv')

primerquartil = csv['Age'].quantile(0.25)

for (columnName, columnData) in csv.iteritems():
    print(columnName)
    percentil50 = np.percentile(csv[columnName], 50)
    print('percentil 50 : ', percentil50)

print(primerquartil)
