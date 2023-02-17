
class MEntry:
    def __init__(self, left: None, right: None, up: None, down: None) -> None:
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.status = 0 # 0 means unvisited, 1 means queued, 2 means visited, 3 means inaccessible