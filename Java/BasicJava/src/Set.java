import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.TreeSet;

public class Set {
    public static void main(String[] args) {
        //các phần tử trong set chỉ lưu đc các phần tửu khác nhau
        //set chỉ lưu đc các phần tử kiểu đối tượng
        //các phần tử trong set không có thứ tự, xuất hiện random khi in ra
        HashSet<Integer> set1 = new HashSet<>();
        set1.add(100);
        set1.add(200);
        set1.add(300);
        set1.add(400);
        set1.add(500);
        set1.add(400);
        set1.add(200);
        set1.add(300);
        
        for(int x : set1){
            System.out.print(x + " ");
            
        }
        System.out.println();

        //
        HashSet<Integer> set2 = new HashSet<>();
        int[] a = {1, 2, 3, 2, 4, 5, 6, 7, 8, 2, 5, 2, 2};

        for(int x : a){
            set2.add(x);
        }
        System.out.println(set1.size());
        for(int x : set2){
            System.out.print(x + " ");
        }
        System.out.println();

        //
        set2.remove(3);
        for(int x : set2){
            System.out.print(x + " ");
        }  
        System.out.println();

        //O(1)
        System.out.println(set2.contains(2));
        
        //giữ đc thứ tự sắp xếp của các phần tử trong set
        LinkedHashSet<Integer> set3 = new LinkedHashSet<>();
        int[] b = {3, 3, 1 ,2 , 5 ,6 , 7, 8, 9, 4, 2, 5, 26, 52};
        for(int x : b){
            set3.add(x);
        }

        for(int x : set3){
            System.out.print(x + " ");
        }
        System.out.println();

        //các phần tử trong set là tăng dần
        TreeSet<Integer> set4 = new TreeSet<>();
        int[] c = {3, 3, 1 ,2 , 5 ,6 , 7, 8, 9, 4, 2, 5, 26, 52};
        for(int x : c){
            set4.add(x);
        }

        for(int x : set4){
            System.out.print(x + " ");
        }

        

    }
}
