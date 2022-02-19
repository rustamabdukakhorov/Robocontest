//Author: R.U.S.T.E.A.M
#include <bits/stdc++.h>
using namespace std;

long long int binar(long long int n)
{
    if(n==1)
        return 1;
    if(n%2==0)
        return 10*binar(n/2);
    else
        return 10*binar(n/2)+1;
}

int main() 
{
    int t;
    cin>>t;
    while(t--)
    {
        long long int n,a=1,b=9;
        cin>>n;
        while(b%n!=0)
        {
            a++;
            b=binar(a);
            b*=9;
        }
        cout<<b<<endl;
    }
    return 0;
}
