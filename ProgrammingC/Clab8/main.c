#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Подключаем дополнительную библиотеку для работы со строками

int main()
{
    char str1[50], str2[50], ch, str3[50]; // Объявляем 2 строки, символ, первое вхождение которого будет необходимо найти, и доп. строку
    char *ans1, *ans2; //

    scanf("%s %s %c", &str1, &str2, &ch); // Ввод из консоли 2 строк и символа
    strcpy(str3, str1); // копируем доп. строку значение изначальной строки для удобства дальнейших операций

    printf("Concatenation: %s \n", strcat(str1, str2)); // 1 задание, выводим в консоль результат конкатенации

    if (strcmp(str3, str2) != 0){
        printf("Comparison: False \n"); // 2 задание выводим в консоль результат сравнения 2 введённых строк
    }
    else{
        printf("Comparison: True \n");
    }


    ans1 = strchr(str1, ch); // 3 задание, выводим в консоль номер символа, введённого ранее
    printf("Number of %c is: %d\n", ch, strlen(str1)-strlen(ans1)+1);


    ans2 = strpbrk(str3,str2); //4 задание, выводим в консоль номер первого вхождения любого из символов первой строки во 2
    printf("Number of similar char in %s and %s is: %d\n", str3, str2, strlen(str3)-strlen(ans2)+1);


    printf("Length of the part of the %s that doesn't consist any from the %s is: %d\n", str3, str2, strcspn(str3,str2)); // 5 задание, выводим в консоль длину отрезка 1 строки, который не содержит символов второй строки
    return 0;
}
