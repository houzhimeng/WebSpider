import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl  #用于修改x轴坐标
plt.style.use('ggplot')   #默认绘图风格很难看，替换为好看的ggplot风格
fig = plt.figure(figsize=(8,5))   #设置图片大小
colors1 = '#6D6D6D'  #设置图表title、text标注的颜色
columns = ['index', 'image', 'title', 'actor', 'time','score']  #设置表头
df = pd.read_csv('猫眼top100.csv',encoding = "utf-8",header = None,names =columns,index_col = 'index')  #打开表格
# index_col = 'index' 将索引设为index
df_score = df.sort_values('score',ascending = False)  #按得分降序排列
name1 = df_score.title[:10]      #x轴坐标
score1 = df_score.score[:10]    #y轴坐标
plt.bar(range(10),score1,tick_label = name1)  #绘制条形图，用range()能搞保持x轴正确顺序
plt.ylim ((9,9.8))  #设置纵坐标轴范围
plt.title('电影评分最高top10',color = colors1) #标题
plt.xlabel('电影名称')      #x轴标题
plt.ylabel('评分')          #y轴标题
# 为每个条形图添加数值标签
for x,y in enumerate(list(score1)):
    plt.text(x,y+0.01,'%s' %round(y,1),ha = 'center',color = colors1)
    pl.xticks(rotation=270)   #x轴名称太长发生重叠，旋转为纵向显示
    plt.tight_layout()    #自动控制空白边缘，以全部显示x轴名称
    # plt.savefig('电影评分最高top10.png')   #保存图片
    plt.show()