import java.util.ArrayList;
import java.util.Hashtable;

public class Graph {
    private Hashtable<Integer, ArrayList<ArrayList<Integer>>> connections;

    public Graph() {
        connections = new Hashtable<Integer, ArrayList<ArrayList<Integer>>>();
    }

    public ArrayList<Integer> vertices() {
        return Collections.list(connections.keys());
    }

    public ArrayList<Integer> islands() {
        ArrayList<Integer> lst = new ArrayList<Integer>();
        for (int i : vertices()) {
            if (neighbors(i).size() == 0) {
                lst.add(i);
            }
        }
        return lst;
    }

    public void add_edge(int start, int end) {
        int weight = 0;
        boolean bidirectional = false;
        add_edge(start, end, weight, bidirectional);
    }

    public void add_edge(int start, int end, int weight) {
        boolean bidirectional = false;
        add_edge(start, end, weight, bidirectional);
    }

    public void add_edge(int start, int end, boolean bidirectional) {
        int weight = 0;
        add_edge(start, end, weight, bidirectional);
    }

    public void add_edge(int start, int end, int weight, boolean bidirectional) {
        if (connections.get(start).contains(end)) {
            purge(start, end);
        }
        connections.get(start).add(new ArrayList<Integer>(Arrays.asList(end, weight)));
        if (bidirectional) {
            connections.get(end).add(new ArrayList<Integer>(Arrays.asList(start, weight)));
        }
    }

    public void remove_edge(int start, int end) {
        boolean bidirectional = false;
        remove_edge(start, end, bidirectional);
    }

    public void remove_edge(int start, int end, boolean bidirectional) {
        purge(start, end);
        if (bidirectional) {
            purge(end, start);
        }
    }

    public void add_vertex() {
        connections.put(vertices().size(), new ArrayList<ArrayList<Integer>>());
    }

    public void remove_vertex(int index) {
        connections.remove(index);
        if (vertices().size() > 0) {
            for (int i : vertices()) {
                purge(i, index);
            }
        }

    }

    public ArrayList<Integer> neighbors(int start) {
        boolean weighted = false;
        return neighbors(start, weighted);
    }

    public ArrayList<Integer> neighbors(int start, boolean weighted) {
        if (weighted) {
            return connections.get(start);
        } else {
            ArrayList<Integer> a = new ArrayList<Integer>();
            for (ArrayList<Integer> i : connections.get(start)) {
                a.add(i.get(0));
            }
            return a;
        }
    }

    public boolean connection(int start, int end) {
        if (vertices().contains(start)) {
            return connections.get(start).contains(end);
        } else {
            return false;
        }
    }

    public void purge(int start, int target) {
        ArrayList<ArrayList<Integer>> lst = new ArrayList<ArrayList<Integer>>();
        for (ArrayList<Integer> j : connections.get(start)) {
            if (j.get(0) != target) {
                lst.add(new ArrayList<Integer>(Arrays.asList(j.get(0), j.get(1))));
            }
        }
        connections = lst;
    }

    public int weight(int start, int end) {
        for (ArrayList<Integer> j : connections.get(start)) {
            if (j.get(0) == end) {
                return j.get(1);
            }
        }
        return 0;
    }
}