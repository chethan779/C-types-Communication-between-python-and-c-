import ctypes as ct
import tkinter as tk


root=tk.Tk()
root.geometry("800x900")

matrix_frame=tk.Frame(root)
matrix_frame.place(relx=0.5,rely=0.1,anchor="n")

row1 = int(input("Enter number of rows in Matrix A: "))
col1 = int(input("Enter number of column in Matrix A: "))
row2= int(input("Enter number of rows in Matrix B: "))
col2=int(input("Enter number of column in Matrix B: "))


tk.Label(matrix_frame,text="Enter Values In Matrix A").grid(row=0,column=0,columnspan=5)

matrix_A=[]

for i in range(row1):
    row_entries1=[]
    
    for j in range(col1):
        entry1=tk.Entry(matrix_frame,width=5,font=('Arial',16),justify='center')
        entry1.grid(row=i+1,column=j,padx=2,pady=2)

        row_entries1.append(entry1)
    matrix_A.append(row_entries1)

start_row_B=row1+3

tk.Label(matrix_frame,text="Enter Values In Matrix B").grid(row=start_row_B,column=0,columnspan=5)

matrix_B=[]

for i in range(row2):
    row_entries2=[]
    for j in range(col2):
        entry2=tk.Entry(matrix_frame,width=5,font=('Arial',16),justify='center')
        entry2.grid(row=start_row_B+i+1,column=j,padx=2,pady=2)
        row_entries2.append(entry2)
    matrix_B.append(row_entries2)

start_row_C=start_row_B+row2+3

def multiply_matrices():
    lib=ct.CDLL("./matrix_op.dll")

    A=[]
    for i in range(row1):
        for j in range(col1):
            A.append(int(matrix_A[i][j].get()))

    B=[]
    for i in range(row2):
        for j in range(col2):
            B.append(int(matrix_B[i][j].get()))

    Array_Type1=ct.c_int * (row1*col1)
    Array_Type2=ct.c_int * (row2*col2)
    Array_Type3=ct.c_int * (row1*col2)

    a=Array_Type1()
    b=Array_Type2()
    c=Array_Type3()

    lib.multiply_matrix.argtypes=[ct.c_int,ct.c_int,ct.c_int,ct.c_int,ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int)]
    lib.multiply_matrix.restype=None

    lib.mutiplication_matrix(row1,col1,row2,col2,a,b,c)

    for i in range(row1):
        for j in range(col2):
            value=c[i * col2 + j]

            label=tk.Label(matrix_frame,text=str(value),width=6,font=('Arial', 16),relief="solid")
            label.grid(row=start_row_C+i+1,column=j,padx=2,pady=2)

evaluate_btn=tk.Button(matrix_frame,text="EVALUATE",command=multiply_matrices).grid(row=start_row_C,column=0,columnspan=5)

root.mainloop()