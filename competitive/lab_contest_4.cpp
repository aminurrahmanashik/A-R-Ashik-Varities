
// Bismillahir Rahmanir Rahim//


#include<bits/stdc++.h>
using namespace std;

#define N 1000
vector<int>adj[N];
bool visited[N];  // true or false detector
vector<int>result;


void dfs(int u)
{
    visited[u]=1;
    result.push_back(u);
    for(int i=0;i<adj[u].size();i++)
    {
        if(!visited[(adj[u][i])])
            dfs(adj[u][i]);
    }
}


int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,e;
        cin >>n>>e;
       
       // making all unvisited
        for(int i=0; i<N; i++)
        {
            adj[i].clear();
            visited[i]=false;
        }
        result.clear();
        
        for(int i=0; i<e; i++)
        {
            int u,v;
            cin>>u>>v;
            adj[u].push_back(v);
        }
        
        dfs(1);
        sort(result.begin(),result.end());
        // output
        for(int i=0;i<result.size();i++)
        cout<<result[i]<<" ";
        cout<<endl;
    }
return 0;
}



/*
#include<bits/stdc++.h>
using namespace std;
vector<int>g[100];
int vis[100];
int cnt=0;
void dfs(int source )
{

	vis[source]=1;
	for(int i=0;i<g[source].size();i++)
	{   int next=g[source][i];
		if(!vis[next])
		{
			dfs(next);
            cnt++;
		}
	}
}
int main()
{


    int cases;
    cin>>cases;

    while(cases--){
   /* for(int i=0;i<1000;i++)
    {
        g[i].clear();
    }
    cnt=0;
    int n,m;
    cin>>n>>m;
     for(int i = 0; i <= n; i++)
        {
            g[i].clear();
            vis [i] = 0;
           // cost[i][i] = 0;
        }

    for(int i=0;i<m;i++)
    {
    	int x,y;
    	cin>>x>>y;
    	g[x].push_back(y);
    }
    memset(vis,0,sizeof vis);

    dfs(1);

    cnt++;
    cout<<cnt<<endl;
}

}
*/
