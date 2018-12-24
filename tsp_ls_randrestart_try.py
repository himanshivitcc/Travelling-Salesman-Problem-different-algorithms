import math
import heapq
import sys
import numpy
import os
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time

dir = 'C:/Users/himan/Downloads/tsp_problems_ls/tsp_problems'
# for cities_dir in range(14, 17):
#     for inst in range(1,3):
#         instance = 'instance_' + str(inst) + '.txt'
#         fil = open(os.path.join(data_dir + '/' + str(cities_dir) + '/', instance), 'r')
#         st = fil.read()
#         data = st.split('\n')
#         distances, vertices = hill_climb.create_graph(data)
        #print(distances, vertices)
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
for cities in range(14, 17):
    print("the folder now is ",cities)
    index=0
    avg_list=[None]*10
    for instances in range(1,3):
        
        for rnd_restart in range(2,20,2):
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

            average_time_14_inst1=[]
            for i in range(0,100):
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
                        print("in TSP restart")
                        
                        start = time.time()
                        while True:
                            performance=0
                            if(random_restart > rnd_restart):
                                print("no solution")
                                #best_cost = 0
                                break
                            best_path,best_cost=self.TSP_hill()
                            print("The path generated is ",best_path)
                            print("The cost generated is ",type(best_cost))
                                #if(best_cost=="AMBFCDKLEGNIHJ"):
                            print("hellloooo")
                            if(int(cities)==14 and instance == "instance_1.txt" ):
                                if(math.floor(best_cost)<=(318*1.01)):
                                    print("Found")
                                    #steps_3_14.append(random_restart)
                                    performance = best_cost/318

                                    break

                                else:
                                    random_restart+=1
                                    continue

                            

                            if(int(cities)==14 and instance == "instance_2.txt" ):       
                                if(math.floor(best_cost)<=(324*1.01)):
                                    print("Found")
                                    performance = best_cost/324
                                    break
                                else:
                                    random_restart+=1
                                    continue

                            if(int(cities)==15 and instance == "instance_1.txt" ):
                                if(math.floor(best_cost)<=(315.07*1.01)):
                                    print("Found")
                                    performance = best_cost/315.07
                                    break
                                else:
                                    random_restart+=1
                                    continue

                            if(int(cities)==15 and instance == "instance_2.txt" ):
                                if(math.floor(best_cost)<=(318*1.01)):
                                    print("Found")
                                    performance = best_cost/318
                                    break
                                else:
                                    random_restart+=1
                                    continue

                            if(int(cities)==16 and instance == "instance_1.txt" ):
                                if(math.floor(best_cost)<=(404*1.01)):
                                    print("Found")
                                    performance = best_cost/404
                                    break
                                else:
                                    random_restart+=1
                                    continue

                            if(int(cities)==16 and instance == "instance_2.txt" ):
                                if(math.floor(best_cost)<=(354.55*1.01)):
                                    print("Found")
                                    performance = best_cost/354.55
                                    break
                                else:
                                    random_restart+=1
                                    continue
                        end = time.time()
                        #print()

                        time_taken= end-start
                        print("The number of random restart is ",random_restart, "for random_restart",rnd_restart,"folder",cities,"and instance is",instance)
                        print("The time taken is ", end - start)
                        print("The performance is", performance )
                        #random_restart=0

                        if(int(cities)==14 and instance == "instance_1.txt" ):
                            time_3_14_inst1.append(time_taken)
                            perf_3_14_inst1.append(performance)

                        if(int(cities)==14 and instance == "instance_2.txt" ):
                            time_3_14_inst2.append(time_taken)
                            perf_3_14_inst2.append(performance)
                        if(int(cities)==15 and instance == "instance_1.txt" ):
                            time_3_15_inst1.append(time_taken)
                            perf_3_15_inst1.append(performance)
                        if(int(cities)==15 and instance == "instance_2.txt" ):
                            time_3_15_inst2.append(time_taken)
                            perf_3_15_inst2.append(performance)
                        if(int(cities)==16 and instance == "instance_1.txt" ):
                            time_3_16_inst1.append(time_taken)
                            perf_3_16_inst1.append(performance)
                        if(int(cities)==16 and instance == "instance_2.txt" ):
                            time_3_16_inst2.append(time_taken)
                            perf_3_16_inst2.append(performance)

                        if(len(time_3_14_inst1)==100):
                            average_time_14_inst1=sum(time_3_14_inst1)/len(time_3_14_inst1)
                            average_perf_14_inst1=sum(perf_3_14_inst1)/len(perf_3_14_inst1)
                            print("The average matrix for time taken folder",cities,"and instance is",instance, "time_3_14_inst1", average_time_14_inst1)
                            plot_avg_14_1.append(average_time_14_inst1)
                            plot_avgperf_14_1.append(average_perf_14_inst1)
                            
                            #plt.scatter(x,y)
                            #plt.xlabel("randon restarts")
                            #plt.ylabel("average time for instance 1 and cities 14")
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





                        
                       


                s=TSP_class()
                #print("Running ONLY hill clibming algorithm")
                #best_path,best_cost=s.TSP_hill()
                #print("The best path is ",best_path+'A')
                #print("The best cost is ",best_cost)
                s.TSP_hill_restart()

x=range(10,100,10)
y=plot_avg_14_1
plt.plot(x,y,color='red', label='jjjj')
y=plot_avg_14_2
plt.plot(x,y,color='green')
y=plot_avg_15_1
plt.plot(x,y,color='blue')
y=plot_avg_15_2
plt.plot(x,y,color='yellow')
y=plot_avg_16_1
plt.plot(x,y,color='violet')
y=plot_avg_16_2
plt.plot(x,y,color='orange')
plt.xlabel("random restarts")
plt.ylabel("average time for instances color specified")
plt.show()
#red_patch = mpatches.Patch(color='red', label='cities 14 , instance_1',color='green', label='cities 14 , instance_2')
#plt.legend(handles=[red_patch],handles=[green_patch])

y=plot_avgperf_14_1
plt.plot(x,y,color='red')
plt.xlabel("random restarts")
plt.ylabel("Cities 14, instance 1")
#plt.show()

y=plot_avgperf_14_2
plt.plot(x,y,color='green')
plt.xlabel("random restarts")
plt.ylabel("Cities 14, instance 2")
#plt.show()

y=plot_avgperf_15_1
plt.plot(x,y,color='blue')
plt.xlabel("random restarts")
plt.ylabel("Cities 15, instance 1")
#plt.show()

y=plot_avgperf_15_2
plt.plot(x,y,color='yellow')
plt.xlabel("random restarts")
plt.ylabel("Cities 15, instance 2")
#plt.show()

y=plot_avgperf_16_1
plt.plot(x,y,color='violet')
plt.xlabel("random restarts")
plt.ylabel("Cities 16, instance 1")
#plt.show()

y=plot_avgperf_16_2
plt.plot(x,y,color='orange')
plt.xlabel("random restarts")
plt.ylabel("Cities 16, instance 2")
plt.xlabel("random restarts")
plt.ylabel("average PERFORMANCE for instances color specified")  
plt.show()



print("the size of x is ",len(x), "and y is ",len(y))


