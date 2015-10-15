#include "Python.h"

static PyObject* is_perfect(PyObject *self, PyObject *args) {
    unsigned long n ,i, sum=0;
    if (!PyArg_ParseTuple(args, "k", &n))
        return NULL;
    for (i=1; i < n; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }
    if (sum == n) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}


static PyMethodDef CPerfectMethods[] = {
    {
        "is_perfect",
        is_perfect,
        METH_VARARGS,
        "Check if number is perfect with GIL"
    },
    {NULL, NULL, 0, NULL},        /* Sentinel */
};

static struct PyModuleDef cperfectmodule = {
    PyModuleDef_HEAD_INIT,
    "cperfect",   /* name of module */
    "Perfect functions in C", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    CPerfectMethods,
};

PyMODINIT_FUNC PyInit_cperfect(void) {
        return PyModule_Create(&cperfectmodule);
}
