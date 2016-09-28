int lengthOfLastWord(char* s) {
    if(!s) return 0;
    int len = strlen(s)-1, i = 0;
    while (s[len] == ' ')len--;
    for (; len >= 0 && s[len] != ' ' ; len--) i++;
    return i;
}
