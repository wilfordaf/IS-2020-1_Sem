#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char* third_task(int digit){ // 3 задание
    const char *str[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}; // массив со словестной интерпретацией цифр
    return(str[digit]); // возвращаем цифру соответствующую номеру

}
float* fifth_task(int months, int percent, float beginning){ // 5 задание
    float bet;
    float* str;
    bet = (float)percent/100; // считаем процентную ставку
    for(int i = 1; i <= months; i++){ // в цикле домножаем начальную сумму на ставку и добавляем значение в массив
        beginning *= (1+(float)percent/100);
        str[i-1] = beginning;
    }
    return str; // возвращаем массив
}
int main()
{
    int digit;
    scanf("%d", &digit); // вводим с клавиатуры цифру
    printf("Your digit is - %s", third_task(digit)); // выводим на консоль словестную интерпретацию
    int months, percent;
    float beginning;
    scanf("%d", &months); // вводим с клавиатуры данные
    scanf("%d", &percent);
    scanf("%f", &beginning);
    float* str = fifth_task(months, percent, beginning);
    for(int i = 1; i <= months; i++){ // выводим циклом
        printf("Month is: %d, Sum is: %f\n", i, str[i-1]);
    }
    return 0;
}
