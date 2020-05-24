#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    int sum=0;
    int x=0;
    int count=1;
    for(int i=0;i<5;i++)
    {
        x=n%10;
        n/=10;
        sum+=x;
    }
    printf("%d",sum);
    return 0;
}
