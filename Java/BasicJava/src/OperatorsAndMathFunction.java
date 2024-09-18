public class OperatorsAndMathFunction{
    public static void main(String[] args) {
        //Mathmematics operators
        int a = 1000, b = 300;
        int sum = a + b;
        int hieu = a - b;
        int tich = a * b;
        float thuong = (float)a/b;
        int du = a % b;
        
        System.out.println("sum = " + sum);
        System.out.println("hieu = " + hieu);
        System.out.println("tich = " + tich);
        System.out.printf("thuong = %.2f\n", thuong);
        System.out.println("du = " + du);
        
        
        //Comparison operators
        System.out.println("---");
        System.out.println(10 < 5);
        System.out.println(10 > 5);
        System.out.println(2 <= 3);
        System.out.println(2 >= 3);
        System.out.println(2 <= 2);
        System.out.println(2 != 3);
        System.out.println(2 == 3);

        //Logical operators
        System.out.println("---");
        int x = 3, y = 2;
        System.out.println((x >= 2) && (y <= 3));
        System.out.println((x <= 2) || (y >= 3));
        System.out.println(!(10 < 20));

        //Increment/Decrement operators
        System.out.println("---");
        int n = 3;
        System.out.println(n++);
        System.out.println(n);
        System.out.println(++n);
        
        System.out.println(n--);
        System.out.println(n);
        System.out.println(--n);

        int l = 50;
        int m = l++;
        int t = ++l;
        
        System.out.println(l);
        System.out.println(++m);
        System.out.println(t++);


        //Some math functions
        System.out.println("---");
        System.out.println("Trị tuyệt đối: " + Math.abs(-190));
        System.out.println("Min: " + Math.min(10,30));
        System.out.println("Max: " + Math.max(300, 12));
        System.out.println("Mũ 2: " + Math.pow(2, 10));
        System.out.println("Căn bậc 2: " + Math.sqrt(80));
        System.out.println("Căn bậc 3: " + Math.cbrt(27));
        System.out.println("Làm tròn lên: " + Math.ceil(34.55));
        System.out.println("Làm tròn xuống: " + Math.floor(34.55));
        System.out.println("Làm tròn toán học: " + Math.round(3.55));

        //Toán tử 3 ngôi
    }
}
