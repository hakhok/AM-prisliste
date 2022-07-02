import csv
import curses
from curses import wrapper


file = open("priser.csv")
csvreader = csv.reader(file)
header = next(csvreader)


rows = []
for row in csvreader:
    rows.append(row)
file.close()

print("\n")

for row in rows:
    item = (row[0]).split(';')[0]
    price = (row[0]).split(';')[1]
    print(f"{item} koster {price}")

total_price = 0
added_items = []
under15 = 10000
over15 = 12400
reise = 300
timelonn = 150
profitt_prosent = 25

for row in rows:
    item = (row[0]).split(';')[0]
    price = (row[0]).split(';')[1]
    if item == 'over 15 personer':
        over15 = int(price)
        break
    if item == 'under 15 personer':
        under15 = int(price)
        break
    if item == 'reiseutgifter':
        reise = int(price)
        break
    if item == 'timelonn':
        timelonn = int(price)
        print("Timelønn = " + timelonn)
        break
    print(f"\n{item} koster {price}, ønsker du å legge til?")
    user_input = input("Ditt svar(y/n): ")
    if user_input == "y":
        total_price += int(price)
        added_items.append(item)
        print(f"{item} ble lagt til")
    elif user_input == "n":
        print(f"{item} ble ikke lagt til")

folk = input("\nAntall personer: ")
if int(folk) <= 15:
    total_price += under15
elif int(folk) > 15:
    total_price += over15
added_items.append(f"Personer: {folk}")

reiseutgifter = input("Antall reiseutgifter: ")
reiseutgiftpris = int(reiseutgifter)*int(reise)
added_items.append(f"Reiseutgifter: {reiseutgifter}")
total_price += reiseutgiftpris
print(f"Reiseutgifter: {reiseutgiftpris} på {reiseutgifter} personer.")

personell_timer = input("Beregner arbeidstimer: ")
personell_kostadd = int(personell_timer)*timelonn
added_items.append(f"Personell timer: {personell_timer} = {personell_kostadd}kr")
print(f"Personell timer: {personell_timer}")

total_price_profitt = total_price + total_price*profitt_prosent/100
fortjeneste = total_price_profitt - total_price

print(f"\nAM-priser:")
print(f"Total pris: {total_price}")
print(f"Total pris + {profitt_prosent}% fortjenetse: {total_price_profitt}")
print(f"Fortjeneste: {fortjeneste}")
print("Dette ble lagt til:")
for item in added_items:
    print(item)
