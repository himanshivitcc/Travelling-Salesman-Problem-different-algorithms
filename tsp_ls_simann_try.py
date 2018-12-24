import math
import heapq
import sys
import numpy
import os
import random 
import matplotlib.pyplot as plt
import time

dir = 'C:/Users/himan/Downloads/tsp_problems_ls/tsp_problems'
average_time_14_inst1 = 0


plot_avg_14_1=[]
plot_avg_14_2=[]
plot_avg_15_1=[]
plot_avg_15_2=[]
plot_avg_16_1=[]
plot_avg_16_2=[]

plot_avgperf_14_1=[]
plot_avgperf_14_2=[]
plot_avgperf_15_1=[]
plot_avgperf_15_2=[]
plot_avgperf_16_1=[]
plot_avgperf_16_2=[]

time_3_14_inst1=[]
time_3_15_inst1=[]
time_3_16_inst1=[]
time_3_14_inst2=[]
time_3_15_inst2=[]
time_3_16_inst2=[]

perf_3_14_inst1=[]
perf_3_14_inst2=[]
perf_3_15_inst1=[]
perf_3_15_inst2=[]
perf_3_16_inst1=[]
perf_3_16_inst2=[]
for cities in range(14, 17):
	print("the folder now is ",cities)
	index=0
	avg_list=[None]*10

	for instances in range(1,3):
		
		for x in range(0,100):
			print("The i right now is",x)
			instance = 'instance_' + str(instances) + '.txt'
			fil = open(os.path.join(dir + '/'+str(cities)+'/', instance), 'r')
			print("The instance is now", instance)
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
				#def __init__(self):
				#   self.index=0
				#   print("hello")          
				
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
					print(vertices)

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
							if(neighbouring_path_cost<best_cost):
								best_cost=neighbouring_path_cost
								best_path=neighbouring_path

					return best_cost,best_path

				def generate_random_neighbour(self,path):
					n=len(path)
					x=random.sample(range(1, n), 2)
					random_neighbour=self.swap(x[0],x[1],path)
					#print(random_neighbour)
					return random_neighbour






				def TSP_hill(self):
					count=0
					random_start_node=self.generate_random_tour(vertices)
					current = random_start_node
					curr_cost=self.get_cost(current)


					while True:
						next_best_cost,next_best_path=self.get_best_neighbours(current)
						if(curr_cost <= next_best_cost):
							break
						else:
							count+=1
							curr_cost=next_best_cost
							current=next_best_path
					print("The number of states generates are ",count)
					return current,curr_cost

				def TSP_hill_restart(self):
					random_restart=0

					if(int(cities)==14 and instances == "instance_1.txt" ):
						while True:
						
							if(random_restart > 100):
								print("no solution")
								break
							best_path,best_cost=self.TSP_hill()
							print("The path generated is ",best_path)
							print("The cost generated is ",type(best_cost))
								#if(best_cost=="AMBFCDKLEGNIHJ"):
							print("hellloooo")
							if(math.floor(best_cost)<=(318*1.01)):
								print("Found")
								break
							else:
								random_restart+=1
								continue
					  
						print("The number of random restart is ",random_restart)
					#random_restart=0

					if(int(cities)==14 and instances == "instance_2.txt" ):
						while True:
						
							if(random_restart > 100):
								print("no solution")
								break
							best_path,best_cost=self.TSP_hill()
							print("The path generated is ",best_path)
							print("The cost generated is ",type(best_cost))
								#if(best_cost=="AMBFCDKLEGNIHJ"):
							print("hellloooo")
							if(math.floor(best_cost)<=(324*1.01)):
								print("Found")
								break
							else:
								random_restart+=1
								continue
												 

						print("The number of random restart is ",random_restart)
						#random_restart=0

					if(int(cities)==15 and instances == "instance_1.txt" ):
						while True:
						
							if(random_restart > 100):
								print("no solution")
								break
							best_path,best_cost=self.TSP_hill()
							print("The path generated is ",best_path)
							print("The cost generated is ",type(best_cost))
								#if(best_cost=="AMBFCDKLEGNIHJ"):
							print("hellloooo")
							if(math.floor(best_cost)<=(315.07*1.01)):
								print("Found")
								break
							else:
								random_restart+=1
								continue
												 

						print("The number of random restart is ",random_restart)

					if(int(cities)==15 and instances == "instance_2.txt" ):
						while True:
						
							if(random_restart > 100):
								print("no solution")
								break
							best_path,best_cost=self.TSP_hill()
							print("The path generated is ",best_path)
							print("The cost generated is ",type(best_cost))
								#if(best_cost=="AMBFCDKLEGNIHJ"):
							print("hellloooo")
							if(math.floor(best_cost)<=(318*1.01)):
								print("Found")
								break
							else:
								random_restart+=1
								continue
												 

						print("The number of random restart is ",random_restart)

					if(int(cities)==16 and instances == "instance_1.txt" ):
						while True:
						
							if(random_restart > 100):
								print("no solution")
								break
							best_path,best_cost=self.TSP_hill()
							print("The path generated is ",best_path)
							print("The cost generated is ",type(best_cost))
								#if(best_cost=="AMBFCDKLEGNIHJ"):
							print("hellloooo")
							if(math.floor(best_cost)<=(404*1.01)):
								print("Found")
								break
							else:
								random_restart+=1
								continue
												 

						print("The number of random restart is ",random_restart)

					if(int(cities)==16 and instances == "instance_2.txt" ):
						while True:
						
							if(random_restart > 100):
								print("no solution")
								break
							best_path,best_cost=self.TSP_hill()
							print("The path generated is ",best_path)
							print("The cost generated is ",type(best_cost))
								#if(best_cost=="AMBFCDKLEGNIHJ"):
							print("hellloooo")
							if(math.floor(best_cost)<=(354.55*1.01)):
								print("Found")
								break
							else:
								random_restart+=1
								continue
												 

						print("The number of random restart is ",random_restart)

				def TSP_simulatedAnn(self):
					performance=0
					current_state=self.generate_random_tour(vertices)
					print("the current state is",current_state)
					T=10000
					start=time.time()
					while(T>0):
						curr_cost=self.get_cost(current_state)
						next_state=self.generate_random_neighbour(current_state)
						next_cost=self.get_cost(next_state)
						dE= curr_cost-next_cost
						if(dE>0):
							current_state=next_state
						else:
							frac= -dE/T
							p=math.exp(frac)
							checkpoint=random.randint(1,100)
							if(checkpoint<p):
								current_state=next_state
						T=T-1
					end=time.time()
					time_taken=(end-start)*10

					if(int(cities)==14 and instance == "instance_1.txt" ):  
						#print("bellooo")     
						performance = curr_cost/318
						time_3_14_inst1.append(time_taken)
						perf_3_14_inst1.append(performance)

					if(int(cities)==14 and instance == "instance_2.txt" ):       
						performance = curr_cost/324
						time_3_14_inst2.append(time_taken)
						perf_3_14_inst2.append(performance)
							   
					if(int(cities)==15 and instance == "instance_1.txt" ):
						performance = curr_cost/315.07
						time_3_15_inst1.append(time_taken)
						perf_3_15_inst1.append(performance)
						
					if(int(cities)==15 and instance == "instance_2.txt" ):
						performance = curr_cost/318
						time_3_15_inst2.append(time_taken)
						perf_3_15_inst2.append(performance)

					if(int(cities)==16 and instance == "instance_1.txt" ):
						performance = curr_cost/404
						time_3_16_inst1.append(time_taken)
						perf_3_16_inst1.append(performance)

					if(int(cities)==16 and instance == "instance_2.txt" ):
						performance = curr_cost/353
						time_3_16_inst1.append(time_taken)
						perf_3_16_inst1.append(performance)

					print("The value of performance for", cities,"and", instance, "is", performance)
					print("The value of time_taken for", cities,"and", instance, "is", time_taken)

					# if(int(cities)==16 and instance == "instance_2.txt" ):
					# 	performance = curr_cost/354.55
					# 	time_3_16_inst2.append(time_taken)
					# 	perf_3_16_inst2.append(performance)
					# 	print("The value of x is ",x)
					# 	print("The performan for city",cities,"and instance",instance,"is",performance)
					# 	print("The length of time_3_14_inst1 is",time_3_14_inst1)

					if(len(time_3_14_inst1)==100):
						average_time_14_inst1=sum(time_3_14_inst1)/len(time_3_14_inst1)
						average_perf_14_inst1=sum(perf_3_14_inst1)/len(perf_3_14_inst1)
						print("The average for time taken folder",cities,"and instance is",instance, "time_3_14_inst1", average_time_14_inst1)
						plot_avg_14_1.append(average_time_14_inst1)
						#plot_avgperf_14_1.append(average_perf_14_inst1)
						#y=plot_avg_14_1
						#plt.plot(average_time_14_inst1,color="red")
						#plt.show()
							
					if(len(time_3_14_inst2)==100):
						average_time_14_inst2=sum(time_3_14_inst2)/len(time_3_14_inst2)
						average_perf_14_inst2=sum(perf_3_14_inst2)/len(perf_3_14_inst2)
						print("The average matrix for time taken folder",cities,"and instance is",instance, "time_3_14_inst2", average_time_14_inst2)
						plot_avg_14_2.append(average_time_14_inst2)
						plot_avgperf_14_2.append(average_perf_14_inst2)
					if(len(time_3_15_inst1)==100):
						average_time_15_inst1=sum(time_3_15_inst1)/len(time_3_15_inst1)
						average_perf_15_inst1=sum(perf_3_15_inst1)/len(perf_3_15_inst1)
						print("The average matrix for time taken folder",cities,"and instance is",instance, "time_3_14_inst1", average_time_15_inst1)
						plot_avg_15_1.append(average_time_15_inst1)
						plot_avgperf_15_1.append(average_perf_15_inst1)
					if(len(time_3_15_inst2)==100):
						average_time_15_inst2=sum(time_3_15_inst2)/len(time_3_15_inst2)
						average_perf_15_inst2=sum(perf_3_15_inst2)/len(perf_3_15_inst2)
						print("The average matrix for time taken folder",cities,"and instance is",instance, "time_3_14_inst1", average_time_15_inst2)
						plot_avg_15_2.append(average_time_15_inst2)
						plot_avgperf_15_2.append(average_perf_15_inst2)
					if(len(time_3_16_inst1)==100):
						average_time_16_inst1=sum(time_3_16_inst1)/len(time_3_16_inst1)
						average_perf_16_inst1=sum(perf_3_16_inst1)/len(perf_3_16_inst1)
						print("The average matrix for time taken folder",cities,"and instance is",instance, "time_3_14_inst1", average_time_16_inst1)
						plot_avg_16_1.append(average_time_16_inst1)
						plot_avgperf_16_1.append(average_perf_16_inst1)
					if(len(time_3_16_inst2)==100):
						average_time_16_inst2=sum(time_3_16_inst2)/len(time_3_16_inst2)
						average_perf_16_inst2=sum(perf_3_16_inst2)/len(perf_3_16_inst2)
						print("The average matrix for time taken folder",cities,"and instance is",instance, "time_3_14_inst1", average_time_16_inst2)
						plot_avg_16_2.append(average_time_16_inst2)
						plot_avgperf_16_2.append(average_perf_16_inst2)

								

					#return current_state,curr_cost

							

			print("The evrage time for city ",cities,"instances",instance, "is", plot_avg_14_1)
			s=TSP_class()
			#print("Running ONLY hill clibming algorithm")
			#best_path,best_cost=s.TSP_hill()
			#print("The best path is ",best_path+'A')
			#print("The best cost is ",best_cost)
			s.TSP_simulatedAnn()
			#print("the best state is",best_state)
			#print("the best cost is",best_cost)


