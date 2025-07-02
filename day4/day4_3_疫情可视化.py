import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts

# 处理数据
f_us = open("csv/美国.txt","r",encoding="utf-8")
us_data = f_us.read()
f_rb = open("csv/日本.txt","r",encoding="utf-8")
rb_data = f_rb.read()
f_yd = open("csv/印度.txt","r",encoding="utf-8")
yd_data = f_yd.read()
#去掉开头不规范的

us_data = us_data.replace("jsonp_1629344292311_69436(","")
rb_data = rb_data.replace("jsonp_1629350871167_29498(","")
yd_data = yd_data.replace("jsonp_1629350745930_63180(","")
# 去掉结尾

us_data=us_data[:-2]
rb_data=rb_data[:-2]
yd_data=yd_data[:-2]
# json 转换为字典

us_dict=json.loads(us_data)
rb_dict=json.loads(rb_data)
yd_dict=json.loads(yd_data)
#取trend key

us_trend_data=us_dict["data"][0]["trend"]
rb_trend_data=rb_dict["data"][0]["trend"]
yd_trend_data=yd_dict["data"][0]["trend"]
# 取日期数据用于x轴，取2020年,切片！！！！

us_x_data=us_trend_data["updateDate"][:314]# x轴公共的

# 取确认数据用于y轴，取2020年

us_y_data=us_trend_data["list"][0]["data"][:314]
rb_y_data=rb_trend_data["list"][0]["data"][:314]
yd_y_data=yd_trend_data["list"][0]["data"][:314]
# 生成折线图

line=Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本",rb_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度",yd_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="2020年疫情确诊人数",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()
f_us.close()
f_rb.close()
f_yd.close()