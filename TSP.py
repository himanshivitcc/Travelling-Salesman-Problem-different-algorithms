# coding: utf-8
# In[16]:
import math
import heapq
import sys
import numpy
import os
import matplotlib.pyplot as plt

### Algo :
#1) Calculate the distances between each cities in the form of dict A:{B:,C:,D:} and so on
#2) Add A (start ) to the frontier[PRIORIRTY Queue] .
#3)while:
#    pop frontier.
#    calculate the path and f(n) to remaining cities . eg pop AB, calculate paths(ABC, ABD)
#                                                    , costs (Euclidien (AB+BC), Euclidien(AB+BD))
#                                                    , f(n)=g(n)(ALready calculated a s 2nd param+h(n)= MST of remaining cities)
#    if:
#        all cities are visited . break
#4) print the popped path + start node (including the corresponding distances)

Avg_gen=[None]*16
gen=[None]*10
dir = 'C:/Users/himan/Downloads/tsp_problems/tsp_problems'
for cities in os.listdir(dir):
    if(cities==str(36)):
        continue
    print("the folder now is ",cities)
    index=0
    avg_list=[None]*10
    for instances in os.listdir(os.path.join(dir,cities)):
        
        print("the instance now is ",instances)
        fil = open(os.path.join(dir + '/'+str(cities)+'/', instances), 'r')
        nodes_generated=0
        
