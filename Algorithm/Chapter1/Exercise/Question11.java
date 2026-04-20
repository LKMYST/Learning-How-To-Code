package Algorithm.Chapter1.Exercise;

public class Question11 {
    public static void displayMatrix(boolean[][] m) {
        for (boolean[] e : m) {
            for (boolean i : e) {
                System.out.print(i ? "*" : " ");
            }
            System.out.print("\n");
        }
    }
}
