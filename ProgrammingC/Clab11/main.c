#include <stdio.h>
#include "rightriangle.h" // ���������� ����� �� ����������� � ���������


int main()
{
    struct dot a, b, c; // ������ ��������� 3 ����� ������������
    scanf("%lf %lf %lf %lf %lf %lf", &a.x, &a.y, &b.x, &b.y, &c.x, &c.y); // ������ �� ����������
    struct triangle t = new_triangle(a,b,c); // ������ �����������
    printf("Perimeter of such triangle is: %f, Square: %f", per(t), area(t)); // ������� �������� � �������
    return 0;
}
