#include <stdio.h>
#include <string.h>

void makearchive(char* filename, int amountoffiles, char* files[]){ //создание архива
    int sizeofname; // размер названия файла
    int sizeofcontent; // размер содержимого файла
    FILE *file;
    file = fopen(filename, "w");
    for (int i = 0; i < amountoffiles; i++){
        sizeofname = strlen(files[i]);
        fputc(sizeofname, file); // записываем размер имени файла
        for (int j = 0; j < sizeofname; j++) // записываем имя файла
            fputc(files[i][j], file);
        FILE *filearchived;
        filearchived = fopen(files[i], "r"); // открываем один из файлов, которые необходимо заархивировать
        fseek(filearchived, 0, SEEK_END);
        sizeofcontent = ftell(filearchived); // размер содержимого этого файла
        fseek(filearchived, 0, SEEK_SET);
        fwrite(&sizeofcontent, 4, 1, file); // записываем размер файла
        for (int j = 0; j < sizeofcontent; j++)
            fputc(getc(filearchived), file); // записываем его содержимое
    }
    fclose(file);
}

void extractarchive(char* filename){ // разархивация
    FILE *file;
    file = fopen(filename, "r");
    fseek(file, 0, SEEK_END);
    int endoffile = ftell(file); // размер файла
    fseek(file, 0, SEEK_SET);
    while(ftell(file) < endoffile){ // читаем весь файл
        int bufferforsize = getc(file); // из записанных данных берём размер названия файла
        char newfilename[bufferforsize]; // теперь само название файла
        for (int i = 0; i < bufferforsize; i++)
            newfilename[i] = getc(file); // записываем его
        fread(&bufferforsize, 4, 1, file); // записываем размер содержимого этого файла
        FILE *new_file;
        new_file = fopen(newfilename, "w"); // создаём файл с таким названием на запись
        for (int i = 0; i < bufferforsize; i++) // записываем содержимое из архива
            fputc(getc(file), new_file);
        fclose(new_file);
    }
}

void listarchive(char* filename){ // список заархивированных файлов
    FILE *file;
    file = fopen(filename, "r");
    fseek(file, 0, SEEK_END);
    int endoffile = ftell(file); // размер файла
    fseek(file, 0, SEEK_SET);
    while(ftell(file) < endoffile){
        int size = getc(file); // размер названия файла
        char newfilename[size]; // название файла
        for (int i = 0; i < size; i++) // записываем его
            newfilename[i] = getc(file);
        printf("%s\n", newfilename); // выводим название на косоль
        fread(&size, 4, 1, file);
        fseek(file, size, SEEK_CUR);
    }
}

int main (int argc, char* argv[]){
    if (!(strcmp(argv[3], "--create"))){
        int amountoffiles = argc - 4;
        makearchive(argv[2], amountoffiles, &argv[4]);
    }
    else if (!(strcmp(argv[3], "--extract"))){
        extractarchive(argv[2]);
    }
    else if (!(strcmp(argv[3], "--list"))){
        listarchive(argv[2]);
    }
    return 0;
}