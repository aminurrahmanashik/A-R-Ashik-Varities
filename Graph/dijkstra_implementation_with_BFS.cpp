#include<bits/stdc++.h>
using namespace std;

// bool visited[100];
int dist[100];
vector<int>graph[100];
vector<int>weight[100];
queue<int>q;

 void dijkstra(int start){
 	int cur,next,cost;
 	q.push(start);
 	dist[start] = 0;
 	
 	while(!q.empty()){
 		cur = q.front();
 		q.pop();
 		
 		for(int i = 0; i <  graph[cur].size(); ++i){
 			next = graph[cur][i];
 			cost = weight[cur][i];
 			// q.pop();
 		    if(dist[next] > dist[cur] + cost){
 		    	q.push(next);
 		    	dist[next] = dist[cur]+cost;
			 }
		 }
	 }	
 }


int main(){
	int i,j,k;
	int nodes,edges,source,destination;
	int u,v,w;
	cin>>nodes>>edges;
	
	for(i = 0; i < edges; ++i){
		cin>>u>>v>>w;
		
		graph[u].push_back(v);
		weight[u].push_back(w);
		graph[v].push_back(u);
		weight[v].push_back(w);
		
	}
		for(int i = 0; i < nodes; ++i)
		dist[i] = 1e8;
		
		cin>>source;
		dijkstra(source);
		
		for(i = 0; i < nodes; ++i)
			cout<<"Distance of the node "<<i+1<<" from "<<source<< " is:"<<dist[i]<<endl;
		
	return 0;
	}

