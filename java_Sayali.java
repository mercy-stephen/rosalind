
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
     System.out.println("Name:Sayali Jayendra Tawade");
     System.out.println("Email:tawadesayali4848@gmail.com");    
     System.out.println("Slack_username:@tawadesayali11");        
     System.out.println("<Twitter_handle>:@tawadesayali11");  
     System.out.println("Biostack:Data science & Genomics");
    
        String x = "tawadesayali11";
        String y = "tawadesayali11";
        System.out.println("<Hamming_Distance>:" + getDistance(x,y));
}
}
