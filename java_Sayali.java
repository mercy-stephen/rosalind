#!usr/bin/java
public class java_Sayali{

    public static int getDistance(String x, String y){

        int hamming_distance =0;

        for (int i = 0; i <x.length() ; i++) {
            if(x.charAt(i)!=y.charAt(i))
                hamming_distance++;
        } 
        return hamming_distance;
    }
public static void main(String[] args) {   
     System.out.println("Name: Sayali Jayendra Tawade");
     System.out.println("Email id: tawadesayali4848@gmail.com");    
     System.out.println("Slack username: @tawadesayali11");     
     System.out.println("Biostack:Data science & Genomics");   
     System.out.println("Twitter handle:@tawadesayali11");  
    
        String x = "tawade_sayali";
        String y = "tawade_sayali";
        System.out.println("Hamming distance: " + getDistance(x,y));
}
}
