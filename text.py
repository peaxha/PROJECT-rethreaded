from math import pi

def sphere_volume():
    print("\n-- Sphere Volume Rate --")
    mode = input("Do you know dV/dt or dr/dt? (V/r): ")
    r = float(input("Enter current radius: "))

    if mode == "r":
        drdt = float(input("Enter dr/dt: "))
        dVdt = 4 * pi * (r**2) * drdt
        print("dV/dt = " + str(round(dVdt, 6)))
    elif mode == "V":
        dVdt = float(input("Enter dV/dt: "))
        drdt = dVdt / (4 * pi * (r**2))
        print("dr/dt = " + str(round(drdt, 6)))
    else:
        print("Invalid input.")


def sphere_surface_area():
    print("\n-- Sphere Surface Area Rate --")
    mode = input("Do you know dA/dt or dr/dt? (A/r): ")
    r = float(input("Enter current radius: "))

    if mode == "r":
        drdt = float(input("Enter dr/dt: "))
        dAdt = 8 * pi * r * drdt
        print("dA/dt = " + str(round(dAdt, 6)))
    elif mode == "A":
        dAdt = float(input("Enter dA/dt: "))
        drdt = dAdt / (8 * pi * r)
        print("dr/dt = " + str(round(drdt, 6)))
    else:
        print("Invalid input.")


def cylinder_volume():
    print("\n-- Cylinder Volume Rate --")
    mode = input("Do you know dV/dt, dr/dt, or dh/dt? (V/r/h): ")
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    if mode == "r":
        drdt = float(input("Enter dr/dt: "))
        dhdt = float(input("Enter dh/dt (0 if constant height): "))
        dVdt = 2 * pi * r * h * drdt + pi * (r**2) * dhdt
        print("dV/dt = " + str(round(dVdt, 6)))
    elif mode == "h":
        dhdt = float(input("Enter dh/dt: "))
        drdt = float(input("Enter dr/dt (0 if constant radius): "))
        dVdt = 2 * pi * r * h * drdt + pi * (r**2) * dhdt
        print("dV/dt = " + str(round(dVdt, 6)))
    elif mode == "V":
        dVdt = float(input("Enter dV/dt: "))
        choice = input("Solve for dr/dt or dh/dt? (r/h): ")
        if choice == "r":
            dhdt = float(input("Enter dh/dt (0 if none): "))
            drdt = (dVdt - pi * (r**2) * dhdt) / (2 * pi * r * h)
            print("dr/dt = " + str(round(drdt, 6)))
        elif choice == "h":
            drdt = float(input("Enter dr/dt (0 if none): "))
            dhdt = (dVdt - 2 * pi * r * h * drdt) / (pi * (r**2))
            print("dh/dt = " + str(round(dhdt, 6)))
    else:
        print("Invalid input.")


def cone_volume():
    print("\n-- Cone Volume Rate --")
    mode = input("Do you know dV/dt, dr/dt, or dh/dt? (V/r/h): ")
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    if mode == "r" or mode == "h":
        drdt = float(input("Enter dr/dt: "))
        dhdt = float(input("Enter dh/dt: "))
        dVdt = (1.0/3.0) * pi * (2 * r * h * drdt + (r**2) * dhdt)
        print("dV/dt = " + str(round(dVdt, 6)))
    elif mode == "V":
        dVdt = float(input("Enter dV/dt: "))
        choice = input("Solve for dr/dt or dh/dt? (r/h): ")
        if choice == "r":
            dhdt = float(input("Enter dh/dt: "))
            drdt = (3*dVdt/pi - r**2 * dhdt) / (2*r*h)
            print("dr/dt = " + str(round(drdt, 6)))
        elif choice == "h":
            drdt = float(input("Enter dr/dt: "))
            dhdt = (3*dVdt/pi - 2*r*h*drdt) / (r**2)
            print("dh/dt = " + str(round(dhdt, 6)))
    else:
        print("Invalid input.")


def main():
    print("Universal Related Rates Solver")
    print("1. Sphere Volume")
    print("2. Sphere Surface Area")
    print("3. Cylinder Volume")
    print("4. Cone Volume")
    choice = input("Select problem type (1-4): ")

    if choice == "1":
        sphere_volume()
    elif choice == "2":
        sphere_surface_area()
    elif choice == "3":
        cylinder_volume()
    elif choice == "4":
        cone_volume()
    else:
        print("Invalid selection.")

main()
