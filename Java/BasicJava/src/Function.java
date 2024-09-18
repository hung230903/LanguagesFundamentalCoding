import java.util.Scanner;

public class Function {
    //public static return_type function_name
    public static void helloWorld(){
        System.out.println("Hello world!");
    }
    
    //public static void(parameters)
    public static void param(int n, long m, char c){
        System.out.println(n + " " + m + " " + c);
    }

    //
    public static int getValue(int n){
        return n * 100;
    }

    //
    public static int sum(int a, int b, int c){
        int sum = a + b + c;
        return sum;
    }

    //
    public static boolean check_even_number(int n){
        if(n % 2 == 0){
            return true;
        }
        else{
            return false;
        }
    }

    //
    public static long countDigit(long n){
        int cnt = 0;
        if(n == 0){
            return 1;
        }
        while(n != 0){
            cnt++;
            n /= 10;
        }
        return cnt;
    }

    //khi build hàm vs return type là bool thì nên chỉ ra hàm có giá trị sai trước
    public static boolean checkPrime(int a){
        if(a < 2){
            return false;
        }
        for(int i = 0; i <= Math.sqrt(a); i++){
            if(a % i == 0){
                return false;
            }
        }
        return true;
    }

    //main function
    //phải truyền đủ đối số vào trong hàm nếu thừa hoặc thiếu sẽ bị lỗi
    public static void main(String[] args) {
        //function_call(arguments)
        helloWorld();
        
        System.out.println("---");
        param(28, 1000000000, 'a');
        param(100, 500, '#');
        
        System.out.println("---");

        int x = getValue(50);
        System.out.println(x);

        System.out.println("---");
        System.out.println(sum(10, 2, 3));

        System.out.println("---");
        System.out.println(check_even_number(10));
        System.out.println(check_even_number(20));
        System.out.println(check_even_number(13));

        System.out.println("---");
        Scanner sc = new Scanner(System.in);
        System.out.println("Count digit");
        System.out.print("Enter a digit: ");
        long n = sc.nextLong();
        System.out.println(countDigit(n));
        System.out.println("---");
        System.out.println("Print prime numbers");
        System.out.print("Enter a digit: ");
        int a = sc.nextInt();
        for(int i = 1; i <= a; i++){
            if(checkPrime(i)){
                System.out.println(i + " ");
            }
        }

        sc.close();

    }
}
