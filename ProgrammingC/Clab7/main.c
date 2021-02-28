#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct dot {
    double x;
    double y;
};
struct triangle {
    struct dot A;
    struct dot B;
    struct dot C;
};
double lenght(const struct dot *a, const struct dot *b){
    double len = sqrt(pow(a->x - b->x, 2)+pow(a->y - b->y, 2));
    return len;
}
double area(const struct triangle *t){
    double a = lenght(&t->A, &t->B);
    double b = lenght(&t->B, &t->C);
    double c = lenght(&t->A, &t->C);
    double p = (a+b+c)/2;
    return sqrt(p*(p-a)*(p-b)*(p-c));
}
union{
    int cardreader;
    struct{
        int elements: 1;
        int sd: 1;
        int compactflash: 1;
        int memoystick: 1;
    } bit_Field;

} device;
void main()
{
    enum lamps {
        filament, daylight, halogen
    };
    enum lamps chosen  = halogen;
    printf("%d\n", chosen);

    struct dot A = {0,0};
    struct dot B = {0,3};
    struct dot C = {4,0};
    struct triangle t = {A,B,C};
    printf("%lf", area(&t));

    scanf("%X", &device.cardreader);
    printf("%d %d %d %d", abs(device.bit_Field.elements), abs(device.bit_Field.sd), abs(device.bit_Field.compactflash), abs(device.bit_Field.memoystick));

}
