// cmult.c

#include <stdio.h>

float cmult(int int_parm, float float_parm) {
    float result = int_parm * float_parm;
    printf("    In cmult: int: %d, float %.1f returning %.1f\n", int_parm, 
            float_parm, result);
    return result;
}
