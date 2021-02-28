#include <stdio.h>
#include <stdlib.h>

int main()
{
int arr[8]={77,12,74,34,56,78,234,678};
for(int i = 0; i < 8; i++)
{
    printf("%d %d\n", i, arr[i]);
}
int mtrx1[2][2]=
{
    {2,1},
    {1,3}
};
int mtrx2[2][2]=
{
    {1,2},
    {3,1}
};
int mtrx3[2][2];
mtrx3[0][0]=mtrx1[0][0]*mtrx2[0][0]+mtrx1[0][1]*mtrx2[1][0];
mtrx3[0][1]=mtrx1[0][0]*mtrx2[0][1]+mtrx1[0][1]*mtrx2[1][1];
mtrx3[1][0]=mtrx1[1][0]*mtrx2[0][0]+mtrx1[1][1]*mtrx2[1][0];
mtrx3[1][1]=mtrx1[1][0]*mtrx2[0][1]+mtrx1[1][1]*mtrx2[1][1];
printf("%d %d\n%d %d", mtrx3[0][0], mtrx3[0][1], mtrx3[1][0], mtrx3[1][1]);

return 0;
}
