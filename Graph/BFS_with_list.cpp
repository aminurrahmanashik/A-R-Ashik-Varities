#include<bits/stdc++.h>
using namespace std;


bool visited[100];
int dist[100];
vector<int>graph[100];
queue<int>q;

void bfs(int start){
	int cur,next;
	q.push(start);
	visited[start] = 1;
	dist[start] = 0;
	
	while(!q.empty()){
		cur = q.front();
		q.pop();
		for(int i = 0; i < graph[cur].size(); ++i){
				next = graph[cur][i];
				if(!visited[next]){
					q.push(next);
					visited[next] = 1;
					dist[next] = 1+dist[cur];
				}
		}
	}
}
				

int main(){
	int i , j , k,source;
	int nodes,edges,u,v;
	cin>>nodes>>edges;
	
	for(i = 0; i < edges; ++i){
		cin>>u>>v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	memset(visited,0,sizeof(visited));
	
	cin>>source;
	
	bfs(source);
	
	for(i = 0; i < nodes; ++i){ 
		cout<<"Dist-"<<i<<":"<<dist[i]<<endl;
	}
	int destination;
	cin>>destination;
	
	cout<<"Distance of the node "<<destination<<" from "<<source<<" is:"<<dist[destination]<<endl;
}
