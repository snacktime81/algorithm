import java.util.Scanner;

public class Baekjoon11931 {
    public static void mergeSort(int[] data, int bottom, int top){
        if(bottom < top) {
            int middle = (bottom + top) / 2;
            mergeSort(data, bottom, middle);
            mergeSort(data, middle + 1, top);
            merge(data, bottom, middle, top);
        }
    }
    public static void merge(int[] data, int bottom, int middle, int top){
        int markBottom = bottom;
        int index = bottom;
        int markMiddle = middle + 1;
        int tmp[] = new int[data.length];
        while(markBottom <= middle && markMiddle <= top) {
            if (data[markBottom] >= data[markMiddle]) {
                tmp[index] = data[markBottom];
                index += 1;
                markBottom += 1;
            } else {
                tmp[index] = data[markMiddle];
                index += 1;
                markMiddle += 1;
            }
        }
        while(markBottom <= middle){
            tmp[index] = data[markBottom];
            index += 1;
            markBottom += 1;
        }
        while(markMiddle <= top) {
            tmp[index] = data[markMiddle];
            index += 1;
            markMiddle += 1;
        }
        for(int i = bottom; i <= top; i++){
            data[i] = tmp[i];
        }
    }
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] data = new int[n];
        for(int i = 0; i < n; i++){
            int num = scanner.nextInt();
            data[i] = num;
        }
        mergeSort(data, 0, n-1);
        for(int k : data){
            System.out.println(k);
        }
    }
}
