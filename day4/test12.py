example1 = "3 < 7 < 11"
example2 = "13 > 44 > 33 > 1"
example3 = "1 < 2 < 6 < 9 > 3"
test1 = int(example1[0]) < int(example1[4]) < int(example1[8])
test2 = int(example2[:2]) > int(example2[5:7]) and int(example2[5:7]) > int(example2[10:12]) and int(example2[10:12]) > int(example2[15:])
test3 = int(example3[0]) < int(example3[4]) < int(example3[8]) and int(example3[8]) < int(example3[12]) and int(example3[12]) > int(example3[16])
print(test1)  
print(test2) 
print(test3) 
