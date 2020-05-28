#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    int t;
    cin>>t;
    int a[1000];
    for(int i=0; i<t; i++)
    {
        cin>>a[t-i-1];  
    }
    for(int j=0; j<t; j++)
    {
        cout<<a[j]<<" ";
    }  
    return 0;
}
