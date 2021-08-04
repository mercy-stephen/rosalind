#!usr/bin/java

public class Sanjana_Stage1 {       
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
    System.out.println("Name: Sanjana Joshi");
    System.out.println("Email id: sanjanajo868@gmailcom");    
    System.out.println("Slack username: @Sanjana1404");     
    System.out.println("Biostack: Genomics");  
    String str1 = "Sanjana1404";
    String str2 = "Sanjana1404";
 
    System.out.println("Hamming distance: "+ hammingDist (str1, str2));
}
}    
        
