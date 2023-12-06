#include <time.h>
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - to print python list info
 * @p: argument
 *
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *obj;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; ++i)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
