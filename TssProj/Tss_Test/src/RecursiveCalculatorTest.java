import org.junit.Test;
import static org.junit.Assert.*;

public class RecursiveCalculatorTest {

    @Test
    public void testFactorial() {
        assertEquals(120, factorial(5));
    }

    @Test
    public void testFibonacci() {
        assertEquals(13, fibonacci(7));
    }

    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        } else {
            int fib = 1;
            int prevFib = 1;
            for (int i = 2; i < n; i++) {
                int temp = fib;
                fib += prevFib;
                prevFib = temp;
            }
            return fib;
        }
    }

    @Test
    public void testAddition() {
        assertEquals(8, add(5, 3));
    }

    @Test
    public void testSubtraction() {
        assertEquals(6, subtract(10, 4));
    }

    @Test
    public void testMultiplication() {
        assertEquals(14, multiply(7, 2));
    }

    @Test
    public void testDivision() {
        assertEquals(4, divide(20, 5));
    }

    @Test
    public void testDivideByZero() {
        assertEquals(0, divide(10, 0));
    }

    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static int divide(int a, int b) {
        return a / b;
    }

    public static void main(String[] args) {
        System.out.println("Factorial of 5: " + factorial(5));
        System.out.println("7th Fibonacci number: " + fibonacci(7));

    }
}
