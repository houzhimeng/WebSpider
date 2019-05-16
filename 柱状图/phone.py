# -*-coding:utf-8-*-
# 柱状图

import matplotlib.pyplot as plt
import time

mobile_176xxxx4617 = [6.33, 24.1, 40.7, 47.9, 31.9, 31.4, 41.7, 46.4, 38.9, 39, 48, 47.4]
mobile_155xxxx9617 = [41.4, 36.5, 16.4, 16.6, 16.1, 16, 16, 31.2, 20, 16, 22.1, 16]
mobile_173xxxx9636 = [9.4, 9.1, 9.7, 9.1, 9.2, 9, 9, 9.1, 39, 9, 19.22, 19]
time = ['2018.4', '2018.5', '2018.6', '2018.7', '2018.8', '2018.9', '2018.10', '2018.11', '2018.12', '2019.1', '2019.2', '2019.3']

time = data_source.time

time_len = len(time)
xtick_index = range(int(time_len))width:长条形宽度，默认值0.8

plt.figure(figsize=(12, 8))  # 建立图形

"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
alpha:透明度
color:颜色
label:标签，为后面设置legend准备
"""
bar1 = plt.bar([i - 0.2 for i in xtick_index], mobile_176xxxx4617, width=0.2,
               alpha=0.8, label='176xxxx4617')  # 第一个图

bar2 = plt.bar([i for i in xtick_index], mobile_155xxxx9617, width=0.2,
               alpha=0.8, label='155xxxx9617')  # 第二个图

bar3 = plt.bar([i + 0.2 for i in xtick_index], mobile_173xxxx9636, width=0.2,
               alpha=0.8, label='173xxxx9636')  # 第三个图

plt.xticks(xtick_index, time)  # 设置x轴刻度显示值
plt.ylim(0, 65)  # y轴的范围
plt.title('我的话费统计')  # 标题
plt.xlabel('时间')  # x轴的标签
plt.ylabel('话费金额（单位：元）')  # y轴的标签
plt.legend()  # 设置图例

'''
get_height:获取值
get_x：获取x轴的位置
get_width:获取图形的宽度
text(x,y,s,fontsize,ha,va)
    x,y:表示坐标值上的值
    s:表示说明文字
    fontsize:表示字体大小
    ha：垂直显示方式{'centee':'中心', 'right':'右', 'left':'左'}
    va：水平显示方式{'center':'中心', 'top':'下', 'bottom':'上', 'baseline':'基线'} 
'''

for rect in bar1:
    height = rect.get_height()  # 获得bar1的高度
    plt.text(rect.get_x() + rect.get_width() / 2, height + 3, str(height), fontsize=6, ha="center", va="bottom")
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 3, str(height), fontsize=6, ha="center", va="bottom")
for rect in bar3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 3, str(height), fontsize=6, ha="center", va="bottom")


def show_plt():
    plt.show()