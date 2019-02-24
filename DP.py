import sys


class Solution:
	def numDecodings(self, s):
		memo = {}
		def f(s):
			print ("\nThe input string is:",s)
			if s == "":
				return 1 #if s is a empty string there is only one way to decode it
			elif s[0] == "0":
				return 0 #if s[0] is 0 then the string is invalid, since no letter maps to 0, e.g 01 doesn't make sense
			elif len(s) == 1:
				return 1#if s is 1 long and it is 1-9 there is 1 way to decode it
			elif s in memo:
				return memo[s]# if the number of ways to decode s is in the dictionary we just retreive it and return
			elif int(s[0] + s[1]) > 0 and int(s[0] + s[1]) <= 26:
				#s will be longer than 1 at this case
				#so if  s[0]+s[1] converted to an int is in the range 1 to 26 inclusive this is what we do
				ret =  f(s[1:]) + f(s[2:]) #the number of ways to decode the string 123: decode("123") = decode("23") + decode("3") = 3
				#this is because one way of decoding is picking 1 as a standalone number while the other way is picking 12 as a standalone number and decoding the rest of the string after those two numbers
				# if we got to here the value for s won't be in the dictionary so we put it there for the future and return
				memo[s] = ret
				print ("\nReturn value is: ",ret)
				print ("\nmemo is: ",memo)
				return ret
			else: 
				#if we got here it is exactly like the last case(the one above) except the string is like 323, 32 is not between 1 and 26
				# so the number of ways to decode is just the number of ways you can decode 23
				ret = f(s[1:])
				memo[s] = ret
				print ("\nReturn value is: ",ret)
				print ("\nmemo is: ",memo)
				return ret
		
		return f(s)

	def numDecodings1(self,s):
		memo = {}
		# Without memoization
		if s == "0":
			return 0
		if len(s)==0 or len(s)==1:
			return 1
		if s[0]=="0":
			return 0
		if s in memo:
			return memo[s]
		if int(s[0]+s[1])<=26 and int(s[0]+s[1])>=10:
			ret = self.numDecodings1(s[1:]) + self.numDecodings1(s[2:])
			memo[s] = ret
			return ret
		else:
			ret =  self.numDecodings1(s[1:])
			memo[s] = ret
			return ret

	def minwindowseq(self,S,T):
		self.validstrings = []
		y = self.helper(S,T,self.validstrings,0)
		return y
		#print (self.validstrings)

	def helper(self,S,T,x,start_index):
		print("\nS is: ",S)
		print("\nT is: ",T)
		#sys.exit()
		if len(T)==0 or T=="" or not T:
			print ("\nExit condition hit. The list is:",x)
			#sys.exit()
			#self.validstrings.append(x)
			return x

		if S[start_index:]=="" or len(S[start_index])==0:
			return None
		checklen = len(S)
		
		while start_index < len(S):
			if S[start_index]==T[0]:
				x.append(start_index)
				print(x)
				print(S[start_index+1:])
				print(T[1:])
				if len(x)==2:
					pass
					#sys.exit()
				#sys.exit()
				return (self.helper(S,T[1:],x,start_index+1))
				#self.helper(S,T[:],x,i+1)
				
			else:
				start_index+=1

	def numWays(self,valueList,change,memo):
		if change in valueList:
			return 1
		mincoins = change
		if change in memo:
			return memo[change]
		for i in [c for c in valueList if c <= change]:
			numcoins = 1 + self.numWays(valueList,change-i,memo)
			if numcoins < mincoins:
				memo[change] = numcoins
				mincoins = numcoins

		return mincoins


s = Solution()
print("Answer is:",s.numWays([1,2,10,21],63,{}))