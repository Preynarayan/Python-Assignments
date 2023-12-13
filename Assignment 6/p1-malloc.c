#include <stdio.h>
#include <stdlib.h>

int main()
{
  int numInts = 5;
  int *ptr;

  ptr = malloc(numInts * sizeof(int));

  ptr[0]   = 10;
  ptr[1]   = 20;
  ptr[2]   = 30;
  *(ptr + 3) = 40;
  *(ptr + 4) = 50;

  for (int i=0; i<numInts; ++i)
    printf("%d ", ptr[i]);

  printf("\n\n");

  for (int i=0; i<numInts; ++i, ++ptr)
    printf("%d ", *ptr);

  printf("\n\n");

  return 0;
}

