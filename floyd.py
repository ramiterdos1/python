#script for Floyd Warshall Algorithm- All Pair Shortest Path

INF = 999999999

def printSolution(distGraph):

    string = "inf"

    nodes =distGraph.keys()

    for n in nodes:

        print "\t%6s"%(n),

    print " "

    for i in nodes:

        print"%s"%(i),

        for j in nodes:

            if distGraph[i][j] == INF:

                print "%10s"%(string),

            else:

                print "%10s"%(distGraph[i][j]),

        print" "

def floydWarshall(graph):

    nodes = graph.keys()

    distance = {}

    for n in nodes:

        distance[n] = {}

        for k in nodes:

            distance[n][k] = graph[n][k]

    for k in nodes:

        for i in nodes:

            for j in nodes:

                if distance[i][k] + distance[k][j] < distance[i][j]:

                    distance[i][j] = distance[i][k]+distance[k][j]

    printSolution(distance)

if __name__ == '__main__':

    graph = {'0':{'0':0,'x':8,'y':8,'w':8},

             'x':{'0':INF,'x':0,'y':4,'w':INF},

             'y':{'0':INF,'x':-3,'y':0,'w':0},

             'w':{'0':INF,'x':-3,'y':0,'w':0},

             }

    floydWarshall(graph)
