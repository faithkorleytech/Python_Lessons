import math

print("--- Electrical Engineering: Impedence Calculator ---")

r = float(input("Enter Resistance (R): "))
x = float(input("Enter Reactance (X): "))

z = complex(r, x)
magnitude = abs(z)

angle_rad = math.atan2(x, r)
angle_deg = math.degrees(angle_rad)

print("-" * 30)
print(f"Rectangular Form: Z = {z} ohms")
print(
    f"Polar Form: Magnitude = {magnitude:.2f} ohms, Angle = {angle_deg:.1f}°")
