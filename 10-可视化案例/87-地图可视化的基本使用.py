# 演示地图可视化的基本使用

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()

# 准备数据
data = [
    ("北京市",99),
    ("上海市",199),
    ("广东省",299),
    ("江西省",399),
    ("浙江省",499),
]

# 添加数据
map.add("测试地图",data,"china")


# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1, "max":9, "label":"1-9", "color": "#CCFFFF"},
            {"min":10, "max":90, "label":"10-9", "color": "#FF66666"},
            {"min":100, "max":500, "label":"100-500", "color": "#990033"}
        ]
    )
)


# 绘图
map.render()
