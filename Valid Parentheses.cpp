class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{'){
                stack.push(s[i]);
            }
            else if(s[i] == ')' || s[i] == ']' || s[i] == '}'){
                if(stack.empty()){
                    return false;
                }
                else{
                    char x = stack.top();
                    if(x == '(' && s[i] == ')' || x == '[' && s[i] == ']' || x == '{' && s[i] == '}'){
                        stack.pop();
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        if(stack.empty()){
            return true;
        }
        return false;
        
    }
};