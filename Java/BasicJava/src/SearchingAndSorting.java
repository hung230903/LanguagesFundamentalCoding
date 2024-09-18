import java.util.Scanner;
import java.util.Arrays;

public class SearchingAndSorting {

    //O(n)
    public static boolean linearSearch(int a[], int n, int x){
        for(int i = 0; i < n; i++){
            if(a[i] == x){
                return true;
            }
        }

        return false;
    }

    //(O(log2n))
    //Điều kiện: Mảng đã đc sort
    public static boolean binarySearch(int a[], int n, int x){
        int left = 0;
        int right = n - 1;
        while(left <= right){
            int mid = (left + right)/2;
            if(a[mid] == x){
                return true;
            }
            else if(a[mid] < x){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        return false;
    }

    //biển thể 1 của binarySearch : Tìm vị trí đầu tiên của 1 phần tử trong mảng
    public static int binarySearchFindFirstPosition1(int a[], int n, int x){
        int res = -1, left = 0, right = n - 1;
        while(left <= right){
            int mid = (right + left) / 2;
            if(a[mid] == x){
                res = mid;
                right = mid - 1;
            }
            else if(a[mid] > x){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }

        return res;
    }

        //biển thể 2 của binarySearch : Tìm vị trí cuối cùng của 1 phần tử trong mảng
        public static int binarySearchFindLastPosition1(int a[], int n, int x){
            int res = -1, left = 0, right = n - 1;
            while(left <= right){
                int mid = (right + left) / 2;
                if(a[mid] == x){
                    res = mid;
                    left = mid + 1;
                }
                else if(a[mid] > x){
                    right = mid - 1;
                }
                else{
                    left = mid + 1;
                }
            }
    
            return res;
        }

        //biển thể 3 của binarySearch : Tìm vị trí đầu tiên >= phần tử x trong mảng
        public static int binarySearchFindFirstPosition2(int a[], int n, int x){
            int res = -1, left = 0, right = n - 1;
            while(left <= right){
                int mid = (right + left) / 2;
                if(a[mid] >= x){
                    res = mid;
                    right = mid - 1;
                }
                else{
                    left = mid + 1;
                }
            }
    
            return res;
        }

        //biển thể 4 của binarySearch : Tìm vị trí cuối cùng <= phần tử x trong mảng
        public static int binarySearchFindLastPosition2(int a[], int n, int x){
            int res = -1, left = 0, right = n - 1;
            while(left <= right){
                int mid = (right + left) / 2;
                if(a[mid] <= x){
                    res = mid;
                    left = mid + 1;
                }
                else{
                    right = mid - 1;
                }
            }
    
            return res;
        }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] a = new int[n];

        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }
        Arrays.sort(a);

        System.out.println(linearSearch(a, n, x));
        System.out.println(binarySearch(a, n, x));
        System.out.println(binarySearchFindFirstPosition1(a, n, x));
        System.out.println(binarySearchFindLastPosition1(a, n, x));
        System.out.println(binarySearchFindFirstPosition2(a, n, x));
        System.out.println(binarySearchFindLastPosition2(a, n, x));
        System.out.println();

        //Số lần xuất hiện của phần tử x
        int last = binarySearchFindLastPosition1(a, n, x);
        int first = binarySearchFindFirstPosition1(a, n, x);
        int res = last - first + 1;
        System.out.println(res);
        System.out.println();

        //
        int[] b = {1, 2, 4, 1, 2, 6, 7, 8 ,9, 2};
        System.out.println(Arrays.binarySearch(b, 1));
        System.out.println(Arrays.binarySearch(b, 12));
        if(Arrays.binarySearch(b, 12) >= 0){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
        

        sc.close();
        
    }
    
}
