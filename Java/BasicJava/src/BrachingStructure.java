import java.util.Scanner;

public class BrachingStructure {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        //Đề bài: Nhập 1 số nguyên, nếu input > 5: in ra Yes, nếu không thì in ra NO
        //Braching structure: cấu trúc rẽ nhánh
        if(n > 5){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }

        /*
         * if(condition_1){
         *      code
         * }
         * else if(conditiona_2){
         *      code
         * }
         * ...
         * else if(condition_n){
         *      code
         * }
         * else{
         *      code
         * }
         * 
         */


        //if_else statement
        //Kiểm tra số chẵn lẻ
        if(n % 2 == 0){
            System.out.println("Even number");
        }
        else if(n % 2 != 0){
            System.out.println("Odd number");
        }
        else{
            System.out.println("Wrong input");
        }

        //swith_case statement
        //Kiểm tra tháng
        System.out.println("---");
        System.out.print("Enter a number: ");
        int a = sc.nextInt();
        switch(a){
            case(1):
                System.out.println("January");
                break;
            case(2):
                System.out.println("February");
                break;
            case(3):
                System.out.println("March");
                break;
            case(4):
                System.out.println("April");
                break;
            case(5):
                System.out.println("May");
                break;
            case(6):
                System.out.println("June");
                break;
            case(7):
                System.out.println("July");
                break;
            case(8):
                System.out.println("August");
                break;
            case(9):
                System.out.println("September");
                break;
            case(10):
                System.out.println("October");
                break;
            case(11):
                System.out.println("November");
                break;
            case(12):
                System.out.println("December");
                break;
            default:
                System.out.println("Wrong input");
        }
        
        //Kiểm tra số ngày của tháng
        System.out.println("---");
        System.out.print("Enter a number: ");
        int b = sc.nextInt();

        switch(b){
            case 1: case 5: case 7: case 8: case 10: case 12:
                System.out.println("31 days");
                break;
            case 4: case 6: case 9: case 11:
                System.out.println("30 days");
                break;
            case 2:
                System.out.println("29 days");
                break;
            default:
                System.out.println("Wrong input");
        }


        //ASCII code
        //A -> Z: 65 -> 90
        //a -> z: 97 -> 122
        //0 -> 9: 48 -> 57
        System.out.println("---");
        char c1 = 'A';
        System.out.println(c1);
        System.out.println((int)c1);
        
        System.out.print("Enter a character: ");
        char c2 = sc.next().charAt(0);
        if(Character.isUpperCase(c2)){
            System.out.println(Character.toLowerCase(c2));
        }
        else if(Character.isDigit(c2)){
            System.out.println(c2);
        }
        else if(Character.isLowerCase(c2)){
            System.out.println(Character.toUpperCase(c2));
        }
        sc.close();
    }
}
