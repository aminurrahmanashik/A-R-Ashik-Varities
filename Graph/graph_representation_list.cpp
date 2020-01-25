#include<bits/stdc++.h>
using namespace std;

// adding edges..

void addEdge(vector<int>adj[],int u,int v){
	adj[u].push_back(v);
	adj[v].push_back(u);
}

// printing the list
void printGraph(vector<int>adj[],int V){
   for(int  i = 0; i < V; ++i){
   	cout<<"The node "<<i<<"'s connected list";
   	
   	// inner loop prints the adjacent nodes using iterator
   /*
   one can do this as well..
   for(int j = 0; j < adj[i].size(); ++j)
   	cout<<"->"<<adj[i][j];
   	*/
   	
   	// alternative way & best to me,
   		for(vector<int>:: iterator it = adj[i].begin(); it != adj[i].end(); ++it)
   		{
   			//cout<<"Value i: "<<i<<endl;;
   		cout<<"->"<<*it;   // iterator points the adjacency list nodes
   	}
   	cout<<"\n";
   }	
}
int main(){
	int V = 5;
	vector<int>ADJ[V];
	addEdge(ADJ,0,1);
	addEdge(ADJ,0,4);
	addEdge(ADJ,1,2);
	addEdge(ADJ,1,3);
	addEdge(ADJ,1,4);
//	addEdge(2,1);
	addEdge(ADJ,2,3);
	addEdge(ADJ,3,4);
	
	printGraph(ADJ,V);
}
