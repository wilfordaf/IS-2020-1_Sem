#include <stdio.h>
#include <stdlib.h>


void concatenation(char *argv[]){ // функция конкатенации 2 файлов
    FILE *new_file = fopen(argv[3], "w"); // открываем файл, в который нужно записать конкатенацию
    for(int i = 1; i <= 2; i++){ // в цикле открываем файлы, которые нужно объединить, и записываем посимвольно в 3 файл
        FILE *file = fopen(argv[i], "r");
        while(1){
            char c = fgetc(file);
            if (c==EOF){
                break;
            }
            fprintf(new_file, "%c", c);
            fclose(argv[i]);
        }
        fprintf(new_file, "%c", '\n');
    }
    fclose(argv[3]);
}

void main(int argc, char *argv[]){ // запускаем конкатенацию от аргументов main
    concatenation(argv);
}
