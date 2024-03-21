import math 
import random
from client_arucotag import ArUcoDetection as msg
import pygame


class rrt_graph:
    def __init__(self,start,goal,Map_dimentions,obsdim):
        (x,y) = start
        self.start = start
        self.goal = goal
        self.goalflag = False
        self.maph,self.mapw  = Map_dimentions
        self.x = []
        self.y = []
        self.parent = []
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)
        self.obstacles = msg.bounding_boxes
        self.obsdim = obsdim
        self.obsnum = len(msg.bounding_boxes)
        self.goalstate = None
        self.path = []
       

    def makeobs(self):
        obs  =[]
        for i in range(0,self.obsnum):
            rectangle = None
            startgoalcol= True
            while startgoalcol:
                center = self.obstacles[i]
                upper = [(center[0] - self.obsdim/2),(center[1] - self.obsdim/2)]
                rectangle  = pygame.rect(upper,(self.obsdim,self.obsdim))
                obs.append(rectangle)
        self.obstacles  = obs.copy()

                
    def add_node(self,x,y,n):
        self.x.insert(n.x)
        self.y.insert(n.y)

    def remove_node(self,n):
        self.x.pop(n)
        self.y.pop(n)

    def add_edge(self,child):
        self.parent.insert(child.parent)

    def remove_edge(self,n):
        self.parent.pop(n)
    
    def number_of_nodes():
        return len(self.x)
        
    def distance(self,n1,n2):
        (x1,y1) = (self.x[n1],self.y[n1])
        (x2,y2) = (self.x[n2],self.y[n2])
        px =(float(x1) - float(x2)) ** 2
        py =(float(y1) - float(y2)) ** 2
        return (px+py) ** 0.5
    
    def sampl_envr(self):
        x = int(random.uniform(0,self.mapw))
        y = int(random.uniform(0,self.maph))
        return x,y
    
    def nearest(self):
        pass
            

    def isfree(self):
        n = self.number_of_nodes()-1
        (x,y) = (self.x[n],self.y[n])
        obs = self.obstacles.copy()
        while len(obs) > 0:
            rectangle = obs.pop(0)
            if rectangle.collidepoint(x,y):
                self.remove_node(n)
                return False
        return True
    def cross_obstacle(self,x1,y1,x2,y2):
        obs = self.obstacles.copy()
        while(len(obs)>0):
            rectangle = obs.pop()
            for i in range(0,101):
                u = i/100
                x= x1*u + x2*(1-u)
                y= y1*u + y2*(1-u)
                if rectangle.collidepoint(x,y):
                    return True
        return False
        
    def connect(self,n1,n2):
        if self.cross_obstacle(self.x[n1],self.y[n1],self.x[n2],self.y[n2]):
            self.remove_node(n2)
            return False
        else:
            self.add_edge(n1.n2)
            return True
    def step():
        pass
    def path_to_goal():
        pass
    def get_path_coords():
        pass
    def bias():
        pass
    def expand():
        pass
    def cost():
        pass