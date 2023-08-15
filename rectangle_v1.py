def calculate_area(length: float, width: float) -> float:
    ''''
    Calculate the area of the rectangle using the length and width.

    Args:
        length - The length of the rectangle
        width - The height of the rectangle

    Return
        The calculated area of the rectangle
    '''
    return length * width


def calculate_perimeter(length: float, width: float) -> float:
    ''''
    Calculate the perimeter of the rectangle using the length and width.

    Args:
        length - The length of the rectangle
        width - The height of the rectangle

    Return
        The calculated perimeter of the rectangle
    '''
    return 2 * (length + width)


def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

if __name__ == "__main__":
    main()