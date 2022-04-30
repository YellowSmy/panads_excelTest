import pandas as pd
import matplotlib.pyplot as plt

#excel data import
df = pd.read_excel('C:/Users/user/Desktop/pandas_excelEx/excelData/sample_data_50.xlsx');
df_length = len(df.columns);
print(df_length);

#인덱스 행 보여주기
print("------------------------------------------");
dfIndex = df.loc[df_length];
print(dfIndex);
print("------------------------------------------");
print("정렬 기준을 선택하세요.");

#정렬할 데이터 선택
while True:
    selectRow = input();

    #유효 값 나올때까지 try
    try:
        print(df.loc[:, selectRow]); #select Data 출력

        #빈도 수 check
        print("각 항목 별 빈도수를 보시겠습니까?(Y/N)");
        answer = input();
        
        
        if(answer == 'Y' or answer == 'y'):
            print(df[selectRow].value_counts());

            #graph 그리기
            print("그래프를 그리시겠습니까?(Y/N)");
            answer = input();
            if(answer == 'Y' or answer == 'y'):
                df[selectRow].plot();
                plt.savefig(selectRow + '.png');
                print("그래프가 저장되었습니다. 확인해보세요!");
                break;

            else:
                break;
        
        else:
            break;

    except:
        print("행을 찾을 수 없습니다. 다시 입력해 주세요.");

### Y/N select는 UI 만들 때 N 공백으로 처리하기!


