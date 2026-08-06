public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> s = new HashSet<int> ();

        foreach (int num in nums){
            if(s.Contains(num)){
                return true;
            }
            s.Add(num);
        }
        return false;
    }
}