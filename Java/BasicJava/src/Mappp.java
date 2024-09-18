import java.util.Map;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.TreeMap;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Set;
import java.util.ArrayList;

public class Mappp {
    public static void main(String[] args) {
        //HashMap
        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Double, Float> map2 = new HashMap<>();
        HashMap<Character, Integer> map3 = new HashMap<>();

        map1.put(1, 2); //(1 ,2)
        map1.put(2, 3); //(1 ,2), (2, 3)
        map1.put(3, 4); //(1 ,2), (2, 3), (3, 4)
        map1.put(2, 5); //(1 ,2), (2, 5), (3, 4)
        map1.put(2, 1); //(1 ,2), (2, 1), (3, 4)
        System.out.println(map1.size());

        //get() lấy value tương ứng với key cho vào hàm
        System.out.println(map1.get(1));
        System.out.println(map1.get(2));
        System.out.println(map1.get(3));

        //
        System.out.println(map1.containsKey(3));
        System.out.println(map1.containsKey(7));
        System.out.println(map1.containsValue(2));
        System.out.println(map1.containsValue(17));

        //
        map1.replace(2, 5);
        System.out.println(map1.get(2));

        //
        HashMap<Integer, Integer> map4 = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        int[] a = {1 ,2, 3, 1, 2, 7, 8, 9 ,2};
        for(int i = 0; i < 9 ; i++){
            map4.put(a[i], 1);
        }
        System.out.println(map4.size());

        //
        HashMap<Integer, Integer> map5 = new HashMap<>();
        int n = sc.nextInt();
        int[] b = new int[n];
        for(int i = 0; i < n; i++){
            b[i] = sc.nextInt();
            if(map5.containsKey(b[i])){
                int fre = map5.get(b[i]);
                fre++;
                map5.put(b[i], fre);
            }
            else{
                map5.put(b[i], 1);
            }
        }

        Arrays.sort(b);
        for(int i = 0; i < n; i++){
            if(map5.containsKey(b[i])){
                System.out.println(b[i] + " " + map5.get(b[i]));
                map5.remove(b[i]);
            }
        }
        System.out.println();
        
        //Duyệt map và in các ra map
        HashMap<Integer, Integer> map6 = new HashMap<>();
        map6.put(1, 2); 
        map6.put(2, 3); 
        map6.put(4, 4);
        map6.put(7, 4);
        map6.put(8, 4);
        map6.put(9, 4);
        map6.put(3, 4);
        Set<Map.Entry<Integer, Integer>> entrySet1 = map6.entrySet();
        for(Map.Entry<Integer, Integer> entry : entrySet1){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
        System.out.println();
        
        ArrayList<Map.Entry<Integer, Integer>> arr = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry : entrySet1){
            arr.add(entry);
        }


        for(int i = 0; i < arr.size(); i++){
            System.out.println(arr.get(i).getKey() + " " + arr.get(i).getValue());
        }

        System.out.println();

        //
        LinkedHashMap<Integer, Integer> map7 = new LinkedHashMap<>();
        map7.put(1, 2); 
        map7.put(4, 4);
        map7.put(2, 3); 
        map7.put(3, 4);
        map7.put(6, 4);
        map7.put(5, 4);
        Set<Map.Entry<Integer, Integer>> entrySet2 = map7.entrySet();
        for(Map.Entry<Integer, Integer> entry : entrySet2){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
        System.out.println();

        //
        TreeMap<Integer, Integer> map8 = new TreeMap<>();
        map8.put(1, 2); 
        map8.put(4, 4);
        map8.put(2, 3); 
        map8.put(3, 4);
        map8.put(6, 4);
        map8.put(5, 4);
        Set<Map.Entry<Integer, Integer>> entrySet3 = map8.entrySet();
        for(Map.Entry<Integer, Integer> entry : entrySet3){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }


        


        sc.close();


    }
    
}
