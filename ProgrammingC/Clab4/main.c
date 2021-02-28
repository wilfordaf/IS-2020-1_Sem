#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, num;
    scanf("%d",&x);
    printf ("%d\n", -56 <= x && x <= 56);
    scanf ("%X",&num);
    printf ("%d", (num >> 8)&1);
    return 0;
}
