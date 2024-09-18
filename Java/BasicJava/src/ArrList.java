import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;
import java.util.Collections;

public class ArrList {
    public static void main(String[] args) {
        ArrayList<Integer> arr1 = new ArrayList<>();
        arr1.add(1);
        arr1.add(3);
        arr1.add(5);
        arr1.add(2);
        arr1.add(4);
        System.out.println(arr1.size());
        for(int i = 0; i < arr1.size(); i++){
            System.out.print(arr1.get(i) + " ");
        }
        System.out.println();
        
        Collections.sort(arr1, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2){
                return Integer.compare(o2, o1);
            }
    
        });

        for(int x : arr1){
            System.out.print(x + " ");
        }
        System.out.println();

        //
        ArrayList<Integer> arr2 = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            arr2.add(sc.nextInt());
        }
        for(int i = 0; i < n; i++){
            System.out.print(arr2.get(i) + " ");
        }
        System.out.println();

        //
        System.out.println(arr2.contains(5)); //O(n)

        //
        arr2.set(2, 88);
        for(int i = 0; i < n; i++){
            System.out.print(arr2.get(i) + " ");
        }
        System.out.println();

        //
        arr2.remove((Object)1);
        for(int x : arr2){
            System.out.print(x + " ");
        }
        System.out.println();

        //
        arr2.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2){
                return Integer.compare(o1, o2);
            }
        });

        for(int x : arr2){
            System.out.print(x + " ");
        }
        System.out.println();

        //
        System.out.println(arr2.indexOf(3));
        System.out.println(arr2.indexOf(2));

        //
        arr2.clear();
        System.out.println(arr2.isEmpty());

        sc.close();
    }
}
