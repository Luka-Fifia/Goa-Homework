mark = int(input("enter your grade: "))
        
is_A = mark >= 9
is_B = mark >= 8 and mark < 9
is_C = mark >= 7 and mark < 8
is_D = mark >= 6 and mark < 7
is_F = mark < 6

print("your grade is A: " , is_A , "your grade is B: " , is_B , "your grade is C: " , is_C , "your grade is D: " , is_D , "your grade is C: " , is_C , "your grade is D: " , is_D , "your grade is F: " , is_F)
