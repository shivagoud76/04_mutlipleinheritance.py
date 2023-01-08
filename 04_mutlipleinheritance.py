class Firstparent:
    food="Yes"
    Shopping="Yes"
    work="No"
    
    def bank(self):
        print("Savings amount")

class Secondparent:
    education='Yes'
    movie="No"
    food="No"
    
    def privacy(self):
        print("No Privacy")

class fchild(Firstparent,Secondparent):
# class fchild(Secondparent,Firstparent):
    
    def clothes(self):
        print("Clothes of first child")
    
    def phone(self):
        print("Phone of first child")
        
print("For First child food "+fchild.food)
print("For First child Shopping "+fchild.Shopping)
print("The Work for First Child "+fchild.work)   
fc=fchild()
fc.bank()
fc.clothes()
fc.phone()
print(fc.Shopping)
print("Education of First Child "+fc.education)
print("Watching Movie for the First Child "+fc.movie)
fc.privacy()  