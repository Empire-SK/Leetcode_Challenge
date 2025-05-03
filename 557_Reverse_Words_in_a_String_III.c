char* reverseWords(char* s) {
    int length = strlen(s);
    int start = 0;
    
    // Process each character in the string
    for (int i = 0; i <= length; i++) {
        // When we encounter a space or the end of the string
        if (s[i] == ' ' || s[i] == '\0') {
            // Reverse the current word (from start to i-1)
            int left = start;
            int right = i - 1;
            
            while (left < right) {
                // Swap characters
                char temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                
                left++;
                right--;
            }
            
            // Move to the next word
            start = i + 1;
        }
    }
    
    return s;
}