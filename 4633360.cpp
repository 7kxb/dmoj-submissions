#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector <string> adj;
    vector <string> noun;
    for (int _ = 0; _ < n; _++) {
        string temp;
        cin >> temp;
        adj.push_back(temp);
    }
    for (int _ = 0; _ < m; _++) {
        string temp;
        cin >> temp;
        noun.push_back(temp);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << adj[i] << " as " << noun[j] << endl;
        }
    }
}