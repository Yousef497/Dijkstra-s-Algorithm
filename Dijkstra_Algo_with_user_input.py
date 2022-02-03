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
import time

def dijkstra(n_nodes,nodes_graph,source,destination):

    # A function that takes nodes parameter (which describes how nodes are connected)
    # source parameter is the first terminal that we want to start from
    # destination parameter is the final terminal that we want to reach
    
    # We set the cost of all terminal to infinty ( max number to compare with to get
    # the minimum when the node is not visited yet)
    # create a dictionary to hold nodes data

    inf = sys.maxsize

    node_data = {}
    unvisited = nodes_graph.copy()
    path = []
    track_previous = {}

    for node in nodes_graph:
        node_data[node] = inf

    # source terminal cost must be zero

    node_data[source] = 0

    while unvisited:
        min_distance_node = None

        for node in unvisited:
            if min_distance_node is None:
                min_distance_node = node
            elif node_data[node] < node_data[min_distance_node]:
                min_distance_node = node

        path_options = nodes_graph[min_distance_node].items()

        for child_node, weight in path_options:
            if ((weight + node_data[min_distance_node]) < node_data[child_node]):
                node_data[child_node] = weight + node_data[min_distance_node]
                track_previous[child_node] = min_distance_node

        unvisited.pop(min_distance_node)


    currentNode = destination

    while currentNode != source:
        try:
            path.insert(0, currentNode)
            currentNode = track_previous[currentNode]

        except KeyError:
            print("Path is not reachable\n")
            break

    path.insert(0, source)

    # printing the shortest distance and the shortest path
    if node_data[destination] != inf:
        print("\n")
        print("Shortest Distance to the Final Node: " + str(node_data[destination]))
        print("Shortest Path: " + str(path))
        print("\n")




if __name__ == "__main__":
        
    nodes_graph = {}

    nodes_numbers = input("Please Enter the number of Nodes: ")

    # This part is to take user input like the name of nodes and the neighbors to each node and distance
    # You also can input the number of nodes

    print("Please do not enter Node name more than once")
    for i in range(int(nodes_numbers)):
        node_name = input("Enter Node Name: ")

        nodes = {}

        neighbors_number = 0

        try:
            neighbors_number = int(input("Please Enter the number of neighbors to this Node (Enter only integers): "))
        except:
            if not isinstance(type(neighbors_number),int):
                print("Wrong input only integers are allowed, Closing the application.")
                time.sleep(5)


        for j in range(neighbors_number):
            data = input('Enter name of neighbor & distance by ":" ') 
            temp = data.split(':') 
            nodes[temp[0].title()] = int(temp[1])
        
        print("\n")
        nodes_graph[node_name.title()] = nodes


    char = "Y"

    while(char == "Y"):
        source = input("Enter The name of the source node: ").title()
        destination = input("Enter The name of the destination node: ").title()

        dijkstra(nodes_numbers,nodes_graph,source,destination)

        char = input("Do you want to try the path between 2 different nodes? y/n: ").title()
        print("\n")
