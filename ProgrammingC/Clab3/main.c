#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, number, out;
    scanf_s("%d", &num);
    printf_s("%o\n", num);
    printf_s("%X %X\n", num, num >> 4);
    printf_s("%X %X\n", num, ~num);
    scanf_s("%X", &number);
    out = num^number;
    printf_s("%X\n", out);
    return 0;
}
