import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class StarInfo {
    public static void main(String[] Args){
        Scanner scanner = new Scanner(System.in);
        boolean itworks = true;
        while (itworks){
        
            try{
            float distance;
            float luminosity;
            float radius;
            float temperature;
            String spectralClass;
        
            System.out.println("What is the Distance of this star from the earth?");
            distance = scanner.nextFloat();
            System.out.println("What is the luminosity of this star?");
            luminosity = scanner.nextFloat();
            System.out.println("What is the radius of this star?");
            radius = scanner.nextFloat();
            System.out.println("What is the temperature of this star?");
            temperature = scanner.nextFloat();
            scanner.nextLine();
            System.out.println("What is the spectral class of this star?");
            spectralClass = scanner.nextLine();
            ArrayList <String> stars = new ArrayList<String>();
            stars.add(spectralClass);
            stars.add(String.valueOf(temperature));
            stars.add(String.valueOf(radius));
            stars.add(String.valueOf(luminosity));
            stars.add(String.valueOf(distance));        
            for (int i = 0; i < stars.size();i++){
                System.out.println(stars.get(i));
            }
        } catch(InputMismatchException  e){
            System.err.println("Please try again");
        }
        
        System.out.println("Would you like to proceed with more stars? 0(No)/1(Yes)");
        int choice = scanner.nextInt();
        if (choice == 1){
            continue;
        } else {
            break;
        }
        }

    }    
}
