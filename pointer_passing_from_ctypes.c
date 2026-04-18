#include<stdio.h>

void double_int(int* x)
{
     *x = *x * 2;
}

void linear_sort(int* arr,int n)
{int temp;
    for (int i = 0; i < n; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if(arr[i]>arr[j])
            {temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;}
        }
    }
}

void add_matrix(int rows, int cols, int *A, int *B, int *C)
{
    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < cols; j++)
        {
            C[i * cols + j] = A[i * cols + j] + B[i * cols + j];
        }
    }
}