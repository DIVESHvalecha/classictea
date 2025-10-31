package DWM;

public class NaiveBayesOwn {
    // Training data (Outlook, Temperature, Humidity, Wind, Play)
    static String[][] data = {
            { "Sunny", "Hot", "High", "Weak", "No" },
            { "Sunny", "Hot", "High", "Strong", "No" },
            { "Overcast", "Hot", "High", "Weak", "Yes" },
            { "Rain", "Mild", "High", "Weak", "Yes" },
            { "Rain", "Cool", "Normal", "Weak", "Yes" },
            { "Rain", "Cool", "Normal", "Strong", "No" },
            { "Overcast", "Cool", "Normal", "Strong", "Yes" },
            { "Sunny", "Mild", "High", "Weak", "No" },
            { "Sunny", "Cool", "Normal", "Weak", "Yes" },
            { "Rain", "Mild", "Normal", "Weak", "Yes" },
            { "Sunny", "Mild", "Normal", "Strong", "Yes" },
            { "Overcast", "Mild", "High", "Strong", "Yes" },
            { "Overcast", "Hot", "Normal", "Weak", "Yes" },
            { "Rain", "Mild", "High", "Strong", "No" }
    };

    public static void main(String[] args) {
        // test data details
        String outlook = "Sunny";
        String temp = "Hot";
        String humidity = "Normal";
        String wind = "Strong";

        // calculate probability for yes and no
        double pNo = calculateProbability(outlook, temp, humidity, wind, "No");
        double pYes = calculateProbability(outlook, temp, humidity, wind, "Yes");

        System.out.println("probability of yes: " + pYes);
        System.out.println("probability of No: " + pNo);

        if (pYes > pNo) {
            System.out.println("yes");
        } else {
            System.out.println("No");
        }
    }

    private static double calculateProbability(String outlook, String temp, String humidity, String wind,
            String target) {

        // step 1 calculate total of yes and no
        int totalYes = 0, totalNo = 0;
        for (String[] row : data) {
            if (row[4].equals("Yes")) {
                totalYes++;
            } else {
                totalNo++;
            }
        }

        // set target as requried, (yes ka check kr rhe hai toh target yes else no) or
        // uski probability nikalo
        int totalTarget = target.equals("Yes") ? totalYes : totalNo;
        double prior = (double) totalTarget / data.length;

        // suppose target is yes, count values for each attribute, same for no
        int countOutlook = 0, countTemp = 0, countHumidity = 0, countWind = 0;
        for (String[] row : data) {
            if (row[4].equals(target)) {
                if (row[0].equals(outlook))
                    countOutlook++;
                if (row[1].equals(temp))
                    countTemp++;
                if (row[2].equals(humidity))
                    countHumidity++;
                if (row[3].equals(wind))
                    countWind++;
            }
        }

        // calculate probability of each count
        double pOutlook = (double) countOutlook / totalTarget;
        double pTemp = (double) countTemp / totalTarget;
        double pHumidity = (double) countHumidity / totalTarget;
        double pWind = (double) countWind / totalTarget;

        // multiply all
        return prior * pOutlook * pTemp * pHumidity * pWind;
    }
}
