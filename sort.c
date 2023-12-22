// https://www.onlinegdb.com/
#include <stdio.h>
#include <assert.h>

void swap(int t[], int n, int i, int j){
    int temp = t[i];
    t[i] = t[j];
    t[j] = temp;
}



int main(){
    int t[4] = {1, 3, 7, 9};
    printf("{%d, %d, %d, %d}\n", t[0], t[1], t[2], t[3]);
    printf("  swaping...\n");
    swap(t, 4, 1, 2);
    printf("{%d, %d, %d, %d}\n", t[0], t[1], t[2], t[3]);
    return 0;
}
