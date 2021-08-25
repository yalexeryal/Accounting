from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

data = datetime.now()

if __name__ == '__main__':
   print(data)
   print(calculate_salary())
   print(get_employees())
