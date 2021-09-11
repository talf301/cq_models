import cadquery as cq
orig = cq.importers.importStep('C:\\Users\\Tal\\Downloads\\PinecilBottom.step')
# Remove little dots
res = cq.Workplane().box(20,10,10).translate([32,80,7])
shaver = res.cut(orig)
stripped = orig.cut(shaver.translate([20,0,0]))

# Clean up underlying mesh
cover = orig.intersect(res)
covered = stripped.union(cover.translate([20,0,0]))

# Remove Allen key holder
res = cq.Workplane().box(40,10,10).translate([-20,58,7])
shaver = res.cut(covered)
stripped = covered.cut(shaver.translate([70,0,0]))

# Remove Clasp bumps
res = cq.Workplane().box(40,10,10).translate([0,90,12])
shaver = res.cut(stripped)
stripped = stripped.cut(shaver.translate([-25,0,0]))
stripped = stripped.cut(shaver.translate([75,0,0]))
show_object(stripped)