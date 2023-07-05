import joblib

model = joblib.load("Predict_Profit.model")

r_d_spend = int(input("Enter R&D spend: "))
admin = int(input("Enter Administration: "))
marketing_spend = int(input("Enter marketing_spend: "))
print("Select State\n")
print("1.Florida\n")
print("2.New York\n")
print("3.California\n")
choice=int(input("Enter your choice: "))
florida=0
new_york=0
if(choice == 1):
    florida=1
elif(choice==2):
    new_york=1

profit=model.predict([[r_d_spend,admin,marketing_spend,florida,new_york]])

print("Predicted Profit is: ",profit[0])
