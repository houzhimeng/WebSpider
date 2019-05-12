import math

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Surface3D

def surface3d_base() -> Surface3D:
    def surface3d_data():
        for t0 in range(-60, 60, 1):
            y = t0 / 60
            for t1 in range(-60, 60, 1):
                x = t1 / 60
                if math.fabs(x) < 0.1 and math.fabs(y) < 0.1:
                    z = "-"
                else:
                    z = math.sin(x * math.pi) * math.sin(y * math.pi)
                yield [x, y, z]

    c = (
        Surface3D()
        .add(
            "",
            list(surface3d_data()),
            xaxis3d_opts=opts.Axis3DOpts(type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(import math

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Surface3D

def surface3d_base() -> Surface3D:
    def surface3d_data():
        for t0 in range(-60, 60, 1):
            y = t0 / 60
            for t1 in range(-60, 60, 1):
                x = t1 / 60
                if math.fabs(x) < 0.1 and math.fabs(y) < 0.1:
                    z = "-"
                else:
                    z = math.sin(x * math.pi) * math.sin(y * math.pi)
                yield [x, y, z]

    c = (
        Surface3D()
        .add(
            "",
            list(surface3d_data()),
            xaxis3d_opts=opts.Axis3DOpts(type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Surface3D-基本示例"),
            visualmap_opts=opts.VisualMapOpts(
                max_=3, min_=-3, range_color=Faker.visual_color
            ),
        )
    )
    return c
            title_opts=opts.TitleOpts(title="Surface3D-基本示例"),
            visualmap_opts=opts.VisualMapOpts(
                max_=3, min_=-3, range_color=Faker.visual_color
            ),
        )
    )
    return c