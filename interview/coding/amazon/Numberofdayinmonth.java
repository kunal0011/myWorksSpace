package amazon;

public class Numberofdayinmonth {
    public int numberOfDays(int Y, int M) {
        // Check if it's February
        if (M == 2) {
            // Leap year check
            if ((Y % 4 == 0 && Y % 100 != 0) || (Y % 400 == 0)) {
                return 29;
            } else {
                return 28;
            }
        }
        // Months with 31 days
        else if (M == 1 || M == 3 || M == 5 || M == 7 || M == 8 || M == 10 || M == 12) {
            return 31;
        }
        // Months with 30 days
        else {
            return 30;
        }
    }
}
