#include <stdio.h>
#include "rightriangle.h" // подключаем файлы со структурами и формулами


int main()
{
    struct dot a, b, c; // создаём структуры 3 точек треугольника
    scanf("%lf %lf %lf %lf %lf %lf", &a.x, &a.y, &b.x, &b.y, &c.x, &c.y); // вводим их координаты
    struct triangle t = new_triangle(a,b,c); // создаём треугольник
    printf("Perimeter of such triangle is: %f, Square: %f", per(t), area(t)); // выводим переметр и площадь
    return 0;
}
