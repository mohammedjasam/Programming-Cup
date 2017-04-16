def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    a=((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + numerals[num % b])
    print(a)
    return a

n = int(input())
print(baseN(n,4))



# def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
#     try:
#         a=((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
#         return a
#     except:
#         return
#
# n=int(input())
#
# ans=0
# for i in range(1,999999999999999999999999999999999999999):
#     a=baseN(n,i)
#     # print(a)
#     if a==None:
#         pass
#     else:
#         try:
#             if int(a[-1])==3:
#                 ans=i
#                 break
#         except:
#             pass
# print(ans)
# # 2147483648
# #
# # m=int(input())
# # def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
# #     try:
# #         a=((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
# #         return a
# #
# #     except:
# #         return
# #
# # print(baseN(n,m))
