#include<bits/stdc++.h>
using namespace std;

/* Function to check if x is power of 2*/
bool isPowerOfTwo (int x) 
{ 
  /* First x in the below expression is  
    for the case when x is 0 */
  return x && (!(x&(x-1))); 
} 

int main()
{
 int n; cin>>n;
 if(!isPowerOfTwo (n) )
 cout<<"NO\n";
 else cout<<"YES\ ";
// cout<<isPowerOfTwo (n);  // returns '1' or '0'

 return 0;
}
