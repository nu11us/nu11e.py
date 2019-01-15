
public class Geometry {
    public static double polygon_area(double[][] points) {
        int n = points.length;
        double s1 = 0;
        double s2 = 0;
        for (int i = 0; i < n - 1; i++) {
            s1 += points[i][0] * points[i + 1][1] + points[n - 1][0] * points[0][1];
            s2 += points[i + 1][0] * points[i][1] + points[0][0] * points[n - 1][1];
        }
        return 0.5 * abs(s1 - s2);
    }
}