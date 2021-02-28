#ifndef RIGHTRIANGLE_H_INCLUDED
#define RIGHTRIANGLE_H_INCLUDED


struct dot { // структура точки
    double x;
    double y;
};

struct triangle { //структура треугольника
    struct dot A;
    struct dot B;
    struct dot C;
};

struct side { // структура стороны(вектор)
    double x;
    double y;

};

struct dot new_dot(double, double); //создание точки
struct side new_side(struct dot, struct dot); // создание стороны
struct triangle new_triangle(struct dot, struct dot, struct dot); // создание треугольника
double lenght(struct side);
double area(struct triangle);
double per(struct triangle);

#endif // RIGHTRIANGLE_H_INCLUDED
