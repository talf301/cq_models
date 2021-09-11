import cadquery as cq
from cadquery import exporters
res = cq.Workplane().box(30,20,10) \
    .edges("|Z").fillet(5) \
    #.faces(">Z").hole(25)
    
peephole = cq.Workplane().circle(5).extrude(3.5).translate([0,0,1.5])
magnet = cq.Workplane().circle(6).extrude(3).translate([0,0,1])
#res = res.cut(peephole.union(magnet))
res = res.cut(magnet)
exporters.export(res, "magnet_test.stl")