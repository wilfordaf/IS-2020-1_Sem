#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    float x, y, z1, z2;
    scanf("%f %f",&x,&y);
    z1 = pow(cos(x),4) + pow(sin(y),2) + 0.25 * pow(sin(2*x),2)-1;
    z2 = sin(y+x)*sin(y-x);
    printf("%f\n%f",z1,z2);
    return 0;
}
