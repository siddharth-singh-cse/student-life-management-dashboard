# ==================== STUDENT DETAILS ====================

name = input("Enter your name")
college = input("Enter your college name")
age = int(input("Enter your age"))
course = input("Enter your course")

# ==================== ACADEMIC DETAILS ====================

maths = int(input("Enter your maths marks"))
physics = int(input("Enter your physics marks"))
english = int(input("Enter your english marks"))
total = physics + maths + english
average = total / 3
marks_check = total > 200
average_check = average >= 60 
age_check = age >= 18

# ==================== FEE DETAILS ====================

annual_fee = int(input("Enter your annual fee"))
scholarship = int(input("Enter your scholorship"))
remaining_fee = annual_fee - scholarship
fee_check = remaining_fee < 100000

# ==================== MONTHLY EXPENSES ====================


income = int(input("Enter your monthly income"))
rent = int(input("Enter your room rent"))
food = int(input("Enter your food expence"))
travel = int(input("Enter your travel expence"))
others = int(input("Enter your other expence"))
total_expense = rent+food+travel+others
remaining_money = income - total_expense

# ==================== ELIGIBILITY CHECKS ====================

has_id_input = input("Do you have a valid ID? (yes/no): ")
has_id = has_id_input == "yes"

banned_input = input("Are you banned? (yes/no): ")
is_banned = banned_input == "yes"

is_adult = age >= 18
not_banned = not is_banned
overall_eligibility = is_adult and has_id and not_banned

# ==================== PROGRESS SCORE ====================

if average >= 90:
    progress = 100

elif average >= 75:
    progress = 85

elif average >= 60:
    progress = 70

else:
    progress = 50

# ==================== FINAL DASHBOARD ====================

print(f"""
      ========== STUDENT LIFE DASHBOARD ==========
      
      STUDENT DETAILS
      Name: {name}
      College: {college}
      Age: {age}
      Course: {course}
      
      ACADEMIC DETAILS
      Maths :{maths}
      Physics: {physics}
      English: {english}
      Total: {total}
      Average: {average:.2f}
      Marks Check: {marks_check}
      Average Check: {average_check}
      Age Check: {age_check}
      
      FEE DETAILS
      Annual_fee: {annual_fee}
      Scholorship: {scholarship}
      Remaining: {remaining_fee}
      Fee Check:: {fee_check}
      
      MONTHLY EXPENSES
      Income: {income}
      Rent: {rent}
      Food: {food}
      Travel: {travel}
      Others: {others}
      Total_expence: {total_expense}
      Remaining_money: {remaining_money}
      
      ELIGIBILITY
      Valid ID: {has_id}
      Banned: {is_banned}
      Overall Eligibility: {overall_eligibility}

      PROGRESS
      Progress Score: {progress}
      PROGRESS
      progress: {progress}
      """)