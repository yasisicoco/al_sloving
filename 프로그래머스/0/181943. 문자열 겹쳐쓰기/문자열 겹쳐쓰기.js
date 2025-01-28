function solution(my_string, overwrite_string, s) {
    const before = my_string.substring(0, s);
    const after = my_string.substring(s + overwrite_string.length);
    return before + overwrite_string + after;
}