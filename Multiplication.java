
import javax.swing.plaf.multi.MultiButtonUI;


public class Multiplication extends Calculator{
    public Multiplication () {
        operator = '/';
    }
    public double compute(double A, double B){
        operator = '*';
        return A * B;
    }
}