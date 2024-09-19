package amazon;

import java.util.*;

class UnionFind721 {
    public Map<String, String> parent;

    public UnionFind721() {
        parent = new HashMap<>();
    }

    public String find(String x) {
        if (!parent.get(x).equals(x)) {
            parent.put(x, find(parent.get(x)));  // Path compression
        }
        return parent.get(x);
    }

    public void union(String x, String y) {
        String rootX = find(x);
        String rootY = find(y);
        if (!rootX.equals(rootY)) {
            parent.put(rootX, rootY);
        }
    }

    public void add(String x) {
        if (!parent.containsKey(x)) {
            parent.put(x, x);  // Initialize parent of the email to itself
        }
    }
}

public class AccountsMerge721 {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        UnionFind721 uf = new UnionFind721();
        Map<String, String> emailToName = new HashMap<>();

        // Initialize Union-Find structure and map emails to names
        for (List<String> account : accounts) {
            String name = account.get(0);
            String firstEmail = account.get(1);
            uf.add(firstEmail);
            emailToName.put(firstEmail, name);

            for (int i = 1; i < account.size(); i++) {
                String email = account.get(i);
                uf.add(email);
                emailToName.put(email, name);
                uf.union(firstEmail, email);  // Union emails of the same person
            }
        }

        // Group emails by their root parent (i.e., their representative)
        Map<String, List<String>> mergedAccounts = new HashMap<>();
        for (String email : uf.parent.keySet()) {
            String rootEmail = uf.find(email);
            mergedAccounts.computeIfAbsent(rootEmail, x -> new ArrayList<>()).add(email);
        }

        // Prepare the result with sorted emails and corresponding names
        List<List<String>> result = new ArrayList<>();
        for (List<String> emails : mergedAccounts.values()) {
            Collections.sort(emails);
            String name = emailToName.get(emails.get(0));
            List<String> account = new ArrayList<>();
            account.add(name);
            account.addAll(emails);
            result.add(account);
        }

        return result;
    }

    // Test the function
    public static void main(String[] args) {
        AccountsMerge721 sol = new AccountsMerge721();

        List<List<String>> accounts1 = Arrays.asList(
                Arrays.asList("John", "johnsmith@mail.com", "john00@mail.com"),
                Arrays.asList("John", "johnnybravo@mail.com"),
                Arrays.asList("John", "johnsmith@mail.com", "john_newyork@mail.com"),
                Arrays.asList("Mary", "mary@mail.com")
        );
        System.out.println(sol.accountsMerge(accounts1));
        // Output:
        // [
        //   ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        //   ["John", "johnnybravo@mail.com"],
        //   ["Mary", "mary@mail.com"]
        // ]
    }
}
