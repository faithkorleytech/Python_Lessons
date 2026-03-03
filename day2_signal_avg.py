heart_rate = [70, 72, 68, 74]
total = 0

for rate in heart_rate:
    total += rate

average = total / len(heart_rate)

print(f"Total Samples: {len(heart_rate)}")
print(f"Average heart rate: {average:.1f} BPM")

if average > 80:
    print("Alert: High Heart Rate Detected!")
    print(
        f"Average heart rate: {average:.1f} BPM exceeds saftey threshold of 80")

elif average < 60:
    print("Alert: Low Heart Rate Detected!")
else:
    print("Status: Heart rate is normal")
    print("Patient is Stable")

print(f"\nAnalysis complete for {len(heart_rate)} data points.")

peak_value = max(heart_rate)
print(f"The highest peak detected is {peak_value} BPM")
