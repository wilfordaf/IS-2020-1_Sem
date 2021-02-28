#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char* third_task(int digit){ // 3 �������
    const char *str[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}; // ������ �� ���������� �������������� ����
    return(str[digit]); // ���������� ����� ��������������� ������

}
float* fifth_task(int months, int percent, float beginning){ // 5 �������
    float bet;
    float* str;
    bet = (float)percent/100; // ������� ���������� ������
    for(int i = 1; i <= months; i++){ // � ����� ��������� ��������� ����� �� ������ � ��������� �������� � ������
        beginning *= (1+(float)percent/100);
        str[i-1] = beginning;
    }
    return str; // ���������� ������
}
int main()
{
    int digit;
    scanf("%d", &digit); // ������ � ���������� �����
    printf("Your digit is - %s", third_task(digit)); // ������� �� ������� ���������� �������������
    int months, percent;
    float beginning;
    scanf("%d", &months); // ������ � ���������� ������
    scanf("%d", &percent);
    scanf("%f", &beginning);
    float* str = fifth_task(months, percent, beginning);
    for(int i = 1; i <= months; i++){ // ������� ������
        printf("Month is: %d, Sum is: %f\n", i, str[i-1]);
    }
    return 0;
}
