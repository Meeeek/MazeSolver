
# class for a square
class Block():

    def __init__(self, x, y, width) -> None:
        # coords are center based
        self.x, self.y = x, y
        self.width = width

    def within(self, p) -> bool:
        return False

    # return top left point
    def get_tl(self):
        return (self.x - self.width//2, self.y - self.width//2)