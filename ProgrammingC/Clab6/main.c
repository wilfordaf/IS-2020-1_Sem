#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

int main()
{
    int arr[4], *p = arr;
    arr[0] = 1000;
    arr[1] = 1001;
    arr[2] = 1002;
    arr[3] = 1003;
    for(int i = 0; i < 4; i++)
    {
        printf("%d %d\n", i, *(p+i));
    }
    printf("---\n");
    int *a;
    a = (int*)malloc(4*sizeof(int));
    a[0] = 1000;
    a[1] = 1001;
    a[2] = 1002;
    a[3] = 1003;
    for(int i = 0; i < 4; i++)
    {
        printf("%d %d\n", i, a[i]);
    }
    free(a);
    return 0;
}
