'''import csv
def write_into_csv(information_list):
    csv_file=open("student_info.csv","a",newline='')
    writer=csv.writer(csv_file)
    if csv_file.tell()==0:
        writer.writerow(["NAME","AGE","CONTACT_NUMBER","E-MAIL_ID"])
    writer.writerow(information_list)
if __name__ =='__main__':
    condition=True
    student=1
    while(condition):
        student_information=input("Enter student #{} information  in the format ( Name , AGE , Contact_Number , E-mail ID): ".format(student))
        student_information_list=student_information.split(' ')
        print("The information is - \nNAME: {},\nAGE:{}, \nCONTACT_NUMBER:{},\nE-MAIL_ID:{}"
              .format(student_information_list[0],student_information_list[1],student_information_list[2],student_information_list[3]))
        check_again=input("Is the entered information correct ? (yes/no) :")
        if check_again=='yes':
              write_into_csv(student_information_list)
              checking_condition=input("Enter if you want to enter information for another student (yes/no): ")
              if checking_condition=='yes':
                  condition=True
                  student=student+1
              elif checking_condition=='no':
                  condition=False
        elif check_again=='no':
             print("\n PLEASE RE-ENTER AGAIN !")

        else:
            print("Re-enter again")'''
import csv
def appending(detail):
    file=open("student_detail1.csv","a",newline='')
    writer=csv.writer(file)
    if file.tell()==0:
        writer.writerow(["Name","Age","Reg no","Department","Shift"])
    writer.writerow(detail)
if __name__=="__main__":
    condition=True
    count=1
    while(condition):
        details=input("Enter Student details in the given format [Name,Age,Register number,Department,Shift]:")
        detail_list=details.split(" ")
        check=True
        a=input("Is the above mentioned input is correct(yes/no)")
        if a=="yes":
            appending(detail_list)
            print("\n\n\nSTUDENT",count," DETAIL:\n\nName:",detail_list[0],"\nAge:",detail_list[1],'\nRegister Number:',detail_list[2],'\nDepartment:',detail_list[3],'\nShift:',detail_list[4],'\n\n\n')
            continue1=input("Do you want to add another detatils (yes/no)")
            if continue1=="yes":
                condition=True
                count+=1
            else:
                condition=False
        else:
            print("Re-enter again")
