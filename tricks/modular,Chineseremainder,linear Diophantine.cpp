//Thisisacollectionofusefulcodeforsolvingproblemsthat 
//involvemodularlinearequations.Notethatallofthe 
//algorithmsdescribedhereworkonnonnegativeintegers.

#include<iostream> 
#include<vector> 
#include<algorithm>
using namespace std;
typedef vector<int>VI; 
typedef pair<int,int>PII;

int x,y,c,a,b;
//return a%b (positive value) 
int mod(int a,int b){ 
return((a%b)+b)%b; 
}

//computes gcd(a,b) 
int gcd(int a,int b){ 
while(b){
int t=a%b;a=b;b=t;
} 
return a; 
}
//computes lcm(a,b) 
int lcm(int a,int b){
x=c/a; y=0;  
return true;
} 
int g = gcd(a,b); 
if(c % g) return false; 
x=c/g*mod_inverse(a/g,b/g); 
y=(c-a*x)/b;  
return true;
}

int main(){ 
//expected:2 
cout<<gcd(14,30)<<endl;
//expected:2 -2 1  
int g=extended_euclid(14,30,x,y); 
cout<<g<<" "<<x<<" "<<y<<endl;
//expected:95 451 
VI sols=modular_linear_equation_solver(14,30,100); 
for(int i=0;i<sols.size();i++)
cout<<sols[i]<<" "; 
cout<<endl;
//expected:8 
cout<<mod_inverse(8,9)<<endl;
//expected:23 105 
//11 12 
PII ret=chinese_remainder_theorem(VI({3,5,7}),VI({2,3,2})); 
cout<<ret.first<<" "<<ret.second<<endl; 
ret=chinese_remainder_theorem(VI({4,6}),VI({3,5})); 
cout<<ret.first<<" "<<ret.second<<endl;
//expected:5 -1 5 
if(!linear_diophantine(7,2,5,x,y))
cout<<"ERROR"<<endl; 
cout<<x<<""<<y<<endl; 
return 0;
}

