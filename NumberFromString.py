import random #so we can use the shuffle function

def main(): 
    string="zerooneonetwofourfivefivefivesixsixeightninenine" #0 1 1 2 4 5 5 5 6 6 8 9 9
    stringList=list(string)
    random.shuffle(stringList)
    string=''.join(stringList)
    print(getNumbers(string)) #display numbers in ascending order
                     

def depopulateDictionary(num,d):
    for letter in num: #iterate thru the string
        d[letter]-=1 #decrement the amount of that letter in the dictionary by 1
        if(d[letter]==0): #if it's been decrememnted to 0...
            del d[letter] #remove it
    return d #return the updated dictionary
def getNumbers(string):
    d={} #initialize our empty dictionary
    numbers=[] #this will hold the numbers we get from the string
    for letter in string: #iterate thru each character in string to populate our dictionary
        if letter in d: #if this letter is already in our dictionary...
            d[letter]+=1 #increase the count of that letter by 1
        else: #if doesn't already exist
            d[letter]=1 #create a new key of that letter with value pairing =1

    #At this point, we have our dictionary which is populated with how many times each letter appears in the string
    while("g" in d): #while the dictionary has g's in it
        d=depopulateDictionary("eight",d)
        numbers.append(8) #add an 8 to numbers array
    while("w" in d):
        #must be a two
        d=depopulateDictionary("two",d)
        numbers.append(2)
    while("x" in d):
        #must be a six
        d=depopulateDictionary("six",d)
        numbers.append(6)
    while("z" in d):
        #must be a zero
        d=depopulateDictionary("zero",d)
        numbers.append(0)
    while("u" in d):
        #must be a four
        d=depopulateDictionary("four",d)
        numbers.append(4)
    while("t" in d):
        #because we have taken care of all eights and twos, any remaining t's must belong to threes
        d=depopulateDictionary("three",d)
        numbers.append(3)
    while("f" in d):
        #using same logic as last loop, must be a five
        d=depopulateDictionary("five",d)
        numbers.append(5)
    while("v" in d):
        #must be a seven
        d=depopulateDictionary("seven",d)
        numbers.append(7)
    while("o" in d):
        d=depopulateDictionary("one",d)
        numbers.append(1)
    while(d): #while dictionary has elements, they must all be nines
        d=depopulateDictionary("nine",d)
        numbers.append(9)
    numbers.sort() #sort array in ascneding order
    return numbers #return numbers list

if __name__=="__main__":
    main() #call main
