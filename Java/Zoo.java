abstract class Animal {
    String name;
    int age;

    Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    abstract void makeSound();
    abstract void move();

    void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

class Dog extends Animal {

    Dog(String name, int age) {
        super(name, age);
    }

    @Override
    void makeSound() {
        System.out.println("Sound: Barks");
    }

    @Override
    void move() {
        System.out.println("Movement: Runs on four legs");
    }
}

class Bird extends Animal {

    Bird(String name, int age) {
        super(name, age);
    }

    @Override
    void makeSound() {
        System.out.println("Sound: Chirps");
    }

    @Override
    void move() {
        System.out.println("Movement: Flies in the sky");
    }
}

class Fish extends Animal {

    Fish(String name, int age) {
        super(name, age);
    }

    @Override
    void makeSound() {
        System.out.println("Sound: Blubs");
    }

    @Override
    void move() {
        System.out.println("Movement: Swims in water");
    }
}

public class Zoo {
    public static void main(String[] args) {

        Animal[] animals = {
            new Dog("Buddy", 5),
            new Bird("Kiwi", 2),
            new Fish("Goldie", 1)
        };

        for (Animal animal : animals) {
            animal.displayInfo();
            animal.makeSound();
            animal.move();
            System.out.println();
        }
    }
}