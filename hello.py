import genesis as gs
gs.init(backend=gs.gpu)

scene = gs.Scene(show_viewer=True)
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(file='franka_sim/franka_panda.xml'),
)

scene.build()

for i in range(1000):
    scene.step()