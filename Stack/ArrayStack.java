package Stack;

public class ArrayStack implements Stack{
    private Object[] a;
    private int size;

    public ArrayStack() {
        a = new Object[10];
    }

    public ArrayStack(int capacity) {
        a = new Object[capacity];
    }
    
    @Override
    public Object peek() {
        if (size == 0)
            throw new IllegalStateException("Stack is empty! ");
        return a[size - 1];
    }

    @Override
    public void push(Object object) {
        if (size == a.length)
            resize();
        a[size++] = object;
    }

    @Override
    public Object pop() {
        if (size == 0)
            throw new IllegalStateException("Stack is empty! ");

        Object object = a[--size];
        a[size] = null;
        
        return object;
    }
    
    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    private void resize() {
        Object[] newA = new Object[a.length * 2];

        for (int i = 0; i < size; i++) {
            newA[i] = a[i];
        }

        a = newA;
    }
}
