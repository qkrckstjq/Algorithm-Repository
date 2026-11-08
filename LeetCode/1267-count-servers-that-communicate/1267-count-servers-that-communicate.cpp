class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        
        int answer = 0;
        for(int i = 0; i < size(grid); i++) {
            int sm = 0;
            vector<int> row = grid[i];
            for(int j = 0; j < size(row); j++) {
                sm += row[j];
            }

            if (sm == 1) {
                int j = 0;
                int temp = 0;
                for(int n = 0; n < row.size(); n++) {
                    if(row[n] == 1) {
                        j = n;
                        break;
                    }
                }
                for(int n = 0; n < grid.size(); n++) {
                    if(grid[n][j] == 1) {
                        temp += 1;
                    }
                }
                if(temp < 2) {
                    answer -= 1;
                }
            }


            answer += sm;
        }

        // cout << answer;

        return answer;
    }
};