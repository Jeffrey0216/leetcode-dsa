class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        folders = path.split("/")
        for folder in folders:
            if folder == "" or folder == ".":
                continue
            elif folder == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        return "/" + "/".join(stack)