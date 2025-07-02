from pyecharts.charts import Map
from pyecharts.options import *
import json

cn_f = open("csv/疫情.txt", "r", encoding="utf-8")
cn_json = cn_f.read()
cn_f.close()
cn_dict = json.loads(cn_json)
cn_dict = cn_dict["areaTree"][0]["children"][3]["children"]
list_cn = []
# cn_dict[i]["total"]["confirm"]

for i in range (len(cn_dict)):
    list_cn.append((cn_dict[i]["name"]+"市",cn_dict[i]["total"]["confirm"]))

map = Map()
map.add("河南省疫情地图", list_cn, "河南")
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "lable": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000-4999人", "color": "#FF6699"},
            {"min": 5000, "max": 9999, "lable": "5000-9999人", "color": "#CC6666"},
            {"min": 10000, "max": 99999, "lable": "10000-9999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+人", "color": "#990033"},

        ]

    )
)
map.render("henan.html")