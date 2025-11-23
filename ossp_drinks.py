import threading

users=["Egor", "Anastasia", "Andrew", "Artyom", "Ivan", "Sasha", "Volodymyr"]
drinks=["Water", "Milk", "Coffee", "Tea", "Juice", "Lemonade", "Cola"]

user_drinks=[]

def take_drink(user):
    global drinks, user_drinks

    if drinks:
        drink=drinks.pop(0)
    else:
        drink=None

    user_drinks.append((user, drink))

threads=[]

for user in users:
    t=threading.Thread(target=take_drink,args=(user,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Результат:")
for pair in user_drinks:
    print(pair)