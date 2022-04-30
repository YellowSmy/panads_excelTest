### TODO ###
# 개수 세기 -- Done
# 행 분리 -- Done
# 그래프 그리기 -- Done

from re import L
from matplotlib.pyplot import savefig
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/user/Desktop/pandas_excelEx/excelData/sample_data_50.xlsx');


# 정렬
df_sample = df.loc[:'성별코드', '신장(5Cm단위)'];
print(df_sample);


##개수 세기, 많은 값 찾기
len(df);
df_count = df['신장(5Cm단위)'].value_counts();
print(df_count);


#행 분리 후 셀 세기
for i in range(0,10):
    heightInfo = df['신장(5Cm단위)'].values[i];
    print(heightInfo);

#그래프 그리기 & save
dfgraph = df['신장(5Cm단위)'].plot.bar();
plt.savefig('test.png');


