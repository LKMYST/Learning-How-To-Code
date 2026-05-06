package Stack;

public interface Stack {
    Object peek();
    void push(Object o);
    Object pop();
    int size();
    boolean isEmpty();
}