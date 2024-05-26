package greedy;

import java.util.*;

class Activity {
    int start, finish;

    public Activity(int start, int finish) {
        this.start = start;
        this.finish = finish;
    }
}

public class ActivitySelection {

    public static List<Activity> selectActivities(Activity[] activities) {
        List<Activity> selectedActivities = new ArrayList<>();

        // Sort activities by finish time
        Arrays.sort(activities, Comparator.comparingInt(a -> a.finish));

        // Select the first activity (activity with the earliest finish time)
        selectedActivities.add(activities[0]);
        int prevFinishTime = activities[0].finish;

        // Iterate over the remaining activities and select mutually compatible ones
        for (int i = 1; i < activities.length; i++) {
            if (activities[i].start >= prevFinishTime) {
                selectedActivities.add(activities[i]);
                prevFinishTime = activities[i].finish;
            }
        }

        return selectedActivities;
    }

    public static void main(String[] args) {
        Activity[] activities = {
                new Activity(1, 4),
                new Activity(3, 5),
                new Activity(0, 6),
                new Activity(5, 7),
                new Activity(3, 8),
                new Activity(5, 9),
                new Activity(6, 10),
                new Activity(8, 11),
                new Activity(8, 12),
                new Activity(2, 13),
                new Activity(12, 14)
        };

        List<Activity> selectedActivities = selectActivities(activities);
        System.out.println("Selected Activities:");
        for (Activity activity : selectedActivities) {
            System.out.println("Start: " + activity.start + ", Finish: " + activity.finish);
        }
    }
}
