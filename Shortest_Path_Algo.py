'''
            Dijkstra's Algorithm

Dijkstra's algorithm find the shortest path between any two nodes
by checking the neighboring nodes and calculating the cost
(distace of previous node + distance to the neighboring node)
then comparing with each others and choosing the minimum value and append
this minimum value in a list and this list will include the shortest path
nodes.

This steps are repeated till the terminal node is reached.
'''

import sys
from heapq import heapify, heappush, heappop


def dijsktra(n_nodes,nodes_graph,source,destination):

    # A function that takes nodes parameter (which describes how nodes are connected)
    # source parameter is the first terminal that we want to start from
    # destination parameter is the final terminal that we want to reach
    
    # We set the cost of all terminal to infinty ( max number to compare with to get
    # the minimum when the node is not visited yet
    # create a dictionary to hold nodes data

    inf = sys.maxsize

    nodes_graph_keys = nodes_graph.keys()
    node_data = {}

    for i in nodes_graph_keys:
        node_data.update({i : {'cost':inf, 'previous':[]}})
    
    # if you want to use fixed points
    #node_data = {'A':{'cost':inf, 'previous':[]},
    #             'B':{'cost':inf, 'previous':[]},
    #             'C':{'cost':inf, 'previous':[]},
    #             'D':{'cost':inf, 'previous':[]},
    #             'E':{'cost':inf, 'previous':[]},
    #             'F':{'cost':inf, 'previous':[]},
    #             'G':{'cost':inf, 'previous':[]},
    #             'H':{'cost':inf, 'previous':[]},
    #             'I':{'cost':inf, 'previous':[]},
    #             'J':{'cost':inf, 'previous':[]},
    #             'K':{'cost':inf, 'previous':[]},
    #             'L':{'cost':inf, 'previous':[]},
    #             'M':{'cost':inf, 'previous':[]},
    #             'N':{'cost':inf, 'previous':[]},
    #             'O':{'cost':inf, 'previous':[]}
    #             }

    # source terminal cost must be zero

    node_data[source]['cost'] = 0

    # create a set of visited elements to record the visited elements to ignore when 
    # calculating the next node
    # also create a temp variable that updates the source to the element which is minimum
    # out of all the neigbours

    visited = []
    temp = source

    # we need a for loop to iterate through the nodes choosing the minimum cost

    for i in range(int(n_nodes)-1):
        if temp not in visited:
            visited.append(temp)

            # creating a list that holds the minimum cost of the nodes for each iteration
            min_heap = []
            for j in nodes_graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + nodes_graph[temp][j]

                    if (cost < node_data[j]['cost']):
                        node_data[j]['cost'] = cost     # assign the least cost
                        node_data[j]['previous'] = node_data[temp]['previous'] + list(temp)     # add the previous node to the list
                    
                    #pushing the leastcost into min_heap list that we created
                    #then use the heapify function to get the the minimum of the neighbors cost
                    heappush(min_heap,(node_data[j]['cost'],j))

        #use heapify function to get the next node which has the least cost and update the temp variable with it
        heapify(min_heap)
        temp = min_heap[0][1]   # [0] is the minimum value and [1] is the neighbor

    # printing the shortest distance and the shortest path
    print("\n")
    print("Shortest Distance to the Final Node: " + str(node_data[destination]['cost']))
    print("Shortest Path: " + str(node_data[destination]['previous'] + list(destination)))


if __name__ == "__main__":
    
    nodes_graph = {}

    nodes_numbers = input("Please Enter the number of Nodes: ")

    # This part is to take user input like the name of nodes and the neighbors to each node and distance
    # You also can input the number of nodes

    print("Please do not enter Node name more than once")
    for i in range(int(nodes_numbers)):
        node_name = input("Enter Node Name: ")

        nodes ={}
        neighbors_number = input("Please Enter the number of neighbors to this Node: ")
        for j in range(int(neighbors_number)):
            data = input('Enter name of neighbor & distance by ":" ') 
            temp = data.split(':') 
            nodes[temp[0].title()] = int(temp[1])
        
        print("\n")
        nodes_graph[node_name.title()] = nodes


    char = "Y"

    while(char == "Y"):
        source = input("Enter The name of the source node: ").title()
        destination = input("Enter The name of the destination node: ").title()

        dijsktra(nodes_numbers,nodes_graph,source,destination)

        char = input("Do you want to try the path between 2 different nodes? y/n \n").title()

       
