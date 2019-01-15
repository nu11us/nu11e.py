
public class Crypto {
    public static int str_value(String x) {
        int sum = 0;
        for (char y : x.toLowerCase().toCharArray()) {
            sum += (int) (y) - 96;
        }
        return sum;
    }

    public static int str_value(char x) {
        return (int) (x) - 96;
    }

    public static String rot_shift(String text, int n) {
        String string2 = "";
        for (char y : text.toCharArray()) {
            string2 += (char) ((int) (y) + n);
        }
        return string2;
    }

    public static String rot_shift_alpha(String text, int n) {
        String string2 = "";
        for (char y : text.toLowerCase().toCharArray()) {
            int z = (int) (y) + n;
            if (z < 97) {
                string2 += (char) (123 - (97 - z));
            } else if (z > 122) {
                string2 += (char) (97 + (123 - z));
            } else {
                string2 += (char) z;
            }
        }
        return string2;
    }

}
