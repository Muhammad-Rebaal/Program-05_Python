# Define class MyFirstClass
class MyFirstClass:
    print("Who wrote this?")

    # Define string variable called index
    index= "Author-Book"
    # Define function hand_list()
    def hand_list(self,philosopher,book):
        print(philosopher+" wrote the book: "+book)
        print(MyFirstClass.index)
          
    
        # variable + “ wrote the book: ” + variable
    

# Call function handlist()
whodunnit= MyFirstClass()
whodunnit.hand_list("Sun Tzu","The Art of War") 
