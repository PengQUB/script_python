import pandas as pd

path = "/Users/momo/Desktop/xgboost_aibroadcaster/csv_form.csv"  # raw data csv file
tmp_csv = "/Users/momo/Desktop/xgboost_aibroadcaster/tmp_form.csv"
final_csv = "/Users/momo/Desktop/xgboost_aibroadcaster/final_form.csv"  # target csv file

train_df = pd.read_csv(path, header=1)
# print(train_df.shape)
# train_df.head(2)

present_list = ["火箭", "跑车", "游艇", "巴掌", "城堡", "飞碟", "钻石", "钻戒"]
thanks_list = ["谢", "感", "破费", "么么哒", "比心", "笔芯", "给大哥"]
askfor_list = ["送", "上个", "来个", "帮忙", "守塔", "破", "星光", "一人一", "飘屏", "飘个屏", "整", "刷", "圈", "排面", "输"]
praise_list = ["姐", "哥", "姐夫", "牛逼", "厉害", "豪", "六六六", "阔"]
welcome_list = ["欢迎", "你好", "来了"]
fansteam_list = ["关注", "点点", "来波", "红包", "集合", "一波"]
share_list = ["分享"]
words_list = present_list + thanks_list + askfor_list + praise_list + welcome_list + fansteam_list + share_list
for keyword in words_list:
    train_df[train_df[train_df.columns[1]].str.contains(keyword, na=False)].to_csv(tmp_csv, mode='a', header=False)

new_data = pd.read_csv(tmp_csv, header=1)
new_data.drop_duplicates().to_csv(final_csv, mode='a', header=False)