//Author: R.U.S.T.E.A.M
#include <bits/stdc++.h>

using namespace std;

bool isPrime(int n)
{
    if (n <= 1)
        return false;
  
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            return false;
  
    return true;
}

int main()
{
	int n, count = 0;
	cin>>n;
	for(int i=2; i<=n/2; i++)
		if(isPrime(i) && isPrime(n-i))
			count++;
	isPrime(n/2) and n%2 == 0 ? cout << 2*count - 1 : cout << 2*count;
	return 0;
}

