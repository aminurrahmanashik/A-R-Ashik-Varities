#include<bits/stdc++.h>
using namespace std;

vector<int>adj[10];
int main(){
	int x,y,nodes,edges;
	cin>>nodes>>edges;
	
	for(int i = 0; i < edges; ++i){
		cin>>x>>y;
		adj[x].push_back(y);
	}
	
   for(int i = 1; i <= nodes; ++i){
   	cout<<"Adjacency list of "<<i<<":";
   	
   	for(int j = 0; j < adj[i].size(); ++j){  // i starts from '0' as we've taken edges '0' indexed/ see input loop i
   		if(j == adj[i].size()-1)    // it will print the last node value 
	      cout<<adj[i][j]<<endl;
	      else cout<<adj[i][j]<<"-->";  // printing continued...
	   }
   }
   return 0;
}

