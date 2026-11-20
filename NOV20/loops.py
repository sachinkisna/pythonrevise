

# for variable in iterable
#range(stop) 0 to start and exclude teh stop value

# for num in range(10):
#     print(num)

#range(start,stop)--> from start to stop exclude teh stop value

# for number in range(1,6):
#     print(number)   

#range(start , stop, steps)--> the steps determines te insrement or decreament

# for i in range(10,20):
#     print(i)
#     if i==15:
#         pass



# while loop
# count=1
# while count<=5:
#     print(count)
#     count+=1

# for i in range(1,3):
#     for j in range(1,3):
#         print(f"Inner Loop{j}")
#     print(f"Outer Loop{i}")

#looping through strings

name="Sachin"

lists=["list1","list2","lists3"]

for ind,ele in enumerate(lists,start=10):
    print(ind,ele)