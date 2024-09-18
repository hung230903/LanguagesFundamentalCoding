import java.util.Scanner;

public class WhileLoop {
    public static void main(String[] args) {
        int i = 1;
        while(i < 4){
            System.out.println(i);
            i++;
        }

        //Đếm số chữ số
        System.out.println("---");
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int cnt = 0;
        
        if(n == 0){
            cnt = 1;
        }

        while(n != 0){
            cnt++;
            n /= 10;
        }

        System.out.println(cnt);
        sc.close();
    }
}
