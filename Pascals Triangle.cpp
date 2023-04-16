class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> sol;

        vector<int> a(1, 1);
        sol.push_back(a);
        if(numRows == 1) return sol;

        vector<int> b(2, 1);
        sol.push_back(b);
        if(numRows == 2) return sol;

        for(int i = 3; i <= numRows; i++){
            vector<int> row;
            row.push_back(1);

            for(int j = 0; j < i - 2; j++){
                row.push_back(sol[i - 2][j] + sol[i - 2][j + 1]);
            }

            row.push_back(1);
            
            sol.push_back(row);
        }
        return sol;
    }
};
