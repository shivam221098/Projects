# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone:

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None

    def assign(self, employee_id):
        self.employee_id = employee_id

    def is_assigned(self):
        return self.employee_id is not None

    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)


class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)


class PhoneAssignments:

    def __init__(self):
        self.phones = []
        self.employees = []

    def add_employee(self, employee):
        # TODO raise exception if two employees with same ID are added
        for i in self.employees:
            if i.id == employee.id:
                raise EmployeeError(f"Employee ID: {employee.id} is already present. can't add again")
        self.employees.append(employee)

    def add_phone(self, phone):
        # TODO raise exception if two phones with same ID are added
        for i in self.phones:
            if i.id == phone.id:
                raise PhoneError(f"phone ID: {phone.id} is already present. can't add again")
        self.phones.append(phone)

    def assign(self, phone_id, employee):
        # Find phone in phones list
        # TODO if phone is already assigned to an employee, do not change list, raise exception
        # TODO if employee already has a phone, do not change list, and raise exception
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception
        for phone in self.phones:
            if phone.employee_id == employee.id and phone.id == phone_id:
                return
        for phone in self.phones:
            if employee.id == phone.employee_id:
                raise PhoneError
        for phone in self.phones:
            if phone.id == phone_id and phone.is_assigned():
                raise PhoneError(f"phone ID: {phone.id} is already assigned. can't assign again")
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(employee.id)
                return

    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None

    def phone_info(self, employee):
        # find phone for employee in phones list

        # TODO  should return None if the employee does not have a phone
        # TODO  the method should raise an exception if the employee does not exist
        if employee not in self.employees:
            raise PhoneError

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None


class PhoneError(Exception):
    pass


class EmployeeError(Exception):
    pass


if __name__ == '__main__':
    assignments = PhoneAssignments()

    phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
    phone2 = Phone(2, 'Samsung', 'Galaxy S III')
    phone3 = Phone(3, 'Samsung', 'Galaxy A7')

    assignments.add_phone(phone1)
    assignments.add_phone(phone2)
    assignments.add_phone(phone3)

    employee1 = Employee(1, 'Alice')
    employee2 = Employee(2, 'Bill')
    employee3 = Employee(3, 'Ted')

    assignments.add_employee(employee1)
    assignments.add_employee(employee2)
    assignments.add_employee(employee3)

    assignments.assign(phone1.id, employee2)  # Assign phone 1 to employee 2
    assignments.assign(phone2.id, employee3)  # Assign phone 2 to employee 3

    print(assignments.phone_info(employee1))  # Employee 1, no phone. Prints None
    print(assignments.phone_info(employee2))  # Employee 2, has Phone 1
    print(assignments.phone_info(employee3))  # Employee 3 has Phone 2

    assignments.un_assign(phone2.id)  # un-assign phone 2 (which belonged to employee 3)
    print(assignments.phone_info(employee3))  # None

    assignments.assign(phone3.id, employee3)  # Assign phone 3 to employee 3
    # TODO this should fail; employee3 should not be able to have two phones
