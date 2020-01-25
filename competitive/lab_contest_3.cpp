
// Bismillahir Rahmanir Rahim // 

#include<bits/stdc++.h>
using namespace std;

vector<int>graph[100];
int visited[100];
int cnt = 0; 

// dfs function
void dfs(int source)
{
	visited[source] = 1;
	for(int i = 0;i < graph[source].size(); i++)
	{   int nxt = graph[source][i];
		if(!visited[nxt])
		{
			dfs(nxt);
            cnt++;
		}
	}
}


int main()
{
    int T;
    cin>>T;

    while(T--){
    	
    int n,m; cnt = 0; 
    cin>>n>>m;
    
     for(int i = 0; i <= n; i++)
        {
            graph[i].clear();
            visited[i] = 0;
        }

    for(int i = 0;i < m; i++)
    {
    	int a,b;
    	cin>>a>>b;
    	graph[a].push_back(b);
    }
    
    memset(visited,0,sizeof visited);
    dfs(1);
    // it will count the no of visited nodes through the same path 
	cnt++;
	// output
    cout<<cnt<<endl;
}

}
