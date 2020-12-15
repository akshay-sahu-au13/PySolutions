## https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		phonemap={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

		if digits == "":
			return []

		result = list(phonemap[digits[0]])
		digits = digits[1:]
		temp = []

		while digits:
			tillnow = []

			for i in phonemap[digits[0]]:
				for j in result:
					temp.append(j + i)
				tillnow += temp
				temp=[] 

			digits = digits[1:]
			result = tillnow

		return result