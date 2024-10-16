public class Division extends Calculator{
    public Division () {
        operator = '/';
    }
    
    public double compute(double A, double B){
        if (B == 0) {
            System.err.println("Division by zero error");
            return 0;
        }
        return A / B;
    }
}
