def rectangle(width, length):
    area = width * length
    circumference = 2 * (width + length)
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")


width = int(input("Width value: "))
length = int(input("Length value: "))


rectangle(width, length)
