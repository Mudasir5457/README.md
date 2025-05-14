def calculate_average(data):
    return sum(data) / len(data)

data = [72, 55, 101, 90]
average = calculate_average(data)
print("Average PM2.5:", average)

stations = [
    ['A1', 62],
    ['A2', 85],
    ['A3', 105],
    ['A4', 78]
]

for station in stations:
    print(f"{station[0]} → {station[1]}")

def report_status(stations, threshold):
    for station in stations:
        name, pm25 = station
        status = "OK" if pm25 <= threshold else "ALERT"
        print(f"{name} → {pm25} ({status})")

report_status(stations, 100)
