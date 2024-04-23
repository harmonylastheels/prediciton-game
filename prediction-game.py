import random


def future_vacation():
    print("Vacation Prediction Game\n")
    name = input("What's your name? ")
    print("\nThink of 3 vacation destinations, modes of transportation, activities, and souvenirs.")

    destinations = [input("Destination #{}: ".format(i + 1)) for i in range(3)]
    transportation = [input("Transportation #{}: ".format(i + 1)) for i in range(3)]
    activities = [input("Activity #{}: ".format(i + 1)) for i in range(3)]
    souvenirs = [input("Souvenir #{}: ".format(i + 1)) for i in range(3)]

    destination = random.choice(destinations)
    transport = random.choice(transportation)
    activity = random.choice(activities)
    souvenir = random.choice(souvenirs)

    print("\nResults for {}:".format(name))
    print("prepare to travel to " + destination + " by " + transport + " and do some "
          + activity + ", where you find a " + souvenir + " to take home.")


if __name__ == "__main__":
    future_vacation()
