import java.util.Scanner;

public class LyThuyetSo {

    //1
    public static boolean checkSuqareNumber(int n){
        long square = (long)Math.sqrt(n);
        if(square * square == n){
            return true;
        }
        return false;
    }

    //2
    public static long sum(int n){
        long sum = 0;
        for(int i = 1; i <= Math.sqrt(n); i++){
            if(n % i == 0){
                if(i == n/i){
                    sum += i;
                }
                else{
                    sum += i + n/i;
                }
            }
        }
        return sum;
    }

    //3
    public static int count(int n){
        int cnt = 0;
        for(int i = 1; i <= Math.sqrt(n); i++){
            if(n % i == 0){
                if(i == n/i){
                    cnt++;
                }
                else{
                    cnt += 2;
                }
            }
        }
        return cnt;
    }

    //4
    public static boolean primeNumber(int n){
        for(int i = 2; i <= Math.sqrt(n); i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        //1
        System.out.print("Square number: ");
        if(checkSuqareNumber(n)){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }

        //2
        System.out.print("Sum: ");
        System.out.println(sum(n));

        //3
        System.out.print("Count: ");
        System.out.println(count(n));

        //4
        System.out.print("Prime numbers: ");
        for(int i = 2; i <= n; i++){
            if(primeNumber(i)){
                System.out.print(i + " ");
            }
        }
        sc.close();
    }
}
