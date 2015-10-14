#include "Python.h"

static PyObject* test_collatz(PyObject *self, PyObject *args) {
    unsigned long x;
    if (!PyArg_ParseTuple(args, "k", &x))
        return NULL;
    while (x != 1 ) {
        if (x % 2) {
            x = x * 3 + 1;
        } else {
            x /= 2;
        }
    }
    Py_RETURN_NONE;
}

static PyObject* test_collatz_nogil(PyObject *self, PyObject *args) {
    unsigned long x;
    if (!PyArg_ParseTuple(args, "k", &x))
        return NULL;
    Py_BEGIN_ALLOW_THREADS;
    while (x != 1 ) {
        if (x % 2) {
            x = x * 3 + 1;
        } else {
            x /= 2;
        }
    }
    Py_END_ALLOW_THREADS;
    Py_RETURN_NONE;
}

static PyMethodDef CCollatzMethods[] = {
    {
        "test_collatz",
        test_collatz,
        METH_VARARGS,
        "Check number for collatz with GIL"
    },
    {
        "test_collatz_nogil",
        test_collatz_nogil,
        METH_VARARGS,
        "Check number for collatz without GIL"
    },
    {NULL, NULL, 0, NULL},        /* Sentinel */
};

static struct PyModuleDef ccollatzmodule = {
    PyModuleDef_HEAD_INIT,
    "ccollatz",   /* name of module */
    "Collatz functions in C", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    CCollatzMethods,
};

PyMODINIT_FUNC PyInit_ccollatz(void) {
        return PyModule_Create(&ccollatzmodule);
}
