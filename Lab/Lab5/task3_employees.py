class Node:
    def __init__(self, employee):
        self.employee = employee
        self.next = None

class EmployeeList:
    def __init__(self):
        self.head = None

    def search_employee(self, emp_no):
        current = self.head
        while current is not None:
            if current.employee["emp_no"] == emp_no:
                return current.employee
            else:
                current = current.next
        return None

    def add_employee(self, emp_no, name, salary, dept_no):
        duplicate = self.search_employee(emp_no)
        if duplicate is not None:
            return False
        else: 
            new_employee = {
                "emp_no": emp_no, 
                "name": name , 
                "salary": salary, 
                "dept_no": dept_no,
            }
            new_node = Node(new_employee)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next 
                current.next = new_node
            return True 

    def remove_employee(self, emp_no):
        current = self.head
        previous = None
        while current is not None:
            if current.employee["emp_no"] == emp_no:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True 
            else:
                previous = current 
                current = current.next

        return False

    def all_employees(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.employee)
            current = current.next
        return result


# Part A
n1 = Node({"emp_no": 101, "name": "Vanna", "salary": 50000, "dept_no": 1})
n2 = Node({"emp_no": 102, "name": "Tena", "salary": 60000, "dept_no": 2})
n1.next = n2
head = n1
print(head.employee['emp_no'])
print(head.next.employee['emp_no'])
print(head.next.next)


# test # ---- Add 101, 102, 103; display order ----
elist = EmployeeList()
elist.add_employee(101, "Vanna", 50000, 1)
elist.add_employee(102, "Tena", 60000, 2)
elist.add_employee(103, "Devi", 55000, 3)
print(elist.all_employees())
# [{'emp_no': 101,...}, {'emp_no': 102,...}, {'emp_no': 103,...}]

# ---- Search 102 ----
print(elist.search_employee(102))
# {'emp_no': 102, 'name': 'Tena', 'salary': 60000, 'dept_no': 2}

# ---- Add 102 again ----
print(elist.add_employee(102, "Tena", 60000, 2))  # False
print(elist.all_employees())  

# ---- Remove first (fresh list) ----
e1 = EmployeeList()
e1.add_employee(101, "A", 1, 1)
e1.add_employee(102, "B", 2, 2)
e1.add_employee(103, "C", 3, 3)
print(e1.remove_employee(101))   
print(e1.all_employees())        

# ---- Remove middle (fresh list) ----
e2 = EmployeeList()
e2.add_employee(101, "A", 1, 1)
e2.add_employee(102, "B", 2, 2)
e2.add_employee(103, "C", 3, 3)
print(e2.remove_employee(102))   
print(e2.all_employees())        

# ---- Remove last (fresh list) ----
e3 = EmployeeList()
e3.add_employee(101, "A", 1, 1)
e3.add_employee(102, "B", 2, 2)
e3.add_employee(103, "C", 3, 3)
print(e3.remove_employee(103))   
print(e3.all_employees())        

# ---- Remove the only node ----
e4 = EmployeeList()
e4.add_employee(101, "A", 1, 1)
print(e4.remove_employee(101))   
print(e4.head)                  

# ---- Search/remove 999 (not present) ----
print(elist.search_employee(999))    
print(elist.remove_employee(999))    

# ---- Empty list ----
e5 = EmployeeList()
print(e5.all_employees())        
print(e5.search_employee(1))     
print(e5.remove_employee(1))     

# Only previous.next changes when removing a middle node — it's redirected
# to skip the removed node and point straight at current.next.
# search_employee knows it reached the end when current becomes None.
