#include <stdio.h>
int func(void);

#define MAX 10
int main(int argc, char **argv)
{
    printf("Hello world! %d\n", func());
    return 0;
}
