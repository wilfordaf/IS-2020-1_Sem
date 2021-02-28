#include <stdio.h>
#include <stdlib.h>
#include <string.h> // ���������� �������������� ���������� ��� ������ �� ��������

int main()
{
    char str1[50], str2[50], ch, str3[50]; // ��������� 2 ������, ������, ������ ��������� �������� ����� ���������� �����, � ���. ������
    char *ans1, *ans2; //

    scanf("%s %s %c", &str1, &str2, &ch); // ���� �� ������� 2 ����� � �������
    strcpy(str3, str1); // �������� ���. ������ �������� ����������� ������ ��� �������� ���������� ��������

    printf("Concatenation: %s \n", strcat(str1, str2)); // 1 �������, ������� � ������� ��������� ������������

    if (strcmp(str3, str2) != 0){
        printf("Comparison: False \n"); // 2 ������� ������� � ������� ��������� ��������� 2 �������� �����
    }
    else{
        printf("Comparison: True \n");
    }


    ans1 = strchr(str1, ch); // 3 �������, ������� � ������� ����� �������, ��������� �����
    printf("Number of %c is: %d\n", ch, strlen(str1)-strlen(ans1)+1);


    ans2 = strpbrk(str3,str2); //4 �������, ������� � ������� ����� ������� ��������� ������ �� �������� ������ ������ �� 2
    printf("Number of similar char in %s and %s is: %d\n", str3, str2, strlen(str3)-strlen(ans2)+1);


    printf("Length of the part of the %s that doesn't consist any from the %s is: %d\n", str3, str2, strcspn(str3,str2)); // 5 �������, ������� � ������� ����� ������� 1 ������, ������� �� �������� �������� ������ ������
    return 0;
}
