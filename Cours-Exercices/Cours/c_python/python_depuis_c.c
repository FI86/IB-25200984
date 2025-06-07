#include <Python.h>

int main() {
    Py_Initialize();  // Démarre l'interpréteur

    PyRun_SimpleString("print('Bonjour de Python dans C !')");
    PyRun_SimpleString("input('Appuyez sur Entrée pour quitter')");

    Py_Finalize();    // Termine l'interpréteur
    return 0;
}
