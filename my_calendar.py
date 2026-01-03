import calendar

# Year
year = 2026

# List of festival dates you want to show (day numbers)
# Format: month: {day: "Name"}
festivals = {
    1: {1: "NewYr", 13: "Lohri", 14: "Sankr", 26: "RepDay"},
    2: {15: "Shivratri"},
    3: {3: "Holika", 4: "Holi"},
    4: {3: "GoodFri"},
    5: {1: "Buddha"},
    8: {15: "IndDay", 26: "Onam", 28: "Raksha"},
    9: {4: "Janmasht"},
    10: {20: "Dussehra"},
    11: {8: "Diwali", 24: "GuruN"},
    12: {25: "Xmas"},
}

for month in range(1, 13):
    print(calendar.month(year, month))
    
    # Print festivals in this month
    if month in festivals:
        for day, name in sorted(festivals[month].items()):
            print(f"{day:2d}-{month:02d}-{year}: {name}")
    print("-" * 30)
