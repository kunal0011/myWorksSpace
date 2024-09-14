package amazon;

public class MultiplyComplexNumber {
    public String complexNumberMultiply(String num1, String num2) {
        // Parse the two complex numbers
        String[] complex1 = num1.split("[+i]");
        String[] complex2 = num2.split("[+i]");

        int a = Integer.parseInt(complex1[0]); // Real part of num1
        int b = Integer.parseInt(complex1[1]); // Imaginary part of num1
        int c = Integer.parseInt(complex2[0]); // Real part of num2
        int d = Integer.parseInt(complex2[1]); // Imaginary part of num2

        // Calculate the real and imaginary parts of the product
        int realPart = a * c - b * d;
        int imaginaryPart = a * d + b * c;

        // Return the result in the form "real+imaginaryi"
        return realPart + "+" + imaginaryPart + "i";
    }
}
