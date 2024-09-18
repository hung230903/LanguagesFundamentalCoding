public class ForLoop {
    public static void main(String[] args){
        for(int i = 1; i <= 3 ; i++){
            System.out.println(i);
        }

        System.out.println("---");
        for(int i = 1; i == 3 ; i++){
            System.out.println(i);
        }
        System.out.println("lmao");

        //Tính tổng từ 1 đến n
        System.out.println("---");
        int n = 9;
        long sum = 0;
        for(int i = 0; i <= n; i++){
            sum += n;
        }
        System.out.println(sum);
        
        //Nested loop
        System.out.println("---");
        for(int i = 1; i <= 3; i++){
            System.out.println(i);
            for(int j = 1; j <= 2; j++){
                System.out.println(j);
            }
            System.out.println("lmao");
        }

        //break-continue
        System.out.println("---");
        for(int i = 0; i <= 9; i++){
            if(i == 5){
                break;
            }
            System.out.println(i);
        }
        
        //
        System.out.println("---");
        outer: for(int i = 0; i <= 3; i++){
            for(int j = 0; j <= 2; j++){
                if(i == 1){
                    break outer;
                }
                System.out.println(j);
            }
            System.out.println(i);
        }

        //
        System.out.println("---");
        for(int i = 1; i <= 5; i++){
            if(i == 3){
                continue;
            }
            System.out.println(i);

        }


    }
}
