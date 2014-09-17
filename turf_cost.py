def calc_turf_cost():
    try:
        length = float(input("Enter garden length: "))
        width = float(input("Enter garden width: "))
        garden_area = length * width
        print("Area of garden is {} m^2".format(garden_area))
        length = length - 2
        width = width - 2
        if length < 0 or width < 0:
            print("The border is bigger than the garden")
            return
        in_border_area = length * width
        turf_cost = in_border_area * 10
        print("Cost of turf is £{}".format(turf_cost))
    except ValueError:
        print("The values must be numbers")
        calc_turf_cost()

calc_turf_cost()
