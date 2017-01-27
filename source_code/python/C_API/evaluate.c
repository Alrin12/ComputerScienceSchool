#include <Python.h>

//���� ����� C �Լ� average_c
float average_c(int * scores, int arr_size)
{
	int sum = 0;
	for (int i = 0; i < arr_size; i++)
		sum += scores[i];

	float mean = (float)sum / arr_size;

	return mean;
}

//���� ����� C �Լ� variance_c
float variance_c(int * scores, int arr_size, int avrg)
{
	int sum = 0;
	int sq_d = 0;
	for (int i = 0; i < arr_size; i++)
	{
		sq_d = (scores[i] - avrg) * (scores[i] - avrg);
		sum += sq_d;
	}
	float var = (float)sum / arr_size;
	return var;
}


//python �Լ����� ���ڸ� �޾� c �ڷ������� �ٲ� �� ����
//������ ������ �ٽ� python ������ ��ȯ�Ͽ� ��ȯ
//���� python ����� �� �Լ��� ȣ���Ѵ�
static PyObject * average(PyObject * self, PyObject * args)
{
	printf("avarage() in cpp is running \n");
	PyObject * scores;
	//�� �ݿ� 100���� �� �Ѱ���.....
	int scoreArr[100];
	if (!PyArg_ParseTuple(args, "O", &scores))
	{
		printf("PyArg_ParseTuple() error! in average ");
		exit(-1);
	}

	const int lenOfList = PyList_Size(scores);

	for (int i = 0; i < lenOfList; i++)
	{
		PyObject * PyValue;

		PyValue = PyList_GetItem(scores, i);
		scoreArr[i] = _PyLong_AsInt(PyValue);
	}

	float avrg = average_c(scoreArr, lenOfList);

	return Py_BuildValue("f", avrg);

}

static PyObject * variance(PyObject * self, PyObject * args)
{
	printf("variance() in cpp is running!!! \n");
	PyObject * scores;
	int scoreArr[100];

	if (!PyArg_ParseTuple(args, "O", &scores))
	{
		printf("PyArg_ParseTuple() error! in variance");
		exit(-1);
	}

	int lenOfList = PyList_Size(scores);

	for (int i = 0; i < lenOfList; i++)
	{
		PyObject * PyValue;
		PyValue = PyList_GetItem(scores, i);

		scoreArr[i] = _PyLong_AsInt(PyValue);
	}
	float avrg = average_c(scoreArr, lenOfList);
	float var = variance_c(scoreArr, lenOfList, avrg);

	return Py_BuildValue("f", var);
}

//����� �Լ� ���̺�
static PyMethodDef evaluateMethods[] = {
	{ "average", (PyCFunction)average, METH_VARARGS, "calculate an average" },
	{ "variance", (PyCFunction)variance, METH_VARARGS, "calculate a variance" },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef evaluatemodule = {
	PyModuleDef_HEAD_INIT,
	"evaluate",//��� �̸�
	"calculate average, variance",//��� ����
	-1,
	evaluateMethods//����� �Լ� ���̺� ���
};

PyMODINIT_FUNC
PyInit_evaluate(void)
{
	return PyModule_Create(&evaluatemodule);//��� ����
}
