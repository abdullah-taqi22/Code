import java.util.Scanner;

public class Java {
    public static void main (String[] args) {
        Scanner at = new Scanner(System.in);

        System.out.print("Enter your name:");
        String name = at.nextLine();

        System.out.println("\nHello, " + name + "!");
    }
}