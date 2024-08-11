from manager import Manager
from employee import Employee

def main() :
    m1 = Manager()
    m1.setName("John Smith")
    m1.setBaseSalary(75000)
    m1.setBonus(5000)
    
    print(m1.getName())
    print("Expected: *John Smith")
    print("%.2f" % m1.getSalary())
    print("Expected: 80000.00")

main()