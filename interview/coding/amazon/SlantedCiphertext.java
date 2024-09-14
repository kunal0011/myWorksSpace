package amazon;

public class SlantedCiphertext {
    public String decodeCiphertext(String encodedText, int rows) {
        if (rows == 1) return encodedText;

        int cols = encodedText.length() / rows;
        StringBuilder decodedText = new StringBuilder();

        for (int startCol = 0; startCol < cols; startCol++) {
            for (int row = 0, col = startCol; row < rows && col < cols; row++, col++) {
                decodedText.append(encodedText.charAt(row * cols + col));
            }
        }

        // Remove trailing spaces
        return decodedText.toString();
    }
}
