//Author: R.U.S.T.E.A.M
#include <bits/stdc++.h>

using namespace std;

int even(long long n) 
{
   
    int count = 0;
    for (int i = 1; i * i <= n; i++) 
    {
    if (n % i == 0) 
    {
        int x = n / i;
        count += i % 2 == 0;

        if (i != x) count += x % 2 == 0;
    }
    }
    return count;
}



int main()
{
  long long t,n;
  cin>>t;
  for(int i=0;i<t;i++)
  {
    cin>>n;
    cout<<even(n)<<"\n";
  }
}
