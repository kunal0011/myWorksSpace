from typing import List


class FileSystem:
    def __init__(self):
        # Root directory is represented as an empty dictionary
        self.root = {}

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)

        # If the path is a file, return its name
        if isinstance(node, str):
            return [path.split('/')[-1]]

        # If it's a directory, return its contents in lexicographical order
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path, create_if_not_exist=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split('/')
        file_name = dirs.pop()

        # Traverse the path to get to the parent directory of the file
        node = self._traverse('/'.join(dirs), create_if_not_exist=True)

        # If the file already exists, append the content
        if file_name in node:
            node[file_name] += content
        else:
            node[file_name] = content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)

        # Since file is represented by a string, just return the content
        return node

    def _traverse(self, path: str, create_if_not_exist: bool = False):
        # Start from the root directory
        node = self.root

        if path == "/":
            return node

        # Split the path into directories
        dirs = path.split('/')[1:]

        for directory in dirs:
            if directory not in node:
                if create_if_not_exist:
                    # Create directory if it doesn't exist
                    node[directory] = {}
                else:
                    return None
            node = node[directory]

        return node

# Test cases


def test_file_system():
    fs = FileSystem()

    # Test case 1: mkdir and ls
    fs.mkdir("/a/b/c")
    assert fs.ls("/") == ["a"], "Test case 1 failed"

    # Test case 2: addContentToFile and ls
    fs.addContentToFile("/a/b/c/d", "hello")
    assert fs.ls("/a/b/c") == ["d"], "Test case 2 failed"

    # Test case 3: readContentFromFile
    assert fs.readContentFromFile("/a/b/c/d") == "hello", "Test case 3 failed"

    # Test case 4: append content to file
    fs.addContentToFile("/a/b/c/d", " world")
    assert fs.readContentFromFile(
        "/a/b/c/d") == "hello world", "Test case 4 failed"

    print("All test cases passed!")


# Run the tests
test_file_system()
