class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var numIndices = [Int: Int]() // Dictionary to store number and its index
        
        for (index, num) in nums.enumerated() {
            let complement = target - num
            if let complementIndex = numIndices[complement] {
                return [complementIndex, index] // Found the solution
            }
            numIndices[num] = index // Store the current number with its index
        }
        
        return [] // Default return (should never reach here since the problem guarantees a solution)
    }
}