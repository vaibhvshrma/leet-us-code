import java.util.Scanner;
import java.util.TreeSet;

class longestSubstrWoRepChars {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String seq = sc.next();
        sc.close();

        System.out.println(lngstSubstrWoRepChars(seq));
    }

    static int lngstSubstrWoRepChars(String seq) {
        int i,j,mxLen = 1;

        i = 0;
        j = 1;

        TreeSet<Character> set = new TreeSet<Character>();

        set.add(seq.charAt(0));

        while (j < seq.length()) {
            
            char c = seq.charAt(j);
            
            if (set.contains(c)) {
                while (seq.charAt(i) != c) {
                    set.remove(seq.charAt(i));
                    i++;
                }
                i++;
            }
            else {
                set.add(c);
            }
            
            mxLen = Math.max(mxLen, j-i+1);
            j++;
        }

        return mxLen;
    }
}