import java.util.ArrayList;

public class Queue {
    private ArrayList items;

    public Queue() {
        items = new ArrayList<>();
    }

    public int length() {
        return items.size();
    }

    public boolean empty() {
        return items.isEmpty();
    }

    public void enqueue(Object x) {
        items.add(x);
    }

    public void dequeue() {
        items.remove(0);
    }
}