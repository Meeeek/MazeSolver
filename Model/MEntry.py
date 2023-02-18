
class MEntry:

    def __init__(self, cp, left=None, right=None, up=None, down=None) -> None:
        self.cp = cp
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.status = 0 # 0 means unvisited, 1 means queued, 2 means visited, 3 means inaccessible, 4 means target, 5 is path
    
    def get_color(self):
        if self.status == 0:
            return (255,255,255)
        elif self.status == 1:
            return (255,191,0)
        elif self.status == 2:
            return (0,255,0)
        elif self.status == 4:
            return (255,0,0)
        elif self.status == 5:
            return (0,0,255)
        return (0,0,0)
