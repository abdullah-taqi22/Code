import java.util.Scanner;

public class Assignment2 {
    public static void main(String[] args) {
        Scanner at = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = at.nextInt();

        if (num % 2 == 0) {
            System.out.println(num + " is EVEN.");
        } else {
            System.out.println(num + " is ODD.");
        }
    }
}
