from Model.MEntry import MEntry

class Maze:

    x, y = 50, 50  # 50 by 50 squares

    def __init__(self) -> None:
        self.mObject = []

        # initialize entry list
        for i in range(self.x):
            newlentry = []
            for j in range(self.y):
                newlentry.append(MEntry((i,j)))
            self.mObject.append(newlentry)

        # initialize all left
        for i in range(1, self.x):
            for j in range(self.y):
                self.mObject[i][j].left = self.mObject[i-1][j]
                
        # initialize all right
        for i in range(0, self.x - 1):
            for j in range(self.y):
                self.mObject[i][j].right = self.mObject[i+1][j]

        # initialize all up
        for i in range(self.x):
            for j in range(1, self.y):
                self.mObject[i][j].up = self.mObject[i][j-1]

        # initailize all down
        for i in range(self.x):
            for j in range(self.y - 1):
                self.mObject[i][j].down = self.mObject[i][j+1]

    def clear_entries(self) -> None:
        self.__init__()
    
    # return the entry at cp
    def get(self, cp) -> MEntry:
        return self.mObject[cp[0]][cp[1]]
