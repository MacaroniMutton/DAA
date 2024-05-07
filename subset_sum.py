def subset_sum_recursive(nums, k, index, current_sum, subset, all_subsets):
    if current_sum == k:
        all_subsets.append(subset[:])
        return
    
    if current_sum > k or index == len(nums):
        return
        
    
    subset.append(nums[index])
    subset_sum_recursive(nums, k, index + 1, current_sum + nums[index], subset, all_subsets)
    
    subset.pop()
    subset_sum_recursive(nums, k, index + 1, current_sum, subset, all_subsets)

def subset_sum(nums, k):
    all_subsets = []
    subset_sum_recursive(nums, k, 0, 0, [], all_subsets)
    return all_subsets

def main():
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    k = 150
    subsets = subset_sum(nums, k)
    for subset in subsets:
        print(subset)

if __name__=='__main__':
    main()