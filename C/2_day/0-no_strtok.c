#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char **split_string(char *string, int *word_count) {
    char **words = NULL;
    char *word;
    int i = 0;

    word = strtok(string, " \t\n");
    while (word != NULL) {
        words = realloc(words, (i + 1) * sizeof(char *));
        words[i] = word;
        i++;
        word = strtok(NULL, " \t\n");
    }

    *word_count = i;
    return words;
}

int main() {
    char string[] = "This is a test string.";
    int word_count;
    char **words = split_string(string, &word_count);

    printf("Word count: %d\n", word_count);
    for (int i = 0; i < word_count; i++) {
        printf("Word %d: %s\n", i, words[i]);
    }

    free(words);
    return 0;
}
