char* truncateSentence(char* s, int k) {
    int count = 0;
    int i = 0;
    
    // Traverse the string and count spaces (word separators)
    while (s[i] != '\0') {
        if (s[i] == ' ') {
            count++;
            if (count == k) {
                break;
            }
        }
        i++;
    }
    
    // Allocate memory for the truncated sentence
    char* result = (char*)malloc((i + 1) * sizeof(char));
    strncpy(result, s, i);
    result[i] = '\0';  // Null-terminate the new string
    
    return result;
}