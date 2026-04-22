from abc import ABC, abstractmethod


# Component
class Node(ABC):
    @abstractmethod
    def total_size(self):
        pass


# Composite
class Folder(Node):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)

    def total_size(self):
        return sum(child.total_size() for child in self.children)


# Leaf
class File(Node):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def total_size(self):
        return self.size


def main():
    root = Folder("docs")
    root.add(File("readme.txt", 4))
    images = Folder("images")
    images.add(File("logo.png", 20))
    root.add(images)
    print(root.total_size())


if __name__ == "__main__":
    main()