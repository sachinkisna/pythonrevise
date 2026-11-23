prices = [500, 1200, 800, 2500, 300, 1800, 900]

sum=0
temp=0
for j,i in enumerate(prices, start=1):
   sum+=i
   if i>1000:
      temp+=1
      
print(f" Total is {sum}")
print(f" Average is {sum/j:.2f}")
print(f" Highest is {max(prices)}")
print(f" Lowest is {min(prices)}")
print(f" Products more than 1000 {temp}")