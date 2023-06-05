**sort-sort the list/string in ascending order by default**
sorted(string) sort之后从string变成list了
string_value = 'I like to sort'
sorted_string = sorted(string_value)
answer = [' ', ' ', ' ', 'I', 'e', 'i', 'k', 'l', 'o', 'o', 'r', 's', 't', 't']


sorted(list)
sorted(list,reverse=True) --sorted in descending order

**join-join the list into string** 
join can be used in tuple, list, dict
somesign.join(theLIST)
eg. "#".join(["1","2","3"]) = "#1#2#3"
    "".join(["a","b","c"]) = "abc"

**split-split the string into list**
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
answer = ['hello', 'my name is Peter', 'I am 26 years old']

**list append & hashmap value(list) append**
currencies = ['Dollar', 'Euro', 'Pound']
currencies.append('Yen')
answer = ['Dollar', 'Euro', 'Pound', 'Yen']

# 如果hashmap的value不是【】list,不能做append举动
hashmap[key].append(value) -- {[key]:[value]}

**hashmap.values() and hashmap.key()**
hashmap.values() are treated as list of values
[value1,value2,value3]

if s in hashmap.keys(): is the same as if s in hashmap():

**range(start,stop)**
startpoint is included
Remember, endpoints aren't included!
range(5)           0,1,2,3,4   
range(3,8)         3,4,5,6,7   
range(3,8,2)       3,5,7       --number in between is 2
range(4,-1,-1)     4,3,2,1,0  

**create list and list of list**
len(nums) = 5
#create [[],[],[],[],[]] 5 number of inside list in the list
[[] for _ in range()]

#create [0,0,0,0,0] 5 0 in the list
[0] * len(nums)

**判断只有字母或者只有数字**
isalpha() - only alphabetical characters. 
isnumeric() - only numbers.
isalnum() - only characters or numbers.

string.isalpha() --return True or False

**string related methods**
len(s) -- how long the string is
s.upper() -- make all string lower cased
s.lower() -- make all string upper cased
s.count("t") -- count how many "t" there is
s.find("o") -- find 第几个是"o"
s.replace("to", "three") -- 把to换成three

**set to正无穷或者负无穷**
profit = float('-inf') 负无穷
profit = float('inf') 正无穷

**if statement in one line**
value = <value_if_true> if <expression> else <value_if_false>
age = 8
if age < 5:
    is_baby = True
else:
    is_baby = False
    
# change to:
age = 8
is_baby = True if age < 5 else False