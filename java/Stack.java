import java.util.ArrayList;

public class Stack {
    private ArrayList items;

    public Stack() {
        items = new ArrayList<>();
    }

    public int length() {
        return items.size();
    }

    public boolean empty() {
        return items.isEmpty();
    }

    public void push(Object x) {
        items.add(0, x);
    }

    public void pull() {
        items.remove(items.size()-1);
    }
}