import cairo
from mesh import Mesh, QuadMesh
from vectors import Vector


camera_position = Vector(0, 0)
camera_zoom = 1

mesh = QuadMesh((3, 3))

def render(mesh: Mesh) -> None:
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
    context = cairo.Context(surface)
    context.scale(1000, 1000)
    context.rectangle(0, 0, 1, 1)
    context.set_source_rgb(1, 1, 1)
    context.fill()
    context.translate(0.5, 0.5)
    context.scale(1, -1)
    context.scale(camera_zoom, camera_zoom)
    context.translate(-camera_position.x, -camera_position.y)

    nodes = mesh.nodes
    links = mesh.links

    for link in links:
        context.move_to(link.nodes[0].point.x, link.nodes[1].point.y)
        context.move_to(link.nodes[0].point.x, link.nodes[1].point.y)

    surface.write_to_png("render.png")

render(mesh)