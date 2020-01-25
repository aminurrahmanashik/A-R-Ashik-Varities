// this will show the output for 
// Calculating the number of digits directly

#include<bits/stdc++.h>
using namespace std;

int main(){
  int num;  cin>>num;
  int N = floor(log10(num))+1;
  cout<<N;
  return 0;	
}
