from __future__ import annotations
from math import sqrt
from vectors import Vector


class Mesh:
    nodes: list[Node]
    links: list[Link]

    def __init__(self, nodes: list[Node], links: list[Link]) -> None:
        self.nodes = nodes
        self.links = links

    def translate(self, vector: Vector) -> None:
        for node in self.nodes:
            node.point += vector

    def scale(self, vector: Vector) -> None:
        for node in self.nodes:
            node.point.x *= vector.x
            node.point.y *= vector.y


class QuadMesh(Mesh):
    def __init__(self, grid: tuple[int, int]) -> None:
        nodes_quad = []
        for x in range(grid[0] + 1):
            nodes_quad.append([])
            for y in range(grid[1] + 1):
                node = Node(Vector(x / grid[0], y / grid[1]))
                nodes_quad[x].append(node)
        nodes = [node for nodes_buffer in nodes_quad for node in nodes_buffer]
        links = []
        for x in range(grid[0]):
            for y in range(grid[1] + 1):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x + 1][y]))
                links.append(link)
        for x in range(grid[0] + 1):
            for y in range(grid[1]):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x][y + 1]))
                links.append(link)
        super().__init__(nodes, links)


class QuadCrossMesh(Mesh):
    def __init__(self, grid: tuple[int, int]) -> None:
        nodes_quad = []
        for x in range(grid[0] + 1):
            nodes_quad.append([])
            for y in range(grid[1] + 1):
                node = Node(Vector(x / grid[0], y / grid[1]))
                nodes_quad[x].append(node)
        nodes = [node for nodes_buffer in nodes_quad for node in nodes_buffer]
        links = []
        for x in range(grid[0]):
            for y in range(grid[1] + 1):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x + 1][y]))
                links.append(link)
        for x in range(grid[0] + 1):
            for y in range(grid[1]):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x][y + 1]))
                links.append(link)
        for x in range(grid[0]):
            for y in range(grid[1]):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x + 1][y + 1]))
                links.append(link)
                link = Link(nodes=(nodes_quad[x][y + 1], nodes_quad[x + 1][y]))
                links.append(link)
        super().__init__(nodes, links)


class TriMesh(Mesh):
    def __init__(self, grid: tuple[int, int]) -> None:
        nodes_quad = []
        for x in range(grid[0] + 1):
            nodes_quad.append([])
            for y in range(grid[1] + 1):
                node = Node(Vector((x + 0.5 * (y % 2)) / grid[0], y * sqrt(3) / (2 * grid[1])))
                nodes_quad[x].append(node)
        nodes = [node for nodes_buffer in nodes_quad for node in nodes_buffer]
        links = []
        for x in range(grid[0]):
            for y in range(grid[1] + 1):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x + 1][y]))
                links.append(link)
        for x in range(grid[0] + 1):
            for y in range(grid[1]):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x][y + 1]))
                links.append(link)
        for x in range(grid[0]):
            for y in range(grid[1]):
                if y % 2 == 0:
                    link = Link(nodes=(nodes_quad[x][y + 1], nodes_quad[x + 1][y]))
                else:
                    link = Link(nodes=(nodes_quad[x][y], nodes_quad[x + 1][y + 1]))
                links.append(link)
        super().__init__(nodes, links)


class HexMesh(Mesh):
    def __init__(self, grid: tuple[int, int]) -> None:
        mesh = TriMesh(grid)
        nodes = mesh.nodes
        links = mesh.links
        super().__init__(nodes, links)


class Node:
    point: Vector

    def __init__(self, point: Vector) -> None:
        self.point = point


class Link:
    nodes: tuple[Node, Node]

    def __init__(self, nodes: tuple[Node, Node]) -> None:
        self.nodes = nodes
