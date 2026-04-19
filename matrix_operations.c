#include<stdio.h>

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


void subtract_matrix(int rows, int cols, int *A, int *B, int *C)
{
    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < cols; j++)
        {
            C[i * cols + j] = A[i * cols + j] - B[i * cols + j];
        }
    }
}


void multiply_matrix(int rows1, int cols1, int rows2, int cols2, int *A, int *B, int *C)
{int sum;
    if(cols1==rows2)
    {
    for(int i = 0; i < rows1; i++)
        {
            for(int j = 0; j < cols2; j++)
                {sum=0;
                    for (int k = 0; k < rows2; k++)
                        {
                            sum=sum+(A[i * cols1 + k]*B[k * cols2 + j]);
                        }
                        C[i * cols2 + j]=sum;
                }
        }
    }
    
}