// fichier: carre_module.c
#include <Python.h>

static PyObject* carre(PyObject* self, PyObject* args) {
    int x;
    if (!PyArg_ParseTuple(args, "i", &x)) return NULL;
    return PyLong_FromLong(x * x);
}

static PyMethodDef CarreMethods[] = {
    {"carre", carre, METH_VARARGS, "Calcule le carré"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef carre_module = {
    PyModuleDef_HEAD_INIT,
    "carre_module",
    NULL,
    -1,
    CarreMethods
};

PyMODINIT_FUNC PyInit_carre_module(void) {
    return PyModule_Create(&carre_module);
}
