/**
 * 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
 * 输入：nums = [4,3,2,7,8,2,3,1]
 * 输出：[5,6]
 */

function findDisappearedNumbers(nums: number[]): number[] {
    // const set = new Set(nums);
    // const newArray = Array.from(set)
    // newArray.sort((a, b) => a - b);
    const arrayLenth = nums.length;

    let total: number[] = []

    nums.forEach((item, index) => {
        total.push(index + 1)
    })
    console.log(total);
    return nums
};

findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
