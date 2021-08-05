//#!/user/bin/c

#include <stdio.h>
#include <string.h>
int main() {
            int i, length, count = 0;
            printf("\n Name : Vanshika Agarwal ") ;
            printf("\n Email : vanshika.agarwal98@gmail.com ");  
            printf("\n slack Username : @Vanshika_16") ;
            printf("\n Biostack : Data Science,Vaccine Informatics, Genomics") ;
            printf("\n Twitter : @Vanshika165 ") ;
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
            printf("\nHamming Distance : %d", count);
            return 0;
}
