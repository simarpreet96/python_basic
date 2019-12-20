def compound_interest(principle, rate, time): 
  
    # Calculates compound interest  
    CI = principle * (pow((1 + rate / 100), time)) 
    print("Compound interest is", CI) 
  
# Driver Code  
compound_interest(10000, 10.25, 5)

pr = input("enter principle amount:") 
ra = input("enter rate:")
ti = input("enter time period:")
ci = float(pr) * (pow((1 + float(ra) / 100), float(ti)))
print("The compund intrest is {0}:" .format(ci)) 