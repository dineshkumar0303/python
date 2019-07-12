class Employee:
    firstname=""
    lastname=""
    emailid="@comp.com"

    def displayEmail(self,firstname,lastname):
        email=firstname+lastname+self.emailid
        print("Email id is {}".format(email))

emp=Employee()
emp.displayEmail("dinesh","kumar")
