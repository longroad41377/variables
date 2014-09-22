try:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    lowdepth = float(input("Enter shallow end depth: "))
    highdepth = float(input("Enter deep end depth: "))

    area = length * width
    topvolume = area * lowdepth
    lowvolume = (area * (highdepth - lowdepth)) / 2
    volume = topvolume + lowvolume

    print("Volume: {}".format(volume))

except ValueError:
    print("The values need to be numbers")
