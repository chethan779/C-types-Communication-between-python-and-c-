import ctypes as ct
import tkinter as tk


root=tk.Tk()
root.geometry("2560x1600")

matrix_frame=tk.Frame(root)
matrix_frame.place(relx=0.5,rely=0.1,anchor="n")

operation = None

def set_operation(op):
    global operation
    operation=op
    set_matrix()


def set_matrix():
# *******************************************************************************************************************************************

        def set_matrix_for_addition_matrix():
            set_matrix_add=tk.Toplevel(root)
            set_matrix_add.geometry("300x200")

            tk.Label(set_matrix_add,text="Enter Number of rows for Matrix A").grid(row=0,column=0)
            row_entry1=tk.Entry(set_matrix_add)
            row_entry1.grid(row=0,column=6,columnspan=10)

            tk.Label(set_matrix_add,text="Enter Number of columns for Matrix A").grid(row=2,column=0)
            col_entry1=tk.Entry(set_matrix_add)
            col_entry1.grid(row=2,column=6,columnspan=10)

            def open_addition_matrix_win():
                set_matrix_add_win=tk.Toplevel(root)
                set_matrix_add_win.geometry("2560x1600")

                set_matrix_add_win_mid_frame=tk.Frame(set_matrix_add_win)
                set_matrix_add_win_mid_frame.place(relx=0.5,rely=0.1,anchor="n")
                row1=int(row_entry1.get())
                col1=int(col_entry1.get())

                set_matrix_add.destroy()

                tk.Label(set_matrix_add_win_mid_frame,text="Enter Values In Matrix A").grid(row=0,column=0,columnspan=5)
                matrix_A=[]

                for i in range(row1):
                    row_entries1=[]
                    for j in range(col1):
                        entry1=tk.Entry(set_matrix_add_win_mid_frame,width=5,font=('Arial',16),justify='center')
                        entry1.grid(row=i+1,column=j,padx=2,pady=2)

                        row_entries1.append(entry1)
                    matrix_A.append(row_entries1)

                start_row_B=row1+3

                tk.Label(set_matrix_add_win_mid_frame,text="Enter Values In Matrix B").grid(row=start_row_B,column=0,columnspan=5)
                matrix_B=[]

                for i in range(row1):
                    row_entries2=[]
                    for j in range(col1):
                        entry2=tk.Entry(set_matrix_add_win_mid_frame,width=5,font=('Arial',16),justify='center')
                        entry2.grid(row=start_row_B+i+1,column=j,padx=2,pady=2)

                        row_entries2.append(entry2)
                    matrix_B.append(row_entries2)

                start_row_C=start_row_B+row1+3

                def add_matrices():
                    lib=ct.CDLL("./matrix_op.dll")

                    A=[]

                    for i in range(row1):
                        for j in range(col1):
                            A.append(int(matrix_A[i][j].get()))

                    B=[]

                    for i in range(row1):
                        for j in range(col1):
                            B.append(int(matrix_B[i][j].get()))

                    ArrayType1=ct.c_int * (row1 * col1) 
                    ArrayType2=ct.c_int * (row1 * col1)       

                    a=ArrayType1(*A)
                    b=ArrayType1(*B)
                    c=ArrayType2()

                    lib.add_matrix.argtypes=[ct.c_int,ct.c_int,ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int)]
                    lib.add_matrix.restype=None
            
                    lib.add_matrix(row1,col1,a,b,c)

                    result_frame=tk.Frame(set_matrix_add_win_mid_frame)
                    result_frame.grid(row=start_row_C + 2 ,column=0 , columnspan=20 , pady=30)

                    for i in range(row1):
                        for j in range(col1):
                            value=c[i * col1 + j]

                            label=tk.Label(result_frame,text=str(value),width=5,font=('Arial', 16),relief="solid")
                            label.grid(row=i,column=j,padx=2,pady=2)

                evaluate_btn=tk.Button(set_matrix_add_win_mid_frame,text="EVALUATE",command=add_matrices)
                evaluate_btn.grid(row=start_row_C,column=0,columnspan=6)

            submit_btn=tk.Button(set_matrix_add,text="SUBMIT",command=open_addition_matrix_win)
            submit_btn.grid(row=6,column=6,columnspan=6)
