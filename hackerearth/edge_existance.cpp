#include<bits/stdc++.h>
using namespace std;

bool arr[1005][1005];
void initialize(){
	for(int i = 0; i < 1005; ++i){
		for(int j = 0; j < 1005; ++j)
		arr[i][j] = false;
	}
}

int main(){
	int nodes,edges,x,y;
	cin>>nodes>>edges;
	initialize();
	
	for(int i = 0; i < edges; ++i){
	 cin>>x>>y;
	//freopen("input.txt", "r", stdin); 
	arr[x][y] = true;
	arr[y][x] = true;
}

int Q;  cin>>Q;
for(int q = 0 ; q < Q; ++q){
	int a,b;
cin>>a>>b;
if(arr[a][b] == true)
cout<<"YES\n";
else cout<<"NO\n";
}

return 0;
}
