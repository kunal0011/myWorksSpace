package amazon;

public class IsprefixOfWord1455 {
    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] words = sentence.split(" ");

        for (int i = 0; i < words.length; i++) {
            if (words[i].startsWith(searchWord)) {
                return i + 1;  // 1-based index
            }
        }

        return -1;
    }

    // Testing
    public static void main(String[] args) {
        IsprefixOfWord1455 solution = new IsprefixOfWord1455();
        String sentence = "i love eating burger";
        String searchWord = "burg";
        System.out.println("Java Test Result: " + solution.isPrefixOfWord(sentence, searchWord));  // Output should be 4
    }
}

