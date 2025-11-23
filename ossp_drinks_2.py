# 2) Более детально описать процесс
# от входа в кафе до выхода
# при этом кто-то может пить внутри помещения
# кто-то брать с собой


# початок сценарія - вхід в кафе
# вхід в кафе (немає черги)
# замовлення (за чергою, одночасно тільке 1)
# напої -(частина бескінечна, частина обмежена)
# видача замовлень (на кожний напой свій час)
# споживання внутрі чи на винос
# кінець сценарію - вихід з кафе

import threading
import time
import random

users = ["Egor", "Anastasia", "Andrew", "Artyom", "Ivan", "Sasha", "Volodymyr"]

drinks = {
    "Water":    {"stock": None, "prep_time": (0.2, 0.4)},
    "Milk":     {"stock": 3,    "prep_time": (0.5, 0.8)},
    "Coffee":   {"stock": 2,    "prep_time": (0.8, 1.3)},
    "Tea":      {"stock": None, "prep_time": (0.4, 0.9)},
    "Juice":    {"stock": 3,    "prep_time": (0.6, 1.0)},
    "Lemonade": {"stock": None, "prep_time": (0.5, 1.0)},
    "Cola":     {"stock": 2,    "prep_time": (0.7, 1.1)},
}

line_lock = threading.Lock()

results_lock = threading.Lock()
results = []


def get_available_drinks():
    available = []
    for name, info in drinks.items():
        stock = info["stock"]
        if stock is None or stock > 0:
            available.append(name)
    return available


def user_scenario(user: str):
    time.sleep(random.uniform(0.2, 0.6))
    print(f"{user} заходить у кафе ")
    print(f"{user} стає в чергу ")
    with line_lock:
        print(f"{user} робить замовлення ")
        available = get_available_drinks()
        if not available:
            print(f"{user} не може зробити замовлення — напої відсутні ")
            print(f"{user} залишає кафе без напою ")
            with results_lock:
                results.append((user, None, None))
            return
        drink_name = random.choice(available)
        info = drinks[drink_name]
        if info["stock"] is not None:
            info["stock"] -= 1
        print(f"{user} замовляє {drink_name} ")
        prep_min, prep_max = info["prep_time"]
        prep_time = random.uniform(prep_min, prep_max)
        time.sleep(prep_time)
        print(f"{user} отримує {drink_name} ")
    mode = random.choice(["inside", "takeout"])
    if mode == "inside":
        print(f"{user} споживає {drink_name} всередині ")
        time.sleep(random.uniform(1.0, 2.0))
        print(f"{user} закінчує споживання ")
    else:
        print(f"{user} забирає {drink_name} з собою ")
    time.sleep(0.3)
    print(f"{user} виходить з кафе ")

    with results_lock:
        results.append((user, drink_name, mode))
print("Початок сценарію\n")

threads = []

for user in users:
    t = threading.Thread(target=user_scenario, args=(user,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Кінець сценарію\n")
print("Підсумки:")

for user, drink, mode in results:
    if drink is None:
        print(f" - {user} не отримав напій ")
    else:
        mode_text = "споживав всередині " if mode == "inside" else "забрав з собою "
        print(f" - {user} отримав {drink} і {mode_text} ")