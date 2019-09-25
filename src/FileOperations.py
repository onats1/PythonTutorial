# r is for read only, w is for writing, r+ is for read and write
# and a is for append( adding to the end of the file)

#opening and closing a file.
employee_file = open("Employee1.txt", "r+")

print(employee_file.readable())

print(employee_file.read())

employee_file.write("\nMight Guy - Eight inner gates.")
employee_file.close()



