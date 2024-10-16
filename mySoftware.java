public class mySoftware {
    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Usage: java mySoftware <operator> <A> <B>");
            return;
        }

        String operator = args[0];
        double A = 0;
        double B = 0;

        try{
         A = Double.parseDouble(args[1]);
         B = Double.parseDouble(args[2]);
        }
        catch (NumberFormatException e){
            System.out.println("Please enter a valid number.");
        }

         Calculator calculator = null;
        
          switch (operator) {
            case "+":
                calculator = new Addition();
                break;
            case "-":
                calculator = new Substraction();
                break;
            case "*":
                calculator = new Multiplication();
                break;
            case "/":
                calculator = new Division();
                break;
            default:
                System.out.println("Invalid operator. Use only +, -, *, or /.");
                return;
        }
         try {
            double result = calculator.compute(A, B);
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
    }
}       
