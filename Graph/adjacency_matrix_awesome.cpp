#include<bits/stdc++.h>
using namespace std;
bool arr[100][100];
void initialize(){
	for(int i = 0; i < 100; ++i){
		for(int j = 0; j < 100; ++j)
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

cout<<"Check for a pair to be an edge:";
int a,b;
cin>>a>>b;

if(arr[a][b] == true)
cout<<"Edge exists!\n";
else cout<<"No edges!!!\n";

return 0;
}
