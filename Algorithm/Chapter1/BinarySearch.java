package Algorithm.Chapter1;

public class BinarySearch {
    // a must be sorted in ascending order
    public static int search(int key, int[] a) {
        int lo = 0;
        int hi = a.length - 1;
        
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            
            if (key < a[mid])
                hi = mid - 1;
            else if (key > a[mid])
                lo = mid + 1;
            else
                return mid;
        }

        return - 1;
    }
}
