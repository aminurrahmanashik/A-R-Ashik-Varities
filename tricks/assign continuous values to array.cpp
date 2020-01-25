// C++ code to demonstrate working of iota() 

#include<bits/stdc++.h>
using namespace std; 
int main() 
{ 
int a[5] = {0}; 
char c[3] = {0}; 

// changes a to {10, 11, 12, 13, 14} 
iota(a, a+5, 10); 
iota(c, c+3, 'a'); // {'a', 'b', 'c'}

	return 0; 

} 

