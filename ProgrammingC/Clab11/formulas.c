#include "rightriangle.h"
#include <math.h>

struct dot new_dot(double a, double b){ //�������� �����
    struct dot d;
    d.x = a;
    d.y = b;
    return d;
}

struct side new_side(struct dot a, struct dot b){ // �������� �������
    struct side s;
    s.x = a.x-b.x;
    s.y = a.y-b.y;
    return s;
}

struct triangle new_triangle(struct dot A, struct dot B, struct dot C){ // �������� ������������
    struct triangle t;
    t.A = A;
    t.B = B;
    t.C = C;
    return t;
}

double lenght(struct side s){ // ������� �������� ����� �������
    return sqrt(s.x*s.x + s.y*s.y);
}

double area(struct triangle t){ // ������� �������� ������� �������������� ������������
    double a = lenght(new_side(t.A, t.B));
    double b = lenght(new_side(t.B, t.C));
    return 0.5*a*b;
}
double per(struct triangle t){ // ������� �������� ��������� ������������
    double a = lenght(new_side(t.A, t.B));
    double b = lenght(new_side(t.B, t.C));
    double c = lenght(new_side(t.A, t.C));
    return a+b+c;
}
