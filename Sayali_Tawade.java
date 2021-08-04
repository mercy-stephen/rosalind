#!usr/bin/java
public class Sayali {
    public static void main(String[] args) {   
     System.out.println("Name: Sayali Jayendra Tawade");
     System.out.println("Email id: tawadesayali4848@gmail.com");    
     System.out.println("Slack username: @Sayali");     
     System.out.println("Biostack:Data science, Genomics");   
     System.out.println("Twitter handle:@tawade_sayali");  
    }
}
public class HummingDistanceString {

    public static void getDistance(String x, String y){

        int humming_distance =0;

        if(x.length()!=y.length()){
            System.out.println("Both string sizes are different");
            return;
        }

        for (int i = 0; i <x.length() ; i++) {
            if(x.charAt(i)!=y.charAt(i))
                humming_distance++;
        }

        System.out.println("x="+x+", y="+y+"  Hamming distance: " + humming_distance);

    }

    public static void main(String[] args) {
        String x = "Sayali";
        String y = "tawade_sayali";
        getDistance(x, y);
}
