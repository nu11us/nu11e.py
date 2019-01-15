import java.util.ArrayList;

public class Node {
    public String key;
    public int weight;
    public Node parent;
    public Node left;
    public Node right;
    public String color;

    public Node(int value) {
        key = Integer.toString(value);
        weight = 0;
        parent = null;
        left = null;
        right = null;
        color = null;
    }

    public Node(int value, int weight) {
        key = Integer.toString(value);
        weight = 0;
        parent = null;
        left = null;
        right = null;
        color = null;
    }
}

public class BinaryTree {
    private Node origin;
    private Hashtable<String, Node> nodes = new Hashtable<String, Node>();

    public BinaryTree() {
        origin = new Node(0);
        nodes = new ArrayList<Node>();
        nodes.put(Integer.parseInt(origin.key), origin);
    }

    public void addNode(Node parent) {
        parent.right = new Node(Integer.parseInt(parent.key) + "0");
        parent.right.parent = parent;
        parent.right.weight = 0;
        nodes.put(Integer.parseInt(parent.right.key), parent.right);
    }

    public void addNode(Node parent, boolean direction) {
        if (direction) {
            parent.left = new Node(Integer.parseInt(parent.key) + "1");
            parent.left.parent = parent;
            parent.left.weight = 0;
            nodes.put(Integer.parseInt(parent.left.key), parent.left);
        } else {
            addNode(parent);
        }
    }

    public void addNode(Node parent, int weight) {
        if (weight != 0) {
            parent.right = new Node(Integer.parseInt(parent.key) + "0");
            parent.right.parent = parent;
            parent.right.weight = weight;
            nodes.put(Integer.parseInt(parent.right.key), parent.right);
        } else {
            addNode(parent);
        }
    }

    public void addNode(Node parent, boolean direction, int weight) {
        if (!direction) {
            addNode(parent, weight);
        } else if (weight == 0) {
            addNode(parent, direction);
        } else {
            parent.left = new Node(Integer.parseInt(parent.key) + "1");
            parent.left.parent = parent;
            parent.left.weight = weight;
            nodes.put(Integer.parseInt(parent.left.key), parent.left);
        }
    }

    public int height(String node_key) {
        Node select = nodes.get(node_key);
        int h = 0;
        while (select.parent != null) {
            h += 1;
            select = select.parent;
        }
        return h;
    }

    public int nodeValue(String node_key) {
        Node select = nodes.get(node_key);
        int h = 0;
        while (select.parent != null) {
            h += select.weight;
            select = select.parent;
        }
        return h;
    }
}

public class RBTree extends BinaryTree {
    private Node origin;
    private Hashtable<String, Node> nodes = new Hashtable<String, Node>();

    public RBTree() {
        origin = new Node(0);
        origin.color = "black";
        nodes.put(Integer.parseInt(origin.key), origin);
    }

    public String colorize(Node parent) {
        if (parent.color == "black") {
            return "red";
        } else if (parent.color == "red") {
            return "black";
        } else {
            return null;
        }
    }

    public void addNode(Node parent) {
        super.addNode(parent);
        parent.right.color = colorize(parent);
    }

    public void addNode(Node parent, boolean direction) {
        super.addNode(parent, direction);
        if (direction) {
            parent.left.color = colorize(parent);
        } else {
            parent.right.color = colorize(parent);
        }
    }

    public void addNode(Node parent, int weight) {
        super.addNode(parent, weight);
        parent.right.color = colorize(parent);
    }

    public void addNode(Node parent, boolean direction, int weight) {
        super.addNode(parent, direction, weight);
        if (direction) {
            parent.left.color = colorize(parent);
        } else {
            parent.right.color = colorize(parent);
        }
    }
}