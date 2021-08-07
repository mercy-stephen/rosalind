
public class java_Sanjana {       
    static int hammingDist(String str1, String str2)
{
    int i = 0, count = 0;
    while (i < str1.length())
    {
        if (str1.charAt(i) != str2.charAt(i))
            count++;
        i++;
    }
    return count;
}
 
public static void main (String[] args)
{
    System.out.println("Name:Sanjana Joshi");
    System.out.println("Email:sanjanajo868@gmailcom");    
    System.out.println("<Slack_username>:@Sanjana1404");  
    System.out.println("<Twitter_handle>:@Sanjana1404"); 
    System.out.println("Biostack:Genomics");     
    
    String str1 = "Sanjana1404";
    String str2 = "Sanjana1404";
 
    System.out.println("<Hamming_Distance>:"+ hammingDist (str1, str2));
}
}    
        
