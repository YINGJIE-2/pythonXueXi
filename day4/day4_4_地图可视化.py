from charset_normalizer.md import is_punctuation
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map=Map()

data=[
    ("北京市",78),
    ("上海市",131),
    ("江苏省",313),
    ("重庆市",311),
    ("台湾省",678),
    ("浙江省",896),
    ("山东省",44),
    ("福建省",378),
]

map.add("地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"FF6666"},
            {"min":100,"max":500,"label":"100-500","color":"990033"},
        ],
                                 )

)
map.render("cn.html")