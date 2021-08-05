#!usr/bin/java
public class Sayali_tawade{

    public static void getDistance(String x, String y){

        int hamming_distance =0;

        if(x.length()!=y.length()){
          
            return;
        }

        for (int i = 0; i <x.length() ; i++) {
            if(x.charAt(i)!=y.charAt(i))
                hamming_distance++;
        }

        System.out.println("x="+x+", y="+y+"  Hamming distance: " + hamming_distance);

    }
public static void main(String[] args) {   
     System.out.println("Name: Sayali Jayendra Tawade");
     System.out.println("Email id: tawadesayali4848@gmail.com");    
     System.out.println("Slack username: @Sayali");     
     System.out.println("Biostack:Data science, Genomics");   
     System.out.println("Twitter handle:@tawade_sayali");  
    
        String x = "Sayali";
        String y = "tawade_sayali";
        getDistance(x, y);
}
}
