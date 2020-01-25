// HCN - Highly Composite Numbers

#include<bits/stdc++.h>
using namespace std;


int prime[] = {2,3,5,7,11,13.17,19,23};
unsigned long long resNum,resDiv,n;

void recur(int pos,int limit,long long num,int div){
	if(div > resDiv){  // Get the number with highest NOD
		resNum = num;
		resDiv = div;
	}
	
	//In case of tie, take smaller number
	else if(resDiv == div && num < resNum)
    resNum = num;
    
// breaking condition
if(pos == 9)   return;

long long p = prime[pos];

for(int i = 1; i <= limit; ++i){

// if the number is less than the previous
	if(num * p > n) break; 
	recur(pos+1,i,num * p,div * (i+1));
	p *= prime[pos];
   }
}	


int main(){
  resNum = 0;
  resDiv = 0;
  cin>>n;
// we are using for 10^9 numbers... needs atleast 9 of primorials
  recur(0,30,1,1);	
 
  cout<<"HCN is:"<<resNum<<" & Number of divisors:"<<resDiv<<endl;
}
