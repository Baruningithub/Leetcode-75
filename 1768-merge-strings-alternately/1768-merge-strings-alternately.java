class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder s=new StringBuilder("");
        int i=0;
        int a=word1.length();
        int b=word2.length();
        while(i<a || i<b){
            if (i<a)
                s.append(word1.charAt(i));
            if(i<b)
                s.append(word2.charAt(i));
            i++;    
        }       
        return s.toString();
    }
}