import java.util.Scanner;

class Solution {
    boolean isNum(char c) {
        return c >= '0' && c <= '9';
    }
    
    public int myAtoi(String str) {
        str = str.trim();
        
        if (str.length() == 0) {
            return 0;
        }
        
        int res = 0;
        boolean negative = false;
        
        int i = 0;
        
        char sign = str.charAt(0);

        if (!isNum(sign)) {
            negative = sign == '-';
            if (sign == '-' || sign == '+')
                i++;
        }
        
        while(i < str.length() && isNum(str.charAt(i))) {
            if (negative) {
                
                int j = 9, k = res;
                
                while(j-- > 0) {
                    res += k;
                        if(res > 0) {
                            return Integer.MIN_VALUE;
                        }
                }
                
                res = res - (str.charAt(i++) - '0');
            }
            else {
                
                int j = 9, k = res;
                
                while(j-- > 0) {
                    res += k;
                        if(res < 0) {
                            return Integer.MAX_VALUE;
                        }
                }
                
                res = res + (str.charAt(i++) - '0');
            }

            if ((negative ? -1L : 1L) * (long) res < 0L) {
                return (!negative ? Integer.MAX_VALUE : Integer.MIN_VALUE);
            }

        }
        
        return res;   
    }
}

class Driver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 100; i++) {
            String st = sc.next();
            System.out.println(sol.myAtoi(st));
        }

        sc.close();
    }
}