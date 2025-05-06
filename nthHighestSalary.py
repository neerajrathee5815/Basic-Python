sal = []


def salary():

    n = int(input("how many salaries you want to enter"))
    for i in range(n):
        sal.append(float(input(f"Enter Salary {i+1} : ")))
    
    print("Salaries added succesfully")

def max_sal():

    max_salary = max(sal)
    print(max_salary)

def nth_sal(sal,x):

    if x > len(sal):
        print("Salary does not exist")
    nth_salary = sorted(sal, reverse=True)
    print(f"The {x} highest salary is {nth_salary[x-1]}")

def run():

    while True:

        print("1. You want to add salaries ?")
        print("2. you want to view highest salary")
        print("3. You want to view nth highesgt salary")
        print("4. Exit")

        choice = input("Select an option from 1 - 4 : ")
        print()

        if choice == "1":
            salary()
        elif choice == "2":
            max_sal()
        elif choice == "3":
            y = int(input("which highest salary you want to see ? "))
            nth_sal(sal,y)
        elif choice == "4":
            print("Thanks for your time")
            break
        else:
            print("invalid choice")

if __name__ == "__main__" :

    run()



  
