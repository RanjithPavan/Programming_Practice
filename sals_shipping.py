# weight = 4.8
def normal_ground_shipping(weight):
    if (weight <= 2.0):
        return 1.5 * weight + 20.00
    elif (weight > 2.0 and weight <= 6.0):
        return 3.00 * weight + 20.00
    elif (weight > 6.0 and weight <= 10.00):
        return 4.00 * weight + 20.00
    else:
        return 4.75 * weight + 20.00


premium = 125.00


def drone_shipping(weight):
    if (weight <= 2.0):
        return 4.5 * weight
    elif (weight > 2.0 and weight <= 6.0):
        return 9.00 * weight
    elif (weight > 6.0 and weight <= 10.00):
        return 12.00
    else:
        return 14.25 * weight


# print(normal_ground_shipping(8.4))
# print(drone_shipping(1.5))

def cheapest_shipping(weight):
    ground = normal_ground_shipping(weight)
    drone = drone_shipping(weight)
    if (ground < drone and ground < premium):
        print("Cheapest way to ship is ground and it costs " + str(ground))
    elif (drone < ground and drone < premium):
        print("Cheapest way to ship is drone and it costs " + str(drone))
    else:
        print("Cheapest way to ship is premium and it costs " + str(premium))


cheapest_shipping(41.5)
