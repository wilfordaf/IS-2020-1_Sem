#include <stdio.h>
#include <stdlib.h>

int length_of_number(int num){ // ф-я, считающая длину числа
    int len = 0;
    while(num != 0){
        len++;
        num /= 10;
        }
    return len;
}

int* third_task(int num){ // берём остаток от деления числа на 10, записываем в массив, целочисленно делим на 10
    int len = length_of_number(num);
    int* arr = malloc(sizeof(int)*len);
    int pointer = len-1;
    while(num != 0){
        int digit = num%10;
        arr[pointer] = digit;
        pointer--;
        num /= 10;
    }
    return arr; // вовзращаем массив
}

void del(char* str, int pointer){ // удаление символа и сдвиг строки
    int i;
    for(i = pointer+1; i< strlen(str); i++){
        str[i-1] = str[i];
    }
    str[strlen(str)-1] = "\0";
}

char* fifth_task(char* str, int i){ // удаление двойных пробелов и пробелов в конце строки
    int space = 0;
    if (i >= strlen(str)){
        if (str[i-1] == ' '){
            del(str, i-1);
        }
        return str;
    }
    else{
        if (str[i-1] == ' '){
            space++;
        }
        if(str[i] == ' ' && space > 0){
            del(str, i);
        }
        else{
            i++;
        }
        return fifth_task(str, i);
    }
}

int main()
{
    int num;
    scanf("%d", &num); // вводим цифру
    int* arr = third_task(num);
    int len = length_of_number(num);
    for(int i = 0; i < len; i++){ // печатаем список цифр числа
        printf("%d ", arr[i]);
    }
    free(arr);
    char str[100] = "Hello,   World  !   "; // задаём строку
    printf("\n%s ", fifth_task(str, 1)); // используем функцию от строки
    return 0;
}
