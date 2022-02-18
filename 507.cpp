//Author: R.U.S.T.E.A.M
#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n;
	cin>>n;
	int a[n], s=0;
	for(int i=0;i<n;i++)
		cin>>a[i];
	for(int i=0;i<n-2;i++)
		for(int j=i+1;j<n-1;j++)
			for(int k=j+1;k<n;k++)
				if(a[i]<a[j] && a[j]<a[k])
					if(a[i] + a[j] + a[k] > s)
						s = a[i] + a[j] + a[k];
	cout<<s;
	return 0;
}
