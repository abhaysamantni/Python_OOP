##
#  Defines an employee of a business.
# 
class Employee :
    ##
    #  Constructs an employee object that contains their name and salary.
    #
    def __init__(self) :
        self._name = ""
        self._baseSalary = 0.0
    
    ##
    #  Sets the name of the employee.
    #  @param newName string containing the employee's name
    #
    def setName(self, newName) :
        self._name = newName
    
    ##
    #  Sets the employee's base salary.
    #  @param newSalary the employee's base salary as a floating-point
    #
    def setBaseSalary(self, newSalary) :
        self._baseSalary = newSalary
    
    ##
    #  Gets the employee's name.
    #  @return a string containing the name
    #
    def getName(self) :
        return self._name
    
    ##
    #  Gets the employee's salary.
    #  @return the salary as a numerical value
    #
    def getSalary(self) :
        return self._baseSalary