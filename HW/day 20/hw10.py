class Device:
    def power_on(self):
        print("Device is powered on")


class Laptop(Device):
    def laptop_feature(self):
        print("Laptop: Used for programming")


class Phone(Device):
    def phone_feature(self):
        print("Phone: Used for calling")


# Create Laptop object
l = Laptop()
l.power_on()
l.laptop_feature()

print()

# Create Phone object
p = Phone()
p.power_on()
p.phone_feature()
