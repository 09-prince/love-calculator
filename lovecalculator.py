print("WELCOME TO OUR PROJECT :>")
choice=['male','female']
gender = None
while gender not in choice:
    gender=input('ENTER YOUR GENDER: \n')

    if gender=="male":
        usr1_name=input("ENTER YOUR NAME: ")
        usr1_age=int(input("ENTER YOUR BIRTHDAY DATE: "))
        usr2_name=input("ENTER HER NAME:  ")
        usr2_age=int(input("ENTER HER BIRTHDAY DATE: "))


    

        usr1_total=len(usr1_name)+(usr1_age)
        usr2_total=len(usr2_name)+(usr2_age)

        if usr1_total<usr2_total:
            total_love=(usr1_total/usr2_total)*100
        elif usr2_total<usr1_total:
            total_love=(usr2_total/usr1_total)*100
            lo=round(total_love)
        import time
        for second in range(5):
            # print(second)
            time.sleep(1)
            print("WAITING FOR RESULT :>")
        print(f"THE LOVE PERSENT IS {lo}")
        print("THANK YOU FOR USING ")

    elif gender =="female":
        usr3_name=input("ENTER YOUR NAME: ")
        usr3_age=int(input("ENTER YOUR BIRTHDAY DATE: "))
        usr4_name=input("ENTER HIS NAME:  ")
        usr4_age=int(input("ENTER HIS BIRTHDAY DATE: "))

        user3_total=len(usr3_name)+(usr3_age)
        user4_total=len(usr4_name)+(usr4_age)

        if user3_total<user4_total:
            total2_love=(user3_total/user4_total)*100
        elif user4_total<user3_total:
            total2_love=(user4_total/user3_total)*100
            lo2=round(total2_love)
        import time
        for i in range(5):
            time.sleep(1)
            print("WAITING FOR RESULT :>")
        print(f"THE LOVE PERSENT IS {lo2} ")
print("THANK YOU FOR USING ")