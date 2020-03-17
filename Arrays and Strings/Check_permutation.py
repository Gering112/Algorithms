# check the permutation given two strings, write a method to decide if one is
# permutation of the other


def check_permutation(str1, str2):
     arr_str1 = []
     arr_str2 = []
               
     for i in str1:
          arr_str1.append(i)
          arr_str1.sort()

     for b in str2:
          arr_str2.append(b)
          arr_str2.sort()


     if len(str1) != len(str2):
          print("Not a permutation")

     elif arr_str1 == arr_str2:
          print("permutation")
     else:
          print("not permutation")

s = check_permutation("dgo","godd")

