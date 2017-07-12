import csv
Fn=["Name","Quantity","Cost"]
class shop:
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
