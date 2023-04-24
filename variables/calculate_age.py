age = input("Please state your age: ")
years = int(age)
months = 12 * years
days = 365 * years
hours = 24 * days
minutes = 60 * hours
seconds = 60 * minutes


print(
    f"Your age is {age} which is the equivelent of:")
print(f"{months} months or {days} days or {hours} hours or {minutes} minutes or {seconds} seconds")
