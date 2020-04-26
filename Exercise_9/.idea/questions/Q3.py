numbers = [2,10,20,12,15,8,9,9,95,44,2]
powers = (2,3,1,0,3,1,0,2)

print((list(map(lambda num,pow:num**pow,numbers,powers))))