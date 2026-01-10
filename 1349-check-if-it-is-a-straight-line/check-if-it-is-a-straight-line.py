class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        dX = x1-x0
        dY = y1-y0
        
        
        for l in range(2,len(coordinates)):
            curr_x, curr_y = coordinates[l]
            dx = curr_x-x0
            dy = curr_y-y0
            if dX*dy != dY*dx:
                return False
        
        return True

        