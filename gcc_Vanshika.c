

#include <stdio.h>
#include <string.h>
int main() {
            int i, length, count = 0;
            printf("\nName:Vanshika Agarwal") ;
            printf("\nEmail:vanshika.agarwal98@gmail.com");  
            printf("\n<Slack_Username>:@Vanshika_16") ;
            printf("\n<Twitter_handle>:@Vanshika165") ;
            printf("\nBiostack:Data Science & Vaccine Informatics") ;
            char S1[] = "Vanshika_16" ;
            char S2[]="Vanshika165" ;
            length = strlen(S2);
            for(i = 0; i < length; i++)
            {
              if(S1[i] != S2[i])
               {
                 count++;
               }
            }
            printf("\n<Hamming_Distance>:%d", count);
            return 0;
}
