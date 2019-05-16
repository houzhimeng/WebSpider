from pyecharts.charts import Bar, Pie
import pandas as pd

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


df = pd.read_csv('book.csv')
# print(df.loc[1:10,['书名','评论数']])
dfn = df.dropna(axis=0,subset=['书名'])  #删除书名为空的记录
dfn_comment = dfn.sort_values('评论数',ascending=False).head(20) #根据评论数排序，取前20本书信息
dfn_score = dfn[dfn['评论数']>200000].sort_values('评分',ascending=False).head(20) #根据评分排序，取前20本书信息
# print(dfn['书名'],dfn['评论数'])
# print(dfn.loc[:,['书名','评论数']])



dfn_book_name = dfn_comment['书名'].values.tolist() #把dataframe类型转成list类型
dfn_comment_nums = dfn_comment['评论数'].values.tolist()



dfn_book_name_score = dfn_score['书名'].values.tolist()
dfn_comment_score = dfn_score['评分'].values.tolist()
# print(dfn_book_name,dfn_comment_nums,dfn_comment_score)
# print(type(df),type(dfn))
# print(dfn.dtypes['出版日期']) #打印列类型

#日期类型转换
# dfn['出版日期'] = pd.to_datetime(dfn['出版日期'],errors='coerce') #转换成日期类型
# dfn['出版日期'] = dfn['出版日期'].dt.year #取年份
dfn_pub_date = dfn
dfn_pub_date['出版日期'] = pd.to_datetime(dfn['出版日期'],errors='coerce') #转换成日期类型
dfn_pub_date['出版日期']= dfn['出版日期'].dt.year #取年份

# print(dfn_pub_date)
#根据出版日期年份分组，取出每年出版书籍数量
dfn_n = dfn_pub_date.groupby(['出版日期'],as_index=False)['书名'].size().reset_index(name='count')

#过滤出版数量在10以下的年份
dfn_n = dfn_n[dfn_n['count']>10]
dfn_n_year = dfn_n['出版日期'].values.tolist()
dfn_n_count = dfn_n['count'].values.tolist()


#最多产的出版社
dfn_n_pub = dfn.groupby(['出版社'],as_index=False)['书名'].size().reset_index(name='count')
dfn_n_pub = dfn_n_pub.sort_values('count',ascending=False).head(10)
dfn_n_pub_name = dfn_n_pub['出版社'].values.tolist()
dfn_n_pub_count = dfn_n_pub['count'].values.tolist()









bar = Bar("豆瓣文学类图书", "评价数量")
bar.add_yaxis("评论数排名", dfn_book_name, dfn_comment_nums, is_more_utils=True)
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render('豆瓣文学评论数分析.html')  # 生成本地 HTML 文件
#

bar = Bar("豆瓣文学类图书", "评价数量")
bar.add_xaxis("评分排名", dfn_book_name_score, dfn_comment_score, is_more_utils=True)
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render('豆瓣文学书籍评分分析.html')  # 生成本地 HTML 文件


pie = Pie("各年份出版书籍数量分布饼图", title_pos='center')
pie.add("", dfn_n_year, dfn_n_count, radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left")
# pie.show_config()
pie.render('年份出版书籍数量分布饼图.html')



pie = Pie("各出版社出版书籍数量分布饼图", title_pos='center')
pie.add("", dfn_n_pub_name, dfn_n_pub_count, radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left")
# pie.show_config()
pie.render('各出版社出版书籍数量分布饼图.html')
