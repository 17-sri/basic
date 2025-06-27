# break : is used to come out of the loop when encountered. It instructs the program to 'exit the loop now'
for i in range(0, 80): # though its range is 0 to 80 but it will only print 0,1,2,3
    print(i)
    if i==3:
        break

# continue : is used to stop the current iteration of the loop and continue with the next one. It instructs the program to 'skip this iteration'
for i in range(4):
    print("printing >>>>>")
    if i==2:    # if i it is 2 , the iteration skipped
        continue
    print(i)

# pass : is a null statement, it instructs to do 'nothing'
l = [1, 2, 3]
for i in l:
    pass   # without 'pass' the program will throw an error, because for loop definition is empty 