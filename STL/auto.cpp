//#include<bits/stdc++.h>
//using namespace std;
//int main(){
//	auto x = 4;
//	auto y = 3.37;
//	auto ptr = &x;
//	cout<<typeid(x).name()<<endl;
//	cout<<typeid(y)<<endl;
//	cout<<typeid(ptr)<<endl;
//	return 0;
//}

// C++ program to demonstrate working of auto 
// and type inference 
#include <bits/stdc++.h> 
using namespace std; 

int main() 
{ 
	int x = 4; 
	auto y = 3.37; 
	auto ptr = &x; 
	cout << x << endl 
		<< y<< endl 
		<< ptr << endl; 

	return 0; 
} 

