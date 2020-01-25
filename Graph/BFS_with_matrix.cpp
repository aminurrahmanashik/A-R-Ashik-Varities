// BFS using adjacency matrix

#include<bits/stdc++.h>
using namespace std;

#define White 1
#define Gray 2
#define Black 3
#define INF -121212121   // garbage for pre-distance of every node
int adj[100][100];
int color[100];
int parent[100];
int dist[100];   // distance array
int node,edge,cost;

void bfs(int SrtNode){
	for(int i = 0; i < node; ++i){  //  for every node the following operation
	    color[i] = White;
	    parent[i] = -1;
	    dist[i] = INF;
	}
	// these dist & parent are for only starting node
	parent[SrtNode] = -1;
	dist[SrtNode] = 0;
	 // taking a queue
	 queue<int>q;
	 q.push(SrtNode);  // pushing the starting node
	 
	 while(!q.empty()){
	 	// now we'll take the first index / front value of the queue 
	 	int x;
	 	x = q.front();
	 	cout<<x<<" ";
	 	q.pop(); // pop it up / 1st element
	 	color[x] = Gray;   // color of the front -> 'Gray' means it's on processing
	 	
		 // this loop will give us the distance or level of each nodes
		 for(int i = 0; i < node; ++i){
	 		// now time to check for adjacency
	 		if(adj[x][i] == cost){
	 			if(color[i] == White){  // if it's not neen processed
	 				 dist[i] = dist[x] + cost;  // dist[x] will give the parent's distance
	 				 parent[i] = x;
	 				 q.push(i);  // adjacent node are being pushed in the queue
				 }
	   	 }
		 }
	 	color[x] = Black;	  // Black means it's already processed
	 }    
}


int main(){
	// node and edge declared global
	cin>>node>>edge>>cost;  // taking nodes
	for(int i = 0; i < edge; ++i){
		int u,v;
		cin>>u>>v; 
		adj[u][v] = cost;
		adj[v][u] = cost;
	}
	 // starting Node
	int SrtNode;  cin>>SrtNode; 
	bfs(SrtNode);  // pssing starting node
	return 0;
}
