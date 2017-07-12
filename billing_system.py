import csv
Fn=["Name","Quantity","Cost"]
class Shop:
    name=""
    qty=0
    cost=0.0
    def add_product(self,name,qty,cost):
        with open("products.csv",'a') as csvf:
         writer=csv.DictWriter(csvf,fieldnames=Fn)
         writer.writerow({"Name":name,"Quantity":qty,"Cost":cost})
        print("Product added successfully :D")
        csvf.close
    def display_product(self):
        with open("products.csv", 'r') as csvf:
            reader=csv.DictReader(csvf,fieldnames=Fn)
            for row in reader :
                print(row)
        csvf.close
    def search_product(self,name1):
        flag=0
        with open("products.csv",'r')as csvf:
            reader=csv.DictReader(csvf,fieldnames=Fn)
            for row in reader:
                if row["Name"] is name1:
                    flag=1
                    break
            if flag==1:
                print (name1 + " Has been found")
                return row
            else :
                print (name1 + " Not found\npress 1.To add the product\t2.To search a different product\nEnter your choice: ")
                choice=input()
                if choice is 1:
                    qty1=input("Enter the quantity of {} to be added".format(name1))
                    cost1=input("Enter the cost of {} to be added".format(name1))
                    self.add_product(name1,qty1,cost1)
                    return row
                elif choice is 2:
                    name1=input("Enter a product to search:")
                    self.search_product(name1)
                else :return None
    def billin(self):
        total=0.0
        option='C'
        while option is not "Q":
            self.display_product()
            name=input("Enter the product's name")
            row=self.search_product(name)
            if row is not None:
                total=total + row["Cost"]
                row["Quantity"]=row["Quantity"]-1
            print("product doesn't exist")
            option=input("\npress C to continue Q to quit")
        print("\nAmount to be payed :Rs."+total)
