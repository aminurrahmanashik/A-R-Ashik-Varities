#include<bits/stdc++.h>
#include<algorithm>
#include<cstring>
#include<string>
#include<cstdlib>
#include<vector>

using namespace std;


bool comp( const pair<float,int>& u, const pair<float,int>& v )
{  return u.first>=v.first;
}


int a1[100005],a2[100005],a3[100005];


int main()
{

    int i,j,k,l,m,n,s,c=0;
    cin>>s>>n;
    pair<float,int> a[n+5];
    for(i=0;i<n;i++)
        {cin>>a[i].first;
        a[i].second=i+1;}

    sort(a,a+n,comp);

    if(s==3)
        for(i=n-10;i<n;i++)
            cout<<a[i].second<<endl;
    if(s==1)
        for(i=0;i<10;i++)
            cout<<a[i].second<<endl;
     if(s==2)
            for(i=(n/2)-5;;i++)
            {
                c++;
                cout<<a[i].second<<endl;
                if(c==10)
                    break;
            }

return 0;
}
