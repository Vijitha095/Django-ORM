import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
print("Connection created")

# cur.execute("CREATE DATABASE DjangoORM")
# print("Database created")

# cur.execute('''CREATE TABLE employee(
#                id int primary key auto_increment,
#                name varchar(20),
#                designation varchar(30),
#                salary decimal(10,2)
#         )''')

# print("Table created")

# cur.execute('UPDATE employee SET designation=HR_Manager WHERE id=1')
# cur.execute('show columns from employee')
# print(cur.fetchall())
# # conn.commit()
# print("data updated")

class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for col in kwargs.keys():
            if cols!="":
                cols+=','
                placeholder+=','
            cols+=col
            placeholder+="%s"
        values=tuple(kwargs.values())
        query=f"insert into employee({cols}) values({placeholder})"
        cur.execute(query,values)
        conn.commit()

    def list(self,*args,**kwargs):
        cur.execute("SELECT * FROM employee")
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())

    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee WHERE {key}={kwargs.get(key)}")
            print(cur.fetchall())

    def update(self,*args,**kwargs):
        print(args,kwargs)
        for key in kwargs:
            cur.execute(f"UPDATE employee SET {key}='{kwargs.get(key)}' WHERE id={args[0]}")
            conn.commit()

    def delete(self,*args,**kwargs):
        cur.execute(f"DELETE FROM employee WHERE id={args[0]}")
        conn.commit()

    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee WHERE {key}='{kwargs.get(key)}'")
            print(cur.fetchall())

employee=Employee()

while True:
    print("1.Create employee")
    print("2.List all employees")
    print("3.Employee detail view")
    print("4.Update employee")
    print("5.Delete employee")
    print("6.Filter employees")
    print("7.Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        name=input("Enter the employee name:")
        desig=input("Enter the designation:")
        salary=float(input("Enter the salary:"))
        employee.create(name=name,designation=desig,salary=salary)

    elif choice == 2:
        employee.list()

    elif choice == 3:
        print("")
        id=int(input("Enter the employee ID:"))
        employee.retrieve(id=id)

    elif choice == 4:
        id=int(input("Enter the id of employee:"))
        print("Update:")
        print("1.Name")
        print("2.Designation")
        print("3.Salary")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("Enter the new name:")
            employee.update(id,name=name)
        elif choice ==2 :
            desig=input("Enter the new designation:")
            employee.update(id,designation=desig)
        elif choice == 3:
            salary = float(input("Enter the new salary:"))
            employee.update(id,salary=salary)
        else:
            print("Invalid choice")

    elif choice == 5:
        id=int(input("Enter the employee ID:"))
        employee.delete(id)

    elif choice == 6:
        print("Filter options:")
        print("1.Filter by name:")
        print("2.Filter by designation:")
        print("3.Filter by salary:")
        choice=int(input("Enter your choice:"))
        if choice == 1:
            name=input("Enter a name:")
            employee.filter(name=name)
        elif choice == 2:
            desig=input("Enter a designation:")
            employee.filter(designation=desig)
        elif choice == 3:
            salary=float(input("Enter a salary:"))
            employee.filter(salary=salary)

    elif choice == 7:
        print("Thank you")
        break

    else:
        print("Invalid choice")

conn.close()
print("Connection closed")
