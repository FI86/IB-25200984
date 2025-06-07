// fichier: exemple.c
#include <stdio.h>

// affichage
__declspec(dllexport) void bonjour() {
    printf("Bonjour depuis le C !\n");
}

// fichier: addition.c
__declspec(dllexport) int addition(int a, int b) {
    return a + b;
}
