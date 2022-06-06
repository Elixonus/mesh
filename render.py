from math import tau
import cairo
from mesh import Mesh, QuadMesh, QuadCrossMesh
from vectors import Vector


camera_position = Vector(0, 0)
camera_zoom = 0.3

mesh = QuadCrossMesh((3, 3))
mesh.translate(Vector(-0.5, -0.5))


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
        context.move_to(link.nodes[0].point.x, link.nodes[0].point.y)
        context.line_to(link.nodes[1].point.x, link.nodes[1].point.y)
        context.set_source_rgb(0, 0, 0)
        context.set_line_width(0.04)
        context.set_line_cap(cairo.LINE_CAP_ROUND)
        context.stroke()

    for node in nodes:
        context.arc(node.point.x, node.point.y, 0.05, 0, tau)
        context.set_source_rgb(1, 1, 1)
        context.fill_preserve()
        context.set_source_rgb(0, 0, 0)
        context.set_line_width(0.02)
        context.stroke()
        context.arc(node.point.x, node.point.y, 0.025, 0, tau)
        context.set_source_rgb(0, 0, 0)
        context.fill()

    surface.write_to_png("render.png")

render(mesh)