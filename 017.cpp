//Author: R.U.S.T.E.A.M
#include <bits/stdc++.h>

using namespace std;

long long int yig(long long int n)
{
	int s = 0;
	while(n>0)
	{
		s += n%10;
		n /= 10;
	}
	return s;
}

int main()
{
	int n, k=0;
	cin>>n;
	long long int i = 1;
	while(k<n)
	{
		if(i % (yig(i) * yig(i)) == 0)
			k += 1;
		i++;
	}
	cout<<i-1;
	return 0;
}

