#include <stdbool.h>

bool judgeCircle(char* moves) {
    // Initialize position at origin
    int x = 0, y = 0;
    
    // Process each move until we reach the end of string
    for (int i = 0; moves[i] != '\0'; i++) {
        switch (moves[i]) {
            case 'R': x++; break;
            case 'L': x--; break;
            case 'U': y++; break;
            case 'D': y--; break;
        }
    }
    
    // Check if robot returned to origin
    return (x == 0 && y == 0);
}