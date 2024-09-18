public class DataType {
    public static void main(String[] args) {
        //In dữ liệu ra màn hình
        System.out.println("Buoi 1 java");
        System.out.println("Java huong doi tuong");
        
        //data type
        System.out.println("---");
        
        int a = 0; //byte: 4byte = 32bit, value: -2^31 -> 2^31 - 1 (-2.10^9 -> 2.10^9)
        long b = 1912839719817L; //byte: 8 byte = 64 bit, value: -2^63 -> 2^63 - 1 (-9.10^8 -> 9.10^8)
        float c = 3.124125f; //byte: 4byte, value: lưu đc 7 số đằng sau dấu ,
        double d = 3.1251256125125d; //byte: 8byte, value: lưu đc 15 số đằng sau dấu ,
        char e = '#'; //byte: 2byte
        boolean check = true; //byte: 1byte
        
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(check);

        //Xử lý số thập phân
        System.out.println("\nXử lý số thập phân"); 
        System.out.printf("%.2f\n", c);        
        System.out.printf("%.4f\n", d);        

        //In các biến trên cùng 1 dòng
        System.out.println("\nIn các biến trên cùng 1 dòng");
        System.out.println(a + " " + b + " " + c);

        //Naming convention: Camel case là bắt buộc
        System.out.println("---");
        int dienTich = 3;
        long thuNhap = 40000000000L;
        
        System.out.print(dienTich + "\n");
        System.out.print(thuNhap);

        
    }
}
