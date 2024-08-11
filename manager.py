from employee import Employee

## 
#  Defines a manager, who is an employee, but with more responsibility.
#
class Manager(Employee) :
    ##
    #  Constructs a manager object with a default bonus of $0.
    #
    def __init__(self) :
        super().__init__()
        self._bonus = 0.0
    
    ##
    #  Sets the manager's bonus.
    #  @param amount the amount of the bonus as a numerical value
    #
    def setBonus(self, amount) :
        self._bonus = amount
    
    ##
    #  Gets the value of the manager's bonus.
    #  @return the bonus as a numerical value
    #
    def getBonus(self) :
        return self._bonus

    # Your code goes here
