int sumOfTheDigitsOfHarshadNumber(int x) {
    int sum = 0;
    int original = x; // Store the original number

    while (x > 0) {
        sum += x % 10;
        x /= 10;
    }

    // Check divisibility using original number
    return (original % sum == 0) ? sum : -1;
}