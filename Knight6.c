#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 6

// Possible knight moves
int knight_moves[8][2] = {
    {2, 1}, {2, -1}, {-2, 1}, {-2, -1},
    {1, 2}, {1, -2}, {-1, 2}, {-1, -2}
};

// Function to check if a move is within the board boundaries
int is_valid(int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < N);
}

// A struct to represent the state in memoization
typedef struct {
    int x, y, A, B, C;
    int visited[6][6];
} State;

// Hashing function for memoization
int state_hash(State *state) {
    int hash = state->x * 1000 + state->y * 100 + state->A * 10 + state->B * 5 + state->C;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            hash += state->visited[i][j] * (i * N + j);
        }
    }
    return hash;
}

// Function to explore knight moves with memoization
int explore_knight_moves(char board[N][N], int x, int y, int A, int B, int C, int score,
                          int visited[N][N], int path[][2], int path_index, State *memo) {
    State current_state = {x, y, A, B, C, {0}};
    memcpy(current_state.visited, visited, sizeof(current_state.visited));

    // Check if we have already computed this state
    int hash = state_hash(&current_state);
    if (memo[hash].x != -1) {
        return memo[hash].x;
    }

    // Base case: if we reached the target
    if (x == 5 && y == 5) {  // Reached f6
        if (score == 2024) {
            // Print the path and values of A, B, C
            printf("Found path with values A = %d, B = %d, C = %d\n", A, B, C);
            printf("Path: ");
            for (int i = 0; i < path_index; i++) {
                printf("(%d, %d) ", path[i][0], path[i][1]);
            }
            printf("\n");
            return 1;  // Valid path found
        }
    }

    // Store current path
    int found_path = 0;

    // Explore all knight moves
    for (int i = 0; i < 8; i++) {
        int nx = x + knight_moves[i][0];
        int ny = y + knight_moves[i][1];
        if (is_valid(nx, ny) && visited[nx][ny] == 0) {
            visited[nx][ny] = 1;  // Mark as visited

            // Update the score based on the current square
            int current_value = board[nx][ny];
            int new_score = score;

            if (current_value != board[x][y]) {  // Different integers
                if (current_value == 'A') {
                    new_score *= A;
                } else if (current_value == 'B') {
                    new_score *= B;
                } else if (current_value == 'C') {
                    new_score *= C;
                }
            } else {  // Same integer
                if (current_value == 'A') {
                    new_score += A;
                } else if (current_value == 'B') {
                    new_score += B;
                } else if (current_value == 'C') {
                    new_score += C;  // Fixed the increment for 'C'
                }
            }

            // Store the current path
            path[path_index][0] = nx;
            path[path_index][1] = ny;

            // Recursive call
            found_path = explore_knight_moves(board, nx, ny, A, B, C, new_score, visited, path, path_index + 1, memo);
            if (found_path) {
                break;  // Exit early if a valid path is found
            }

            visited[nx][ny] = 0;  // Backtrack
        }
    }

    // Store result in memoization
    memo[hash] = current_state;
    return found_path;
}

// Main function to run the knight move exploration
void knight_trip_search(char board[N][N], int A, int B, int C) {
    State memo[10000];  // Adjust size as necessary
    memset(memo, -1, sizeof(memo));  // Initialize memoization
    int visited[N][N] = {0};
    int path[N * N][2];  // Path storage

    // Starting from a1 (0, 0) and moving to f6 (5, 5)
    visited[0][0] = 1;  // Mark starting position as visited
    if (explore_knight_moves(board, 0, 0, A, B, C, A, visited, path, 0, memo)) {
        printf("Path from a1 to f6 found.\n");
    } else {
        printf("No path found from a1 to f6.\n");
    }

    memset(visited, 0, sizeof(visited));  // Clear visited array
    visited[5][0] = 1;  // Starting from a6 (5, 0)

    // Starting from a6 (5, 0) and moving to f1 (0, 5)
    if (explore_knight_moves(board, 5, 0, A, B, C, A, visited, path, 0, memo)) {
        printf("Path from a6 to f1 found.\n");
    } else {
        printf("No path found from a6 to f1.\n");
    }
}

int main() {
    // Example board representation
    char board[N][N] = {
        {'A', 'B', 'B', 'C', 'C', 'C'},
        {'A', 'B', 'B', 'C', 'C', 'C'},
        {'A', 'A', 'B', 'B', 'C', 'C'},
        {'A', 'A', 'B', 'B', 'C', 'C'},
        {'A', 'A', 'A', 'B', 'B', 'C'},
        {'A', 'A', 'A', 'B', 'B', 'C'}
    };

    // Search for paths with specific values
    int A = 5, B = 7, C = 8;  // Example values
    knight_trip_search(board, A, B, C);

    return 0;
}
