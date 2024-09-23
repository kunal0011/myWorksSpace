package amazon;

import java.util.*;
interface NestedInteger {

      // @return true if this NestedInteger holds a single integer, rather than a nested list.
      public boolean isInteger();

      // @return the single integer that this NestedInteger holds, if it holds a single integer
      // Return null if this NestedInteger holds a nested list
      public Integer getInteger();

      // @return the nested list that this NestedInteger holds, if it holds a nested list
     // Return empty list if this NestedInteger holds a single integer
      public List<NestedInteger> getList();
  }


public class FlattenListiterator341 implements Iterator<Integer> {
    private List<Integer> flatList;
    private int index;

    public FlattenListiterator341(List<NestedInteger> nestedList) {
        flatList = new ArrayList<>();
        flatten(nestedList);
        index = 0;
    }

    private void flatten(List<NestedInteger> nestedList) {
        for (NestedInteger ni : nestedList) {
            if (ni.isInteger()) {
                flatList.add(ni.getInteger());
            } else {
                flatten(ni.getList());
            }
        }
    }

    @Override
    public Integer next() {
        return flatList.get(index++);
    }

    @Override
    public boolean hasNext() {
        return index < flatList.size();
    }
}

