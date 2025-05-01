int maxDepth(char* s) {
    int depth=0,max=0;
    for(int i=0;i<strlen(s);i++)
    {
        if(s[i]=='(')
        {
            depth++;
            if(depth>max)
            {
                max=depth;
            }
        } else if(s[i]==')')
        {
            depth--;
        }
    }
    return max;
}