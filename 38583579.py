import sys
sys.setrecursionlimit(10**6)
from collections import  defaultdict
class Graph:
	def __init__(self,v):
		self.vertices=v
		self.g=defaultdict(lambda:[])


	def add_edge(self,u,v):
		self.g[u].append(v)
		self.g[v].append(u)


	def dfs_util(self,source,visited,count):
		visited[source]=True 
		count+=1

		for i in self.g[source]:
			if not visited[i]:
				count=self.dfs_util(i,visited,count)


		return count


	def dfs(self):
		visited=[False]*(self.vertices+1)
		m=1000000007
		count=1
		
		dist=0

		for i in range(1,self.vertices+1):
			if not visited[i]:
				
				dist+=1
				count=(count*self.dfs_util(i,visited,0))%m
				

		print(dist,count)

	def clear(self):
		self.g.clear()


for _ in range(int(input())):
	n,m=map(int,input().split())
	g=Graph(n)
	for _ in range(m):
		u,v=map(int,input().split())
		g.add_edge(u,v)

	g.dfs()
	g.clear()