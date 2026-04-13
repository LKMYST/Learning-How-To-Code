package Stack;

public class Main {
    public static void main(String[] args) {
        ArrayStack as = new ArrayStack();

        System.out.println(as.isEmpty());
        as.push(1);
        as.push('a');
        System.out.println(as.peek());
        as.pop();
        System.out.println(as.peek());
        System.out.println(as.isEmpty());
        as.pop();
        System.out.println(as.isEmpty());
    }
}
