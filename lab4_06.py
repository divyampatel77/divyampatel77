# Print 24 hours with suffixes
for hour in range(24):
    if hour == 0:
        print("12 AM - Midnight")
    elif hour < 12:
        print(f"{hour} AM")
    elif hour == 12:
        print("12 PM - Noon")
    else:
        print(f"{hour % 12} PM")
