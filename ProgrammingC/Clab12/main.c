#include <stdio.h>
#include <stdlib.h>


void concatenation(char *argv[]){ // ������� ������������ 2 ������
    FILE *new_file = fopen(argv[3], "w"); // ��������� ����, � ������� ����� �������� ������������
    for(int i = 1; i <= 2; i++){ // � ����� ��������� �����, ������� ����� ����������, � ���������� ����������� � 3 ����
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

void main(int argc, char *argv[]){ // ��������� ������������ �� ���������� main
    concatenation(argv);
}
