import java.util.Scanner;

public class OneDArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        //
        int[] a = new int[5];
        a[0] = 1;
        a[1] = 2;
        a[2] = 3;
        a[3] = 4;
        a[4] = 5;
        for(int i = 0; i < 5; i++){
            System.out.print(a[i] + " ");
        }
        
        //
        int n = sc.nextInt();
        int [] c = new int[n];
        for(int i = 0; i < n; i++){
            c[i] = sc.nextInt();
        }
        int min = a[0];
        int max = a[0];
        for(int i = 0; i < n; i++){
            if(a[i] > max){
                max = a[i];
            }
            else{
                min = a[i];
            }
        }
        System.out.println(min + " " + max);
        
        for(int i = 1; i <= n; i++){
            System.out.print(a[i] + " ");
        }

        //for - each
        for(int x : a){
            System.out.println(x + " ");
        }

        //Mảng đánh dấu
        //Đếm xem có bao nhiêu phần tử khác nhau trong mảng
        // 0 <= a[i] < 1000000
        int[] e = {1, 2, 3, 4, 5, 6};
        int[] mark = new int[1000001];

        for(int i = 0; i < n; i++){
            e[i] = sc.nextInt();
        }
        
        int lmao = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++){
            mark[e[i]] = 1;
            if(e[i] > lmao) lmao = a[i];
        }

        int cnt = 0;
        for(int i = 0; i <= lmao; i++){
            if(mark[i] == 1){
                cnt++;
            }
        }

        System.out.println(cnt);


        sc.close();
    }
}
