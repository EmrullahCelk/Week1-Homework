boy = float(input("Enter your height: "))
kilo = float(input("Enter your weight: "))
VKI =  kilo / boy ** 2
print("Body Mass Index: ", VKI)

if VKI < 25:
        print("Normal")
elif 25 <= VKI <30:
        print("Your Body Mass Index is Above Normal. You Are Overweight")
elif 30 <= VKI < 40:
        print("Your Body Mass Index is above normal. You are obese")
else:
        print("Your Body Mass Index is above normal. You Are Extremely Fat.")
    