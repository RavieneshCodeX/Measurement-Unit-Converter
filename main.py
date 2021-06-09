print("1. km to m")
print("2. m to km")
print("3. m to cm")
print("4. cm to m")
print("5. m to mm")
print("6. mm to m")
print("7. km to cm")
print("8. cm to km")
print("9. cm to mm")
print("10. mm to cm")
print("11. km to mm")
print('12. mm to km')

unit = input("Please select 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 or 12: ")

if unit == "1":
    print("1. km to m")
    km = int(input("KM: "))
    m = km * int(1000)
    print(m, end='')
    print("m")

if unit == "2":
    print("2. m to km")
    m = int(input("M: "))
    km = m / int(1000)
    print(km, end='')
    print("km")

if unit == "3":
    print("3. m to cm")
    m = int(input("M: "))
    cm = m * int(100)
    print(cm, end='')
    print("cm") 

if unit == "4":
    print("4. cm to m")
    cm = int(input("CM: "))
    m = cm / int(100)
    print(m, end='')
    print("m")

if unit == "5":
    print("1. m to mm")
    m = int(input("M: "))
    mm = m * int(1000)
    print(mm, end='')
    print("mm")

if unit == "6":
    print("6. mm to m")
    mm = int(input("MM: "))
    m = mm / int(1000)
    print(m, end='')
    print("m")

if unit == "7":
    print("7. km to cm")
    km = int(input("KM: "))
    cm = km * int(100000)
    print(cm, end='')
    print("cm")

if unit == "8":
    print("8. cm to km")
    cm = int(input("CM: "))
    km = cm / int(100000)
    print(km, end='')
    print("km")

if unit == "9":
    print("9. cm to mm")
    cm = int(input("CM: "))
    mm = cm * int(10)
    print(mm, end='')
    print("mm")

if unit == '10':
    print("10. mm to cm")
    mm = int(input("MM: "))
    cm = mm / int(10)
    print(cm, end='')
    print("cm")

if unit == '11':
    print("11. km to mm")
    km = int(input("KM: "))
    mm = km * int(1000000)
    print(mm, end='')
    print("mm")

if unit == '12':
    print("12. mm to km")
    mm = int(input("MM: "))
    km = mm / int(1000000)
    print(km, end='')
    print("km")

else: 
    print("UNABLE TO OPERATE DUE TO WRONG INPUT. PLEASE CHECK YOUR INPUT!!!")