#for filename in os.listdir('C:/Users/himan/Downloads/tsp_problems/tsp_problems/'):
#    for i in range(1,10):
#        fil = open(os.path.join('tsp_problems/i', filename), 'r')
#fil = open( "C:/Users/himan/Downloads/tsp_problems/tsp_problems/16/instance_2.txt", 'r' )
        st = fil.read()
        data = st.split('\n')
        cities = int( data[0] )
        #print(data)
        #print(cities)
        #vertices=data.spl
        graph=data[1:cities+1]
        #print(graph)
        distances={}
        vertices=[]
        generate=[]

        #code for calculating MST
        class Graph(): 

            def __init__(self, vertices): 
                self.V = vertices 
                self.graph = [[0 for column in range(vertices)]  
                            for row in range(vertices)] 


            def printMST(self, parent): 
                cost=0
                #print("Edge \tWeight")
                for i in range(1,self.V): 
                    #print(parent[i],"-",i,"\t",self.graph[i][ parent[i] ] )
                    cost=cost+self.graph[i][ parent[i] ]
                #print("the cost os mst is",cost)
                return(cost)



            def minKey(self, key, mstSet): 

                # Initilaize min value 
                min = 1e9

                for v in range(self.V): 
                    if key[v] < min and mstSet[v] == False: 
                        min = key[v] 
                        min_index = v 

                return min_index 


            def primMST(self): 
                min = 1e9

                key = [min] * self.V 
                parent = [None] * self.V 
                key[0] = 0 
                mstSet = [False] * self.V 

                parent[0] = -1 

                for cout in range(self.V): 

                    u = self.minKey(key, mstSet) 

                    mstSet[u] = True
                    for v in range(self.V): 
                        if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                                key[v] = self.graph[u][v] 
                                parent[v] = u 

                cost=self.printMST(parent) 
                return(cost)

        #code End for calculating MST
        class TSP_class():
        #code for finding TSP 
            def __init__(self,index):
                #print("bleg")
                self.nodes_generated=0
                self.index = index
            def find_euclidean( x1, y1, x2, y2 ):
                return math.sqrt( (x1-x2)**2 + (y1-y2)**2)

            for n1 in graph:
                vertex1,x1,y1=n1.split(' ')
                vertices.append(vertex1)
                distances[vertex1]={}
                x1,y1=int(x1),int(y1)
                for n2 in graph:
                    vertex2,x2,y2=n2.split(' ')
                    x2,y2=int(x2),int(y2)
                    if n1==n2:
                        continue
                    distances[vertex1][vertex2]=find_euclidean(x1,y1,x2,y2)
            #print(distances)
            #print(vertices)

            def mst(self,cities_remaining):
                #print("calculating mst for ", cities_remaining)
                graph_size=len(cities_remaining)
                #print("the graph size for mst  ", graph_size)
                g=Graph(graph_size)
                #x=numpy.empty(len(cities_remaining))
                for i in range(0,graph_size):
                    for j in range(0,graph_size):
                        #print("i and j", i , j)
                        if(i==j):
                            #x[i][j]=0
                            g.graph[i][j]=0
                            continue
                        #print("the distances in mst function are",distances[cities_remaining[i]][cities_remaining[j]])
                        g.graph[i][j]=distances[cities_remaining[i]][cities_remaining[j]]
                        #g.graph[i][j]=2
                #print("the graph now is ",g.graph)
                mst_value=g.primMST(); 
                #print("the mst of the remaining_cities is",mst_value)
                return(mst_value)



            def total_f_nd_h(self,path,last_vertex,vertices,frontier,cost_curr_path):
                #print(self.nodes_generated)
                cities_remaining=[]
                for each_city in vertices:
                    cities_remaining.append(each_city)
                #print("cost",distances[last_vertex][remaining_vertex])
                #print("path now",path+remaining_vertex)
                #print("length of path",len(path))
                #x=['A','B','C','D']

                for i in range(0,len(path)):
                    #print("removing ",path[i])
                    cities_remaining.remove(path[i])
                #print("cities_remaining",cities_remaining)
                h=self.mst(cities_remaining)
                for each_city in cities_remaining:
                    new_path=path+each_city
                    f=cost_curr_path+distances[last_vertex][each_city] + h
                    cost=cost_curr_path+distances[last_vertex][each_city]
                    heapq.heappush(frontier,(f,cost,new_path))
                    self.nodes_generated=self.nodes_generated+1
                    #print(nodes_generated)
                    if((len(new_path)==len(vertices)) and (len(cities_remaining)==0)):
                        return new_path


            def TSP(self,distances, vertices):
                print("the index we are looking at", self.index)
                if(len(vertices)==1):
                    print("the TSP path is A")
                    print("the TSP cost is 0")
                    print("the nodes generated in instance is 0")
                    avg_list[self.index]=0
                    self.index=self.index+1
                    #print("avg_list is",avg_list)
                    #if(self.index==9):
                    #    return avg_list
                else:
                    frontier=[]
                    heapq.heapify(frontier)
                    start=vertices[0]
                    #frontier(h(n),cost_path,path)
                    heapq.heappush(frontier,(0,0,start) )
                    remaining_cities=[]
                    for each_city in vertices:
                        remaining_cities.append(each_city)
                    #remaining_cities=
                    #print("the frontier is ",frontier)
                    while True:
                        path = heapq.heappop(frontier)
                        #print("the path popperd is ", path, "and the length is ", len(path[2]))
                        if(len(path[2])==len(vertices)):
                            break
                        cost_curr_path=path[1]
                        last_vertex=path[2][len(path[2])-1]
                        #print(last_vertex[-1])
                        length_path=len(path[2])
                          #for i in range(0,length_path):
                        #remaining_cities.remove(path[1][len(path[1])-1])
                        #print(remaining_cities)
                        #for remaining_vertex in remaining_cities:
                        path_new=self.total_f_nd_h(path[2],last_vertex,vertices,frontier,cost_curr_path)
                                #heapq.heappush(frontier,(path,cost) )

                        #print("the frontier is ",frontier)
                        if(path_new is None):
                            continue
                        if(len(path_new)==len(vertices)):
                            break

                    #path = heapq.heappop(frontier)
                    #print((path[0][len(path[0])-1]))
                    #print(remaining_cities)
                    print("the TSP path is ", path[2]+start)
                    print("the TSP cost is ",path[1]+distances[path[2][-1]][start])
                    print("the nodes generated in instance",self.nodes_generated)
                    avg_list[self.index]=self.nodes_generated
                    self.index=self.index+1

               # print("avg_list is",avg_list)
                if(self.index==10):
                    print("avg_list is",avg_list)
                    list_avg=sum(avg_list)/len(avg_list)
                    print("The average for city",cities," is ", list_avg)
                    Avg_gen[cities-1]=list_avg
                    #plt.plot(200,100)
                    #plt.show()
    


        #nodes_generated=0
        s=TSP_class(index)
        s.TSP(distances,vertices)
        index=index+1
        #print(path)
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#print("The average for 16 is ",Avg_gen)
plt.scatter(x,Avg_gen)
plt.xlabel("Number of cities")
plt.ylabel("Average")
plt.show()

