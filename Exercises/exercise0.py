import math


print ("Task 1:")


def hypotenuse(a: float, b: float) -> float:
    """Compute the hypotenuse given the two catheti using the Pythagorean theorem."""
    return math.hypot(a, b)


def other_cathetus(c: float, a: float) -> float:
    """Compute the other cathetus given hypotenuse c and cathetus a (c >= a)."""
    diff = c * c - a * a
    if diff < 0:
        raise ValueError("Hypotenuse must be greater than or equal to the given cathetus.")
    return math.sqrt(diff)


def main() -> None:
    # a) a=3, b=4 -> compute the hypotenuse
    a1, b1 = 3.0, 4.0
    c1 = hypotenuse(a1, b1)

    # b) c=7.0, a=5.0 -> compute the other cathetus, rounded to one decimal
    c2, a2 = 7.0, 5.0
    b2 = other_cathetus(c2, a2)
    b2_rounded = round(b2, 1)

    print(f"a) hypotenuse = {c1}")
    print(f"b) other cathetus = {b2_rounded}")


if __name__ == "__main__":
    main()