#plt.plot(1,average_time_14_inst1,color="red")
#plt.show()
# #x=range(10,100,10)
y=plot_avg_14_1
#y=plot_avg_14_1
#print("The length od y is",len(y))
plt.plot(y,color='red')
#plt.show()
y=plot_avg_14_2

plt.plot(y,color='green')
#plt.show()
y=plot_avg_15_1
plt.plot(y,color='blue')
#plt.show()
y=plot_avg_15_2
plt.plot(y,color='yellow')
#plt.show()
y=plot_avg_16_1
plt.plot(y,color='violet')
#plt.show()
y=plot_avg_16_2
plt.plot(y,color='orange')
# plt.xlabel("random restarts")

plt.ylabel("average time for instances color specified")
plt.show()


y=plot_avgperf_14_1
plt.plot(y,color='red')
# plt.xlabel("random restarts")
# plt.ylabel("Cities 14, instance 1")
#plt.show()

y=plot_avgperf_14_2
plt.plot(y,color='green')
# plt.xlabel("random restarts")
# plt.ylabel("Cities 14, instance 2")
#plt.show()

y=plot_avgperf_15_1
plt.plot(y,color='blue')
# plt.xlabel("random restarts")
# plt.ylabel("Cities 15, instance 1")
#plt.show()

y=plot_avgperf_15_2
plt.plot(y,color='yellow')
# plt.xlabel("random restarts")
# plt.ylabel("Cities 15, instance 2")
#plt.show()

y=plot_avgperf_16_1
plt.plot(y,color='violet')
# plt.xlabel("random restarts")
# plt.ylabel("Cities 16, instance 1")
# #plt.show()

y=plot_avgperf_16_2
plt.plot(y,color='orange')
# plt.xlabel("random restarts")
# plt.ylabel("Cities 16, instance 2")
# plt.xlabel("random restarts")
plt.ylabel("average PERFORMANCE for instances color specified")  
plt.show()

