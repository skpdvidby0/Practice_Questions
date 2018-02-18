# Author : Shreyas Panigrahi
# Date   : 2-14-2018

"""
The idea is to create a directed acyclic graph of the letters in words of sorted dictionary.
1)  The graph is created by pairwise checking concecutive words in the dictionary. If corresponding
    letters of the word do not match then an edge is added from the letter in the word1 to the letter
    in word2 since, word1 is above word2 in  the dictionary.
2)  After the graph is created a simple topological
    sort is performed and it yields the result.

function printOrder returns a list of ordered sequence of the letters that comprise the alphabet used
to sort this list of terms
"""

from collections import defaultdict

#Open the file and read it line by line
with open("alphabet.txt") as f:
    content = f.readlines()
    #print content

content = [x.strip() for x in content]


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)


    def addEdge(self, u, v):
        self.graph[u].add(v)

    #compare words and add an edge in the graph and call topological sort after graph created
    def printOrder(self,content):
        for i in range(len(content)-1):
            word1=content[i]
            word2=content[i+1]
            for j in range(min(len(word1),len(word2))):
                if (word1[j]!=word2[j]):
                    self.addEdge(word1[j],word2[j])
                    break
        return self.topologicalSort(self.graph)


    def topSortHelper(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
           # try:
                if i not in visited:
                    self.topSortHelper(i,visited,stack)
            #except:
             #   print i
        stack.insert(0,v)

    #recursive topological sort with call to helper function. Implemented with a stack
    def topologicalSort(self,graph):
        visited=[]*len(self.graph)
        stack=[]
        for i in self.graph.keys():
            if i not in visited:
                self.topSortHelper(i,visited,stack)
        # for i in range(len(stack)):
        #     print "Letter",i+1,"=>",stack[i]
        return stack

#Create graph and get the returned ordered sequence
g=Graph()
stack=g.printOrder(content)
for i in range(len(stack)):
    print "Letter", i + 1, "=>", stack[i]

