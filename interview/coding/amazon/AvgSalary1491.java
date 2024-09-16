package amazon;

public class AvgSalary1491 {
    public double average(int[] salary) {
        // Step 1: Find min and max salaries
        int minSalary = Integer.MAX_VALUE;
        int maxSalary = Integer.MIN_VALUE;
        int totalSum = 0;

        for (int sal : salary) {
            totalSum += sal;
            if (sal < minSalary) minSalary = sal;
            if (sal > maxSalary) maxSalary = sal;
        }

        // Step 2: Exclude min and max salaries
        totalSum -= (minSalary + maxSalary);

        // Step 3: Calculate the average of remaining salaries
        int count = salary.length - 2;
        return (double) totalSum / count;
    }

    // Testing
    public static void main(String[] args) {
        AvgSalary1491 solution = new AvgSalary1491();
        int[] salary = {4000, 3000, 1000, 2000};
        System.out.println("Java Test Result: " + solution.average(salary));  // Output should be 2500.0
    }
}

