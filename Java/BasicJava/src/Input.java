import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        //Nhập dữ liệu từ bàn phím
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Nhap so int: ");
        int n = sc.nextInt();
        System.out.println(n);
        
        System.out.print("Nhap so long: ");
        long m = sc.nextLong();
        System.out.println(m);
        
        System.out.print("Nhap so thuc float: ");
        float f = sc.nextFloat();
        System.out.println(f);
        
        System.out.print("Nhap so thuc double: ");
        double a = sc.nextFloat();
        System.out.println(a);
        
        System.out.print("Nhap chuoi ki tu: ");
        char c = sc.next().charAt(0);
        System.out.println(c);

        sc.close();
    }
}
