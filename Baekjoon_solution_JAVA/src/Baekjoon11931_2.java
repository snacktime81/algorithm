import java.util.Scanner;

public class Baekjoon11931_2 {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] data = new int[n];
        for(int i = 0; i < n; i++){
            data[i] = scanner.nextInt();
        }
        mergeSort(data, 0 , n-1);
        for(int k : data){
            System.out.println(k);
        }
    }

    public static void mergeSort(int[] data, int bottom, int top) {
        int markBottom = bottom;
        int markTop = top;
        int index = bottom;
        int markMiddle = (bottom + top) / 2;
        if (top <= 0) {
            return;
        } else {
            int[] leftData = new int[markMiddle+1];
            for(int i = bottom; i < markMiddle+1; i++){
                leftData[i] = data[i];
                //System.out.println(leftData[i]);
            }
            int[] rightData = new int[data.length - (markMiddle + 1)];
            for(int i = markMiddle + 1, j = 0; i < top + 1 && j < rightData.length ; i++, j++) {
                rightData[j] = data[i];
                //System.out.println(rightData[j]);
            }
            mergeSort(leftData, 0, leftData.length - 1 );
            mergeSort(rightData, 0, rightData.length - 1);

            int i = 0;
            int j = 0;
            int tmp[] = new int[top+1];
            while(i < leftData.length && j < rightData.length){
                if(leftData[i] >= rightData[j]){
                    data[index] = leftData[i];
                    index += 1;
                    i += 1;
                }else{
                    data[index] = rightData[j];
                    index += 1;
                    j += 1;
                }
            }
            while(i < leftData.length){
                data[index] = leftData[i];
                index += 1;
                i += 1;
            }
            while(j < rightData.length){
                data[index] = rightData[j];
                index += 1;
                j += 1;
            }
        }
    }
}
