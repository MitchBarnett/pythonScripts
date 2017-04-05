choice = input("""
1 = bytes
2= kb
3 = mb
4 = gb
""")
ammount = float(input("How many? "))

if choice == '1':
    factor = 1
    loops = 1
elif choice == '2':
    factor = 1024
    loops = 1
elif choice == '3':
    factor = 1024*1024
    loops = 1
elif choice == '4':
    factor = 1024*1024
    loops = 1024

total = factor*ammount
total = int(total)
string = 'a'*total
print('calculated')
    

with open("large.txt", "a") as file:
        for i in range(loops):
            file.write(string)
            
print('done')
