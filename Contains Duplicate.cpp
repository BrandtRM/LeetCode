class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> contains = {};
        
        for(int i = 0; i < nums.size(); i++){
            contains.insert(nums[i]);
        }
        
        if(contains.size() == nums.size()){
            return false;
        }
        else{
            return true;
        }
    }
};