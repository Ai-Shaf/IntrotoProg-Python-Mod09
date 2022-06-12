# ---------------------------------------------------------- #
# Title: Listing 08 + Listing 10
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AShafique, 6.9.2020, Modified Script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as DC  # data classes
    import ProcessingClasses as P  # processing classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = DC.Person("Bob", "Smith")
objP2 = DC.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    print(row)
    p = DC.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

print("------------------------------------------------")  # extra line for separation

if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only!
    import ProcessingClasses as P  # processing classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

print("------------------------------------------------------")    # add line for separation

# Test IO classes
# TODO: create and test IO module. Done.
if __name__ == "__main__":
    import IOClasses as IO
    import DataClasses as DC
else:
    raise Exception("This fine was not created to be imported")

emp_data = IO.EmployeeIO.input_employee_data()
print(emp_data)
lstTable.append(emp_data)

IO.EmployeeIO.print_current_list_items(lstTable)

