package Algorithm.Chapter1.Exercise;

public class Question9 {
    public static String toBinaryString(int n) {
        if (n == 0){
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for (int i = n; i > 0; i /= 2) {
            sb.append(i % 2);
        }
        return sb.reverse().toString();
    }
}
