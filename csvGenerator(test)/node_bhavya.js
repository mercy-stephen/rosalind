// HACKBIO 2021
// stage 0: Bhavya's Code

console.log("Name:Bhavya Saini");
console.log("Email:bhavyasaini804@gmail.com");
console.log("Slack:Bhavyasind");
console.log("Twitter:@bhavyeah13");
console.log("Biostack:Transcriptomics & Data Science & Vaccine Informatics");

const str1 = 'Bhavyasind';
const str2 = 'bhavyeah13';
const findHammingDistance = (str1 = '', str2 = '') => {
   let distance = 0;
   if(str1.length === str2.length) {
      for (let i = 0; i < str1.length; i++) {
         if (str1[i].toLowerCase() != str2[i].toLowerCase()){
            distance++
         }
      }
      return distance
   };
   return 0;
};
console.log("H_distance:", findHammingDistance(str1, str2));
