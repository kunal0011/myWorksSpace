from typing import List

# You need to design a file system that supports the following operations:

# create(path: str, value: str): Creates a file at the specified path with the given value. If the path already exists as a file, update its content.
# read(path: str) -> str: Reads the content of the file at the specified path. If the path does not exist, return "".
# ls(path: str) -> List[str]: Lists all files and directories at the specified path. If path is a file, return a list containing just that file. If path is a directory, return a sorted list of all files and directories directly under it.


class FileSystem:
    def __init__(self):
        self.fs = {}

    def create(self, path: str, value: str) -> None:
        parts = path.strip('/').split('/')
        node = self.fs

        for part in parts[:-1]:
            if part not in node:
                node[part] = {}
            node = node[part]

        node[parts[-1]] = value

    def read(self, path: str) -> str:
        parts = path.strip('/').split('/')
        node = self.fs

        for part in parts[:-1]:
            if part not in node:
                return ""
            node = node[part]

        return node.get(parts[-1], "")

    def ls(self, path: str) -> List[str]:
        parts = path.strip('/').split('/')
        node = self.fs

        for part in parts:
            if part not in node:
                return []
            node = node[part]

        if isinstance(node, dict):
            return sorted(node.keys())
        else:
            return [parts[-1]]


fs = FileSystem()
fs.create("/a", "hello")     # Create file /a with content "hello"
print(fs.read("/a"))         # Output: "hello"
print(fs.ls("/"))            # Output: ["a"]
fs.create("/a/b", "world")   # Create file /a/b with content "world"
print(fs.read("/a/b"))       # Output: "world"
print(fs.ls("/a"))          # Output: ["b"]
print(fs.ls("/"))           # Output: ["a"]
