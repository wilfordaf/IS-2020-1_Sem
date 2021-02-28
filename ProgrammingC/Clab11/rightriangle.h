#ifndef RIGHTRIANGLE_H_INCLUDED
#define RIGHTRIANGLE_H_INCLUDED


struct dot { // ��������� �����
    double x;
    double y;
};

struct triangle { //��������� ������������
    struct dot A;
    struct dot B;
    struct dot C;
};

struct side { // ��������� �������(������)
    double x;
    double y;

};

struct dot new_dot(double, double); //�������� �����
struct side new_side(struct dot, struct dot); // �������� �������
struct triangle new_triangle(struct dot, struct dot, struct dot); // �������� ������������
double lenght(struct side);
double area(struct triangle);
double per(struct triangle);

#endif // RIGHTRIANGLE_H_INCLUDED
