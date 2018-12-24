import math
import heapq
import sys
import numpy
import os
import random
import matplotlib.pyplot as plt

#algorithm is same as given in the slides of the lecture
#neighbour function: swap any 2 nodes in the path.

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
class TSP_class1():
#code for finding TSP 
		def __init__(self):
		    #print("bleg")
		    self.nodes_generated=0
		    self.index = 0


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
		    #print("the index we are looking at", self.index)
		    if(len(vertices)==1):
		        #print("the TSP path is A")
		        #print("the TSP cost is 0")
		        #print("the nodes generated in instance is 0")
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
		        #print("the TSP path is ", path[2]+start)
		        #print("the TSP cost is ",path[1]+distances[path[2][-1]][start])
		        return path[1]+distances[path[2][-1]][start]

dir = 'C:/Users/himan/Downloads/tsp_problems_ls/tsp_problems'
index1=0
inst_index=0
for cities in os.listdir(dir):
	#print("the folder now is ",cities)
	#index=0
	avg_list=[None]*10
	#inst_index=0
	p_14=[]
	p_15=[]
	p_16=[]
	avgqua_14=[]
	avgqua_15=[]
	avgqua_16=[]
	percentage_14=[]
	percentage_15=[]
	percentage_16=[]
	for instances in os.listdir(os.path.join(dir,cities)):
		steps_3_14=[]
		steps_3_15=[]
		steps_3_16=[]
		
		for i in range(0,100):
		
			avg_list=[None]*10
			fil = open(os.path.join(dir + '/'+str(cities)+'/', instances), 'r')
			#print("The instance is now", instances)
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


			class TSP_class():
				#code for finding TSP 
				def __init__(self):
					self.index=0
				#	print("hello")	        
				
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

				def generate_random_tour(self,vertices):
					copy = vertices[1:]
					random.shuffle(copy)
					vertices[1:] = copy 
					#print(vertices)

					str1 = ''.join(vertices)
					return(str1)

				def get_cost(self,path):
					cost=0
					#print(path)
					for i in range(0,len(path)-1):
						#print(path[i])
						#print(path[i+1])
						cost = cost + distances[path[i]][path[i+1]]

					#print(cost,path[0])
					cost=cost+distances[path[i+1]][path[0]]  #Adding the start node to the path
					#print(cost,path[0])
					return cost

				def swap(self,i,j,path):
					
					path = list(path)
					path[i], path[j] = path[j], path[i]
					return ''.join(path)

				def get_best_neighbours(self,path):
					best_cost=1e9
					best_path=''
					n=len(path)
					for i in range(1,n-1):
						for j in range(i+1,n):
							neighbouring_path=self.swap(i,j,path)
							neighbouring_path_cost=self.get_cost(neighbouring_path)
							print("The neighbors for path ",path,"genreated are", neighbouring_path)
							if(neighbouring_path_cost<best_cost):
								best_cost=neighbouring_path_cost
								best_path=neighbouring_path

					return best_cost,best_path



				def TSP_hill(self,index1):
					step_toreach_optimum=0
					#print("The index whhe are looking at",index1)
					#print("The instance is now", instances, "and the step_toreach_optimum is set to",step_toreach_optimum)
					random_start_node=self.generate_random_tour(vertices)
					current = random_start_node
					curr_cost=self.get_cost(current)
					# if(index1==2):
					# 	print("The array for cities 14 is ",steps_3_14)

					# if(index1==2):
					# 	print("The array for cities 15 is ",steps_3_15)
					# if(index1==2):
					# 	print("The array for cities 14 is ",steps_3_16)

					# if(index1==2):
					# 	index1=0
					while True:

						next_best_cost,next_best_path=self.get_best_neighbours(current)
						if(curr_cost <= next_best_cost):
							break
						else:
							step_toreach_optimum+=1
							curr_cost=next_best_cost
							current=next_best_path
					#print("The steps to reach the local optimum is ",step_toreach_optimum)

					if(int(cities)==14):
						steps_3_14.append(step_toreach_optimum)
						if(len(steps_3_14)==3):
							#print("The average for folder",cities, "and instance ",instances,"is", sum(steps_3_14)/len(steps_3_14))
							p_14.append(sum(steps_3_14)/len(steps_3_14))
							#inst_index+=1
							#print(steps_3_14)
							#print(p_14)
							if(len(p_14)==10):
								print("The average of number of steps for folder",cities, "and all the instance ","is", sum(p_14)/len(p_14))


					if(int(cities)==15):
						steps_3_15.append(step_toreach_optimum)
						if(len(steps_3_15)==3):
							#print("The average for folder",cities, "and instance ",instances,"is", sum(steps_3_15)/len(steps_3_15))
							p_15.append(sum(steps_3_15)/len(steps_3_15))
							#inst_index+=1
							#print(steps_3_15)
							#print(p_15)
							if(len(p_15)==10):
								print("The average of number of steps for folder",cities, "and all the instance ","is", sum(p_15)/len(p_15))
					if(int(cities)==16):
						steps_3_16.append(step_toreach_optimum)
						if(len(steps_3_16)==3):
							#print("The average for folder",cities, "and instance ",instances,"is", sum(steps_3_16)/len(steps_3_16))
							p_16.append(sum(steps_3_16)/len(steps_3_16))
							#inst_index+=1
							#print(steps_3_16)
							#print(p_16)
							if(len(p_16)==10):
								print("The average of number of steps for folder",cities, "and all the instance ","is", sum(p_16)/len(p_16))
					# #index1+=1
					# if(int(cities)==15):
					# 	steps_3_15.append(step_toreach_optimum)
					# if(int(cities)==16):
					# 	steps_3_16.append(step_toreach_optimum)

					s=TSP_class1()
					Cb=s.TSP(distances,vertices)
					#print("the folder is ",cities,"the instance is",instances," and the cost of best is ",Cb," the cost of ls is",curr_cost)
					if(int(cities)==14):
						if(curr_cost<=Cb):
						
							percentage_14.append(1)
						else:
							percentage_14.append(0)
					if(len(percentage_14)==100):
						#print("The percentage matrix")
						#print(percentage_14)
						print("The average of percentage where Cls=Clb for",cities ,"is",sum(percentage_14)/len(percentage_14))

					if(int(cities)==15):
						if(curr_cost<=Cb):
						
							percentage_15.append(1)
						else:
							percentage_15.append(0)
					if(len(percentage_15)==100):
						#print("The percentage matrix")
						#print(percentage_14)
						print("The average of percentage where Cls=Clb for",cities ,"is",sum(percentage_15)/len(percentage_15))

					if(int(cities)==16):
						if(curr_cost<=Cb):
						
							percentage_16.append(1)
						else:
							percentage_16.append(0)
					if(len(percentage_16)==100):
						#print("The percentage matrix")
						#print(percentage_14)
						print("The average of percentage where Cls=Clb for",cities ,"is",sum(percentage_16)/len(percentage_16))

					if(int(cities)==14):
						avgqua_14.append(curr_cost/Cb)
					#print(avgqua_14)
					if(len(avgqua_14)==100):
						print("The average of",cities," for quality of Best solution is ",sum(avgqua_14)/len(avgqua_14))
					if(int(cities)==15):
						avgqua_15.append(curr_cost/Cb)
					#print(avgqua_14)
					if(len(avgqua_15)==100):
						print("The average of",cities,"for quality of Best solution is ",sum(avgqua_15)/len(avgqua_15))
					if(int(cities)==16):
						avgqua_16.append(curr_cost/Cb)
					#print(avgqua_14)
					if(len(avgqua_16)==100):
						print("The average of",cities,"for quality of Best solution is ",sum(avgqua_16)/len(avgqua_16))
					return current,curr_cost

				#def TSP_hill_restart(self):



					



				#print(vertices)
				#print(distances)

			
			s=TSP_class()
			#print("Running ONLY hill clibming algorithm")
			best_path,best_cost=s.TSP_hill(index1)
			print("The best path is ",best_path+'A')
			print("The best cost is ",best_cost)
			index1+=1

