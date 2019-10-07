#include <Python.h>

static PyObject *StringTooShortError = NULL;

static PyObject *method_fputs(PyObject *self, PyObject *args);

static PyMethodDef FputsMethods[] = {
    {"fputs", method_fputs, METH_VARARGS, "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fputsmodule = {
    PyModuleDef_HEAD_INIT,
    "fputs",
    "Python interface for the fputs C library function",
    -1,
    FputsMethods
};

PyMODINIT_FUNC PyInit_fputs(void) {
    PyObject *module = PyModule_Create(&fputsmodule);

    /* initialize new exception object */
    StringTooShortError = PyErr_NewException("fputs.StringTooShortError", NULL, NULL);

    /* add exception object to the module */
    PyModule_AddObject(module, "StringTooShortError", StringTooShortError);

    return module;
}

static PyObject *method_fputs(PyObject *self, PyObject *args) {
    char *str, *filename = NULL;
    int bytes_copied = -1;

    /* Parse arguments */
    if (!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

	/* an arbitrtary requirement to demonstrate creating an exception */
    if (strlen(str) < 10) {
        /* Generate a custom exception */
        PyErr_SetString(StringTooShortError, "String length must be greater than 10 characters.");
        return NULL;
    }

    FILE *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    return PyLong_FromLong(bytes_copied);
}
