import pandas as pd

split_portion = 10  # split the dataset into smaller pieces

for i in range(4):
    file_name = f"./dataset/bda2024_202203-202402_內容數據_新聞{i+1}.csv"
    if i == 3:
        file_name = "./dataset/bda2024_微股力_社群PKTD-2年.csv"
    df = pd.read_csv(file_name)
    split_size = len(df)//split_portion
    for k in range(split_portion):
        small_df = df.iloc[k*split_size:min(len(df), (k+1)*split_size)]
        small_df.to_csv(file_name.replace(".csv", "")+f"-{k}.csv")
