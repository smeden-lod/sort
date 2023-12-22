#include <stdio.h>

void swap(int t[], int n, int i, int j){
    int temp = t[i];
    t[i] = t[j];
    t[j] = temp;
}

void affiche_tableau(int t[], int n){
    printf("{");
    for (int i = 0; i <n-1; i++){
        printf("%d, ", t[i]);
    }
    printf("%d}\n", t[n-1]);
}

int imini(int t[], int n, int k){
    // t tableau d'entiers de taille n
    // renvoie l'indice du min dans t à partir de k
    int indm = k;
    int m = t[k];
    for (int i = k+1; i<n ; i++){
        if (t[i] < m){
            m = t[i];
            indm = i;
        }
    }
    return indm;
}

 
void tri_selection(int tab[], int n){
    for (int i=0; i<n ; i++){
        swap(tab, n, i, imini(tab, n, i));
    }
}

int main(){
    int tab[7] = {89, 12, 33, 456, 27, 987, 42};
    affiche_tableau(tab, 7);
    tri_selection(tab, 7);
    affiche_tableau(tab, 7);
    return 0;
}
