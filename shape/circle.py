class Circle:
    def __init__(self,centre,rad):
        self.centre= centre
        self.radius= rad
    def __contains__(self, point):
        if (abs(self.centre[0]-point[0])**2 + abs(self.centre[1]-point[1])**2)< self.radius**2:
            return True
        return False 
        
   