def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def area(rect_length, rect_width):
        return rect_length * rect_width

    def perimeter(rect_length, rect_width):
        return 2 * rect_length + 2 * rect_width

    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"
