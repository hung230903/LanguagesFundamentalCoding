import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class comp {

    public static int sum(int n){
        int s = 0;
        while(n != 0){
            s += n % 10;
            n /= 10;
        }

        return s;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //sorting func
        int[] a = {2,3,5,4,6,8,7,9,1};
        
        for(int i = 0; i < 9; i++){
            System.out.print(a[i] + " ");
        }
        System.out.println("");

        Arrays.sort(a); //sorting algo - O(nlogn) - 10^7
        for(int i = 0; i < 9; i++){
            System.out.print(a[i] + " ");
        }
        System.out.println("");
        
        int[] b = {2,3,5,4,6,8,7,9,1};
        Arrays.sort(b, 2, 5); //sorting from 2 -> 4
        for(int i = 0; i < 9; i++){
            System.out.print(b[i] + " ");
        }
        System.out.println("");

        //Comparator
        Integer[] c = {2,3,5,4,6,8,7,9,1};
        Arrays.sort(c, new Comparator<Integer>(){
            @Override
            public int compare(Integer o1, Integer o2){
                return Integer.compare(o2, o1);
                //Nếu muốn o1 xuất hiện trước o2 -> trả về -1
                //Nếu muốn o2 xuất hiện trước o1 -> trả về 2
                // if(o1 < o2){
                //     return -1;
                // }
                // else{
                //     return 1;
                // }
            }
        });
        for(int x : c){
            System.out.print(x + " ");
        }
        System.out.println("");

        //
        Integer[] d = {-2,3,-5,4,-6,8,-7,9,1};
        Arrays.sort(d, new Comparator<Integer>(){
            @Override
            public int compare(Integer o1, Integer o2){
                return Integer.compare(Math.abs(o1), Math.abs(o2));
            }
        });
        for(int x : d){
            System.out.print(x + " ");
        }
        System.out.println("");

        //
        Integer[] e = {111, 2, 3, 243, 12, 1, 10, 1000};
        Arrays.sort(e, new Comparator<Integer>(){
            @Override
            public int compare(Integer o1, Integer o2){
                if(sum(o1) != sum(o2)){
                    return Integer.compare(sum(o1), sum(o2));
                }
                else{
                    return Integer.compare(o1, o2);
                }
            }
        });
        for(int x : e){
            System.out.print(x + " ");
        }

        sc.close();
    } 
}
