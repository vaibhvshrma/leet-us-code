import java.util.Scanner;

/**
 * reverseNum
 */
class Solution {
    public int reverse(int x) {
        String num = Integer.toString(x);
        int sign = 1; 
        if(num.charAt(0) == '-') {
            num = num.substring(1);
            sign = -1;
        }

        int k,res = 0;

        for (int i = num.length()-1; i > -1; i--) {
            char c = num.charAt(i);

            k = res;

            for (int j = 0; j < 9; j++) {
                res += k;
                if (res < 0) {
                    return 0;
                }
            }

            res += c - '0';

            if (res < 0)
                return 0;
        }

        return sign * res;
    }
}

class Driver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 100; i++) {
            int x = sc.nextInt();
            System.out.println(sol.reverse(x));
        }
    }
}