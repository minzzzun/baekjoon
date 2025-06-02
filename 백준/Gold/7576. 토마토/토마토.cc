#include <iostream>
using namespace std;

struct tomato{
    int y, x;
};

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int m, n;
int box[1001][1001];

// 큐 최대 크기 (최악의 경우 n*m)
tomato q[1000000];
int front = 0, rear = 0;

bool is_inside(int ny, int nx){
    return (0 <= ny && ny < n && 0 <= nx && nx < m);
}

void bfs(void){
    while(front < rear){
        int y = q[front].y;
        int x = q[front].x;
        front++;

        for(int i=0; i<4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(is_inside(ny, nx) && box[ny][nx] == 0){
                box[ny][nx] = box[y][x] + 1;
                q[rear++] = {ny, nx};
            }
        }
    }
}

int main(){
    cin >> m >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> box[i][j];
            if(box[i][j] == 1) q[rear++] = {i, j};
        }
    }

    bfs();

    int max = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(box[i][j] == 0){
                cout << -1 << "\n";
                return 0;
            }
            if(max < box[i][j]) max = box[i][j];
        }
    }
    cout << max-1 << "\n";
    return 0;
}
