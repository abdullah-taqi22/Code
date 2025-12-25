import java.util.Scanner;

public class Assignment1 {
    public static void main(String[] args) {
        Scanner at = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = at.nextLine();

        System.out.print("Enter your age: ");
        int age = at.nextInt();

        System.out.println("\nHello, " + name + "!");
        System.out.println("You will be " + (age + 5) + " years old after 5 years.");
    }
}
