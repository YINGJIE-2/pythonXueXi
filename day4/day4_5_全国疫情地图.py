from pyecharts.charts import Map
from pyecharts.options import *
import json

cn_f = open("csv/疫情.txt", "r", encoding="utf-8")
cn_json = cn_f.read()
cn_dict = json.loads(cn_json)
cn_dict = cn_dict["areaTree"][0]["children"]
cn_dict = cn_dict[:34]
list_cn = []
# cn_dict[i]["total"]["confirm"]

for i in range(34):
    list_cn.append((cn_dict[i]["name"]+"省", cn_dict[i]["total"]["confirm"]))
print(list_cn)
map = Map()
map.add("各省份确诊人数", list_cn, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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
map.render("cn.html")
cn_f.close()
