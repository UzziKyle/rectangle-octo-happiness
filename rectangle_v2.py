class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        ''''
            Calculate the area of the rectangle using the length and width.

            Args:
                length - The length of the rectangle
                width - The height of the rectangle

            Return
                The calculated area of the rectangle
        '''
        return self.length * self.width


    def calculate_perimeter(self) -> float:
        ''''
        Calculate the perimeter of the rectangle using the length and width.

        Args:
            length - The length of the rectangle
            width - The height of the rectangle

        Return
            The calculated perimeter of the rectangle
        '''
        return 2 * (self.length + self.width)


def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    rectangle = Rectangle(length=length, width=width)

    print(f"Area of the rectangle: {rectangle.calculate_area()}")
    print(f"Perimeter of the rectangle: {rectangle.calculate_perimeter()}")

if __name__ == "__main__":
    main()