# ******************************************************************************************************************************************

        def set_matrix_for_subtraction_matrix():
            set_matrix_subtract=tk.Toplevel(root)
            set_matrix_subtract.geometry("300x200")

            tk.Label(set_matrix_subtract,text="Enter Number of rows for Matrix A").grid(row=0,column=0)
            row_entry1=tk.Entry(set_matrix_subtract)
            row_entry1.grid(row=0,column=6,columnspan=10)

            tk.Label(set_matrix_subtract,text="Enter Number of columns for Matrix A").grid(row=2,column=0)
            col_entry1=tk.Entry(set_matrix_subtract)
            col_entry1.grid(row=2,column=6,columnspan=10)

            def open_subtraction_matrix_win():
                set_matrix_subtract_win=tk.Toplevel(root)
                set_matrix_subtract_win.geometry("2560x1600")

                set_matrix_subtract_win_mid_frame=tk.Frame(set_matrix_subtract_win)
                set_matrix_subtract_win_mid_frame.place(relx=0.5,rely=0.1,anchor="n")
                row1=int(row_entry1.get())
                col1=int(col_entry1.get())

                set_matrix_subtract.destroy()

                tk.Label(set_matrix_subtract_win_mid_frame,text="Enter Values In Matrix A").grid(row=0,column=0,columnspan=5)
                matrix_A=[]

                for i in range(row1):
                    row_entries1=[]
                    for j in range(col1):
                        entry1=tk.Entry(set_matrix_subtract_win_mid_frame,width=5,font=('Arial',16),justify='center')
                        entry1.grid(row=i+1,column=j,padx=2,pady=2)

                        row_entries1.append(entry1)
                    matrix_A.append(row_entries1)

                start_row_B=row1+3

                tk.Label(set_matrix_subtract_win_mid_frame,text="Enter Values In Matrix B").grid(row=start_row_B,column=0,columnspan=5)
                matrix_B=[]

                for i in range(row1):
                    row_entries2=[]
                    for j in range(col1):
                        entry2=tk.Entry(set_matrix_subtract_win_mid_frame,width=5,font=('Arial',16),justify='center')
                        entry2.grid(row=start_row_B+i+1,column=j,padx=2,pady=2)

                        row_entries2.append(entry2)
                    matrix_B.append(row_entries2)

                start_row_C=start_row_B+row1+3

                def subtract_matrices():
                    lib=ct.CDLL("./matrix_op.dll")

                    A=[]

                    for i in range(row1):
                        for j in range(col1):
                            A.append(int(matrix_A[i][j].get()))

                    B=[]

                    for i in range(row1):
                        for j in range(col1):
                            B.append(int(matrix_B[i][j].get()))

                    ArrayType1=ct.c_int * (row1 * col1) 
                    ArrayType2=ct.c_int * (row1 * col1)       

                    a=ArrayType1(*A)
                    b=ArrayType1(*B)
                    c=ArrayType2()

                    lib.subtract_matrix.argtypes=[ct.c_int,ct.c_int,ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int)]
                    lib.subtract_matrix.restype=None
            
                    lib.subtract_matrix(row1,col1,a,b,c)

                    result_frame=tk.Frame(set_matrix_subtract_win_mid_frame)
                    result_frame.grid(row=start_row_C + 2 ,column=0 , columnspan=20 , pady=30)

                    for i in range(row1):
                        for j in range(col1):
                            value=c[i * col1 + j]

                            label=tk.Label(result_frame,text=str(value),width=5,font=('Arial', 16),relief="solid")
                            label.grid(row=i,column=j,padx=2,pady=2)

                evaluate_btn=tk.Button(set_matrix_subtract_win_mid_frame,text="EVALUATE",command=subtract_matrices)
                evaluate_btn.grid(row=start_row_C,column=0,columnspan=6)

            submit_btn=tk.Button(set_matrix_subtract,text="SUBMIT",command=open_subtraction_matrix_win)
            submit_btn.grid(row=6,column=6,columnspan=6)   


