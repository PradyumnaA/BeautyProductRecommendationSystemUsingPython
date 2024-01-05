import pandas as pandaModule
#Read the CSV File
input_file=input("Please enter the file name with .csv extension")
#Defining the dataframe
dataframe=pandaModule.read_csv(input_file,encoding='latin1')#Here I have made encoding as latin to avoid error
#Asking user to enter the category
if input_file=="TestingData.csv":
    user_choice=input("Enter your category like Soap, Oil Hydrator")#Ask users to enter the choices
else:
    user_choice=input("Enter your category like Shampoo, Oil, Conditioner, Hydrator,Eyeshadow,EyeLiner")


available_options=['Shampoo', 'Oil', 'Conditioner', 'Hydrator','Eyeshadow','EyeLiner','Hydrator','Matte']#If user enters the invalid choice show him the available options
filtered_the_dataframe_on_user_choice=dataframe[dataframe["Category"]==user_choice]

if filtered_the_dataframe_on_user_choice.empty:
    print(f"Sorry user it was an invalid category entry '{user_choice}' please enter the choices from {available_options}")#displaying the error message
else:
    valid_choice_file='category.csv'#If the category is valid then generate the category.csv file
    filtered_the_dataframe_on_user_choice.to_csv(valid_choice_file)
    print(f"Filtered data saved to {valid_choice_file} ")
    

