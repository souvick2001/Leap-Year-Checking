year = int(input("Which year do want to check : "))
if year % 4==0 :
  print(f"{year} is a leap year .😍")
elif year % 100 ==0 :
  print(f"{year} is a leap year .😍")
elif year % 400 ==0 :
  print(f"{year} is a leap year .😍")
else :
  print(f"{year} is not a leap year .🥲")