# ****************************************************************************************************************************************   
 
        def set_matrix_for_multiplication_matrix():
            set_matrix_multiply=tk.Toplevel(root)
            set_matrix_multiply.geometry("300x200")

            tk.Label(set_matrix_multiply,text="Enter Number of rows for Matrix A").grid(row=0,column=0)
            row_entry1=tk.Entry(set_matrix_multiply)
            row_entry1.grid(row=0,column=6,columnspan=10)

            tk.Label(set_matrix_multiply,text="Enter Number of columns for Matrix A").grid(row=2,column=0)
            col_entry1=tk.Entry(set_matrix_multiply)
            col_entry1.grid(row=2,column=6,columnspan=10)

            tk.Label(set_matrix_multiply,text="Enter Number of rows for Matrix B").grid(row=4,column=0)
            row_entry2=tk.Entry(set_matrix_multiply)
            row_entry2.grid(row=4,column=6,columnspan=10)

            tk.Label(set_matrix_multiply,text="Enter Number of rows for Matrix B").grid(row=6,column=0)
            col_entry2=tk.Entry(set_matrix_multiply)
            col_entry2.grid(row=6,column=6,columnspan=10) 

            def open_multiplication_matrix_win():
                set_matrix_multiply_win=tk.Toplevel(root)
                set_matrix_multiply_win.geometry("2560x1600")

                set_matrix_multiply_win_mid_frame=tk.Frame(set_matrix_multiply_win)
                set_matrix_multiply_win_mid_frame.place(relx=0.5,rely=0.1,anchor="n")

                row1=int(row_entry1.get())
                col1=int(col_entry1.get())
                row2=int(row_entry2.get())
                col2=int(col_entry2.get())

                set_matrix_multiply.destroy()

                tk.Label(set_matrix_multiply_win_mid_frame,text="Enter Values In Matrix A").grid(row=0,column=0,columnspan=5)
                matrix_A=[]

                for i in range(row1):
                    row_entries1=[]
                    for j in range(col1):
                        entry1=tk.Entry(set_matrix_multiply_win_mid_frame,width=5,font=('Arial',16),justify='center')
                        entry1.grid(row=i+1,column=j,padx=2,pady=2)

                        row_entries1.append(entry1)
                    matrix_A.append(row_entries1)

                start_row_B=row1+3

                tk.Label(set_matrix_multiply_win_mid_frame,text="Enter Values In Matrix B").grid(row=start_row_B,column=0,columnspan=5)
                matrix_B=[]

                for i in range(row2):
                    row_entries2=[]
                    for j in range(col2):
                        entry2=tk.Entry(set_matrix_multiply_win_mid_frame,width=5,font=('Arial',16),justify='center')
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

                    ArrayType1=ct.c_int * (row1 * col1) 
                    ArrayType2=ct.c_int * (row2 * col2)  
                    ArrayType3=ct.c_int * (row1 * col2)     

                    a=ArrayType1(*A)
                    b=ArrayType2(*B)
                    c=ArrayType3()

                    lib.multiply_matrix.argtypes=[ct.c_int,ct.c_int,ct.c_int,ct.c_int,ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int)]
                    lib.multiply_matrix.restype=None
            
                    lib.multiply_matrix(row1,col1,row2,col2,a,b,c)

                    result_frame=tk.Frame(set_matrix_multiply_win_mid_frame)
                    result_frame.grid(row=start_row_C + 2 ,column=0 , columnspan=20 , pady=30)

                    for i in range(row1):
                        for j in range(col2):
                            value=c[i * col2 + j]

                            label=tk.Label(result_frame,text=str(value),width=5,font=('Arial', 16),relief="solid")
                            label.grid(row=i,column=j,padx=2,pady=2)

                evaluate_btn=tk.Button(set_matrix_multiply_win_mid_frame,text="EVALUATE",command=multiply_matrices)
                evaluate_btn.grid(row=start_row_C,column=0,columnspan=6)

            submit_btn=tk.Button(set_matrix_multiply,text="SUBMIT",command=open_multiplication_matrix_win)
            submit_btn.grid(row=10,column=6,columnspan=6)
# *******************************************************************************************************************************************

        if (operation == "add"):
            set_matrix_for_addition_matrix()
        elif (operation == "subtract"):
            set_matrix_for_subtraction_matrix()
        elif (operation == "Multiply"):
            set_matrix_for_multiplication_matrix()
            
# ********************************************************************************************************************************************

addition_matrix_button=tk.Button(matrix_frame,text="Addition_Matrix",width=20,height=5,command=lambda: set_operation("add"))
addition_matrix_button.grid(row=0,column=0,columnspan=5)


subtract_matrix_button=tk.Button(matrix_frame,text="Substraction_Matrix",width=20,height=5,command=lambda: set_operation("subtract"))
subtract_matrix_button.grid(row=0,column=10,columnspan=6,padx=20)

multiply_matrix_button=tk.Button(matrix_frame,text="Multiplication_Matrix",width=20,height=5,command=lambda: set_operation("Multiply"))
multiply_matrix_button.grid(row=10,column=3,columnspan=6,pady=20)

root.mainloop()