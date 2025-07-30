#include <string.h>

int convert(char c){
    if (c == 'I'){
        return 1;
    } else if (c == 'V'){
        return 5;
    }else if (c == 'X'){
        return 10;
    }else if (c == 'L'){
        return 50;
    }else if (c == 'C'){
        return 100;
    }else if (c == 'D'){
        return 500;
    }else if (c == 'M'){
        return 1000;
    }
    return 0;
}

int romanToInt(char* s) {
    int b = 0, f = 1;
    int intB = 0, intF = 0, intSum = 0;
    while (f < strlen(s)){
        //printf("sum: %d\n", intSum);
        intB = convert(s[b]);
        intF = convert(s[f]);
        if(intB < intF){
            intSum -= intB;
        } else {
            intSum += intB;
        }
        b++;
        f++;
    }
    return intSum + convert(s[b]);
}