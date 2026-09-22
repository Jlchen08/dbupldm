import pandas as pd
from scipy.stats import wilcoxon

# 读取CSV文件
df = pd.read_csv("win_draw_loss_table.csv")

# 只保留WIN行，去除ALL汇总行
win_df = df[(df["Metric"] == "WIN") & (df["η"] != "ALL")].copy()

# 将 η 转为 float，方便排序
win_df["η"] = win_df["η"].astype(float)
win_df = win_df.sort_values(by="η")

# 设定比较目标
methods = ["SVM", "UPSVM", "PinSVM", "LDM"]
dbupldm_wins = win_df["DBUPLDM"].tolist()

# 比较 DBUPLDM vs 其他方法
print(" Wilcoxon Signed-Rank Test (on WIN counts):\n")

for method in methods:
    method_wins = win_df[method].tolist()
    stat, p = wilcoxon(dbupldm_wins, method_wins)
    print(f"DBUPLDM vs {method}:")
    print(f"  Wilcoxon statistic = {stat}, p-value = {p:.8f}")
    if p < 0.05:
        print("  ✅ 差异具有统计学显著性（p < 0.05）\n")
    else:
        print("  ❌ 差异不具有统计学显著性（p ≥ 0.05）\n")
