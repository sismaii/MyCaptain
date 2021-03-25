import csv
def write(ll):
    with open("student_info.csv","a", newline="") as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Phone number","Email Id"])
        writer.writerow(ll)
if _name=='main_' :       
    condition=True
    c=1
    while(condition):
        student_info=input("Enter the Name Age Phone number and the Email Id for student number {}: ".format(c))

        l=student_info.split(" ")
        print("The entered details are:\nName: {}\nAge: {}\nPhone number: {}\nEmail Id: {}".format(l[0],l[1],l[2],l[3]))
        check=input("Is the information provided correct?(yes/no): ")
        if check=='yes':
            write(l)
            choice=input("Would you like to continue?(yes/no): ")
            if choice=='yes':

                condition=True
                c+=1
            else:
                condition=False
        elif check=="no":
            print("Re-enter the values: ")
