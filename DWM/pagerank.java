package DWM;

import java.util.Arrays;
public class pagerank{
    public static void main(String[] args) {
        //step 1 create link matrix, which page is linked to what
        double[][] link = {
                {0, 1, 0, 1},
                {1, 0, 0, 1},
                {1, 1, 0, 0},
                {0, 0, 1, 0}
        };

        //create variables
        int n = link.length;
        double dampingFactor = 0.85;
        double tolerance = 0.0001;

        //create initial pagerank matrix and initialize it with 1/n
        double[] pageRank = new double[n];
        Arrays.fill(pageRank, 1.0/n);

        //formula is
        // (1-d)/n + d*sumation of (pageRank/outgoinglink)

        //so first we will calculate outgoing link for each page
        double[] outGoing = new double[n];
        for (int i = 0; i < n; i++) {
            double sum=0;
            for (int j = 0; j < n; j++) {
                sum+=link[i][j];
            }
            outGoing[i] = sum;
        }

        //now we will calculate actual pagerank until convergence
        boolean convergence = false;
        int iterartion = 0;

        while (!convergence){
            double[] newPageRank = new double[n];
            for (int i = 0; i <n; i++) {
                double sum = 0;
                for (int j = 0; j < n; j++) {
                    if (link[i][j] == 1){
                        sum += pageRank[j]/outGoing[j];
                    }  
                }
                newPageRank[i] = (1-dampingFactor)/n + dampingFactor*sum;
            }

            convergence = true;
            for (int i = 0; i < n; i++) {
                if(Math.abs(newPageRank[i] - pageRank[i]) > tolerance){
                    convergence = false;
                    break;
                }
            }
            pageRank = newPageRank;
            iterartion++;
        }

        System.out.println("pagerank after " + iterartion + " are");
        for (int i = 0; i < n; i++) {
            System.out.println("page-" + (i+1) + ": " + pageRank[i]);
        }
    }
}