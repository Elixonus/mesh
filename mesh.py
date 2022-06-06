from __future__ import annotations
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
        for x in range(grid[0] - 1):
            for y in range(grid[1]):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x + 1][y]))
                links.append(link)
        for x in range(grid[0]):
            for y in range(grid[1] - 1):
                link = Link(nodes=(nodes_quad[x][y], nodes_quad[x][y + 1]))
                links.append(link)
        super().__init__(nodes, links)


class Node:
    point: Vector

    def __init__(self, point: Vector) -> None:
        self.point = point


class Link:
    nodes: tuple[Node, Node]

    def __init__(self, nodes: tuple[Node, Node]) -> None:
        self.nodes = nodes
