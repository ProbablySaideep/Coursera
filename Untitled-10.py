def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # Only True if number == 1 (since base**0 = 1).
        return number == 1

    # Recursive case: keep dividing number by base,
    # but only if it's divisible.
    if number % base == 0:
        return is_power_of(number // base, base)

    # If not divisible, it's not a power.
    return False


print(is_power_of(8, 2))     # Should be True
print(is_power_of(64, 4))    # Should be True
print(is_power_of(70, 10))   # Should be False