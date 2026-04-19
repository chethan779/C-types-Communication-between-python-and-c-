import tkinter as tk

root = tk.Tk()
root.geometry("800x900")


row1 = int(input("Enter number of rows: "))
col1 = int(input("Enter number of column: "))
row2= int(input("Enter number of rows: "))
col2=int(input("Enter number of column: "))

matrix_frame = tk.Frame(root)
matrix_frame.place(relx=0.5, rely=0.1, anchor="n")

tk.Label(matrix_frame, text="Enter the value in Matrix A:").grid(row=0, column=0, columnspan=col1)

entries1 = []

for i in range(row1):
    row_entries = []

    for j in range(col1):
       e = tk.Entry(matrix_frame, width=9,font=('Arial',16) ,justify='center')
       e.grid(row=i+1, column=j, padx=2, pady=2)

       row_entries.append(e)

    entries1.append(row_entries)
start_row_B = row1 + 3
tk.Label(matrix_frame, text="Enter the value in Matrix B:").grid(row=start_row_B, column=0, columnspan=col2)


entries2 = []

for i in range(row2):
    row_entries = []

    for j in range(col2):
       e = tk.Entry(matrix_frame, width=9,font=('Arial',16) ,justify='center')
       e.grid(row=start_row_B+i+1, column=j, padx=2, pady=2)

       row_entries.append(e)

    entries2.append(row_entries)

end_row_B=start_row_B+row2+3

def multiplication_matrix():
    import ctypes as ct

    lib=ct.CDLL("./matrix_op.dll");

    matrix1=[]
    for i in range(row1):
        for j in range(col1):
            matrix1.append(int(entries1[i][j].get()))
    matrix2=[]
    for i in range(row1):
        for j in range(col1):
            matrix2.append(int(entries1[i][j].get()))

    ArrayType1 = ct.c_int * (row1 * col1)
    ArrayType2 = ct.c_int * (row2 * col2)
    ArrayType3 = ct.c_int * (row1 * col2)
    matrix_a=ArrayType1(*matrix1)
    matrix_b=ArrayType2(*matrix2)
    c = ArrayType3()

    lib.multiply_matrix.argtypes = [
    ct.c_int,
    ct.c_int,
    ct.c_int,
    ct.c_int,
    ct.POINTER(ct.c_int),
    ct.POINTER(ct.c_int),
    ct.POINTER(ct.c_int)
    ]

    lib.multiply_matrix.restype = None

    lib.multiply_matrix(row1, col1,row2,col2, matrix_a,matrix_b, c)

    tk.Label(matrix_frame, text="Result").grid(row=end_row_B, column=0, columnspan=col1)

    for i in range(row1):
        for j in range(col2):
            value=c[i * col2 + j]

            label = tk.Label(
                matrix_frame,
                text=str(value),
                width=9,
                font=('Arial', 16),
                relief="solid"
            )
 
            label.grid(
                row=end_row_B + i + 1,
                column=j,
                padx=2,
                pady=2
            )


Evaluate_btn=tk.Button(matrix_frame,text="EVALUATE",command=multiplication_matrix).grid(row=end_row_B,column=0,columnspan=col1)


root.mainloop()