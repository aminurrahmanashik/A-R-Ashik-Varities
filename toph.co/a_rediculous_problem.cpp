

//BISMILLAHIR RAHMANIR RAHIM
/*
do DEEN(ISLAM), keep SMILE :) 
 Author :: A R Ashik
.............CUET_CSE17.........
problem :: A Rediculous Problem
source  :: Toph.co
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <limits.h>
#include <set>
#include <algorithm>
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <utility>
#define pb push_back
#define mp make_pair
#define pi acos(-1.0)
#define ff first
#define LL long long
#define ss second
#define rep(i,n) for(i = 0; i < n; i++)
#define REP(i,n) for(i=n;i>=0;i--)
#define FOR(i,a,b) for(int i = a; i <= b; i++)
#define ROF(i,a,b) for(int i = a; i >= b; i--)
#define re return
#define QI queue<int>
#define SI stack<int>
#define pii pair <int,int>
#define MAX
#define MOD
#define INF 1<<30
#define SZ(x) ((int) (x).size())
#define ALL(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define memo(a,b) memset((a),(b),sizeof(a))
#define G() getchar()
#define MAX3(a,b,c) max(a,max(b,c))

double const EPS=3e-8;
using namespace std;


template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }


string grid[10];
int main(){
   int i,len;
   for(int i = 1 ; i < 8; ++i){
   cin>>grid[i];
   }
   len = grid[1].size();
   for(i=0; i<len; i+=6){
   	
   	if(grid[1][i] == '*' && grid[4][i] == '*' && grid[7][i] == '*'){
   		
   		// printing H,M,N
   		if(grid[1][i+4] == '*' && grid[4][i+4] == '*' && grid[7][i+4] == '*'){
   			if(grid[4][i+1] == '*')                cout<<'H';
   			else if(grid[3][i+2] == '*')           cout<<'M';
   			else                     	 		   cout<<'N';
		   }
		   
		  
		   // printing K,L
		   else if(grid[1][i+1] == '.'){
		   	if(grid[4][i+1] == '*')                 cout<<'K';
		   	else                                    cout<<'L';
		   }
		   
		    // printing E,F
		   else if(grid[1][i+4] == '*'){          
		   	if(grid[7][i+4] == '*')				   cout<<'E';
		   	else               					   cout<<'F';	
		   }
		   
		   // printing B,D
		   else if(grid[7][i+1] == '*'){
		   	if(grid[4][i+1] == '*')                  cout<<'B';
		   	else                                     cout<<'D';
		   }
		   
		   // printing R,P
		   else{
		   	if(grid[7][i+4] == '*')                  cout<<'R';
		   	else                                     cout<<'P';
		   }
	}
	
	// printing A,S,X,Z
	else if(grid[7][i] == '*'){
		if(grid[4][i+1] == '*'){
			if(grid[1][i+4] == '*')                  cout<<'S';
			else                                     cout<<'A';
		}
		else if(grid[3][i+1] == '*')                 cout<<'X';
		else                                         cout<<'Z';
		}     
	// printing  T,W,Y
	else if(grid[6][i+2] == '*'){
		if(grid[1][i] == '*' && grid[1][i+4] == '*'){
			if(grid[1][i+2] == '*')                  cout<<'T';
			else if(grid[7][i+1] == '*')             cout<<'W';
			else                                     cout<<'Y';
		}
		else                                         cout<<'I';
	}
	
	// printing U,G,O,C
	else if(grid[2][i] == '*' && grid[2][i+4] == '*'){
     if(grid[6][i] == '*' && grid[6][i+4] == '*'){
		if(grid[1][i] == '*')                         cout<<'U';
		else if(grid[5][i+3] == '*')                  cout<<'G';
		else if(grid[4][i+4] == '*')                  cout<<'O';
		else                                          cout<<'C';
		}
		
		   // printing Q,V
	    else{
	    	if(grid[5][i+2] == '*')                   cout<<'Q';
	    	else                                      cout<<'V';
		}  
	   }
	   // printing J  
	   else                                           cout<<'J';
   }
   return 0;
}
