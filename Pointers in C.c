#include <stdio.h>

void update(int *a,int *b) {
        int sum = (*a)+(*b);
        int diff = 0;
        if(*b>*a){
            diff = (*b)-(*a);
        }
        else if(*a>*b){
            diff = (*a)-(*b);
        }
        printf("%d\n",sum);
        printf("%d",diff);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    return 0;
}
