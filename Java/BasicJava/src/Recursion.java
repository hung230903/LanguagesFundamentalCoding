public class Recursion {

    //giai thừa
    public static int gt(int n){
        if(n == 0){
            return 1;
        }
        else{
            return n * gt(n - 1);
        }
    }

    //tổng
    public static int sum(int n){
        if(n == 0){
            return 0;
        }
        else{
            return n + sum(n - 1);
        }
    }
    public static void main(String[] args) {

        System.out.println(sum(4));
        System.out.println(gt(4));

    }
}
