fname=input("The filename: ")
i=fname.split('.')
if i[1]=='py':
    print("The extension of the file is: Python")
elif i[1]=='c':
    print("The extension of the file is: C")
elif i[1]=='doc':
    print("The extension of the file is: Microsoft word")
elif i[1]=='class' or i[1]=='java':
    print("The extension of the file is: Java")
elif i[1]=='ppt':
    print("The extension of the file is: Powerpoint")
elif i[1]=='html':
    print("The extension of the file is: HyperText Markup Language")
elif i[1]=='txt':
    print("The extension of the file is: ASCII Text")
elif i[1]=='xls' or i[1]=='xlsx':
    print("The extension of the file is: Excel Spreadsheet")
elif i[1]=='css':
    print("The extension of the file is: Cascading Style Sheets")
else:
    print("The extension of the file might be someother.")
