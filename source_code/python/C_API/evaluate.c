#include <Python.h>

//실제 사용할 C 함수 average_c
float average_c(int * scores, int arr_size)
{
	int sum = 0;
	for (int i = 0; i < arr_size; i++)
		sum += scores[i];

	float mean = (float)sum / arr_size;

	return mean;
}

//실제 사용할 C 함수 variance_c
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


//python 함수에서 인자를 받아 c 자료형으로 바꾼 후 연산
//연산이 끝나면 다시 python 변수로 변환하여 반환
//실제 python 모듈은 이 함수를 호출한다
static PyObject * average(PyObject * self, PyObject * args)
{
	printf("avarage() in cpp is running \n");
	PyObject * scores;
	//한 반에 100명은 안 넘겠지.....
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

//모듈의 함수 테이블
static PyMethodDef evaluateMethods[] = {
	{ "average", (PyCFunction)average, METH_VARARGS, "calculate an average" },
	{ "variance", (PyCFunction)variance, METH_VARARGS, "calculate a variance" },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef evaluatemodule = {
	PyModuleDef_HEAD_INIT,
	"evaluate",//모듈 이름
	"calculate average, variance",//모듈 설명
	-1,
	evaluateMethods//모듈의 함수 테이블 등록
};

PyMODINIT_FUNC
PyInit_evaluate(void)
{
	return PyModule_Create(&evaluatemodule);//모듈 생성
}
