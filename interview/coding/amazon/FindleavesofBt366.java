package amazon;

import java.util.*;

class TreeNode366 {
    int val;
    TreeNode366 left;
    TreeNode366 right;
    TreeNode366() {}
    TreeNode366(int val) { this.val = val; }
    TreeNode366(int val, TreeNode366 left, TreeNode366 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class FindleavesofBt366 {
    public List<List<Integer>> findLeaves(TreeNode366 root) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(root, res);
        return res;
    }

    private int dfs(TreeNode366 node, List<List<Integer>> res) {
        if (node == null) {
            return -1;
        }
        int left = dfs(node.left, res);
        int right = dfs(node.right, res);
        int height = Math.max(left, right) + 1;

        if (res.size() == height) {
            res.add(new ArrayList<>());
        }

        res.get(height).add(node.val);
        return height;
    }
}
