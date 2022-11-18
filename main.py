import tkinter as tk 
import util

loc_lis = []
bhk = ''
sqft_val=''
loc =''
bath =''

predict_val =''

loc_lis = util.get_location_names()

root = tk.Tk()
root.title("House Price Prediction!")
root.geometry("800x400")
root.configure(bg='#e8c286')

    

def set_var():
    try:
        loc= clicked.get()
        bhk = bhk_ip.get()
        sqft_val = sqrft.get()
        bath = bath_ip.get()
        predict_val = util.find_price(bhk, sqft_val, loc, bath)
        myLable= tk.Label(root,text=f'Predicted House price:  Rs.{int(predict_val*100000)} approx.',bg="#e8c286")
        myLable.pack()
        myLable.config(font=('Helvetica bold', 26))
    except:
        bhk_lable = tk.Label(root,text='Enter correct value or Error in the system.',bg="#e8c286")
        bhk_lable.pack(padx=5,pady=5)
        myLable.config(font=(26))
    
    

    

clicked = tk.StringVar()

bhk_lable = tk.Label(root,text='Select area name :',bg="#e8c286")
bhk_lable.pack(padx=5,pady=5)
drop = tk.OptionMenu(root, clicked, *loc_lis)
drop.pack(padx=10,pady=10)
drop.config( bg="#e8c286")

bhk_lable = tk.Label(root,text='Enter BHK of the house (Ex: 2 ,3 ,4...) :',bg="#e8c286")
bhk_lable.pack(padx=5,pady=5)
bhk_ip = tk.Entry(root,width=100,bg='orange')
bhk_ip.pack(padx=10,pady=10)


sqrtft_lable = tk.Label(root,text='Enter Square Feet of the house (Ex: 1000 ,1300 4000...) :',bg="#e8c286")
sqrtft_lable.pack(padx=5,pady=5)
sqrft = tk.Entry(root,width=100,bg='orange')
sqrft.pack(padx=10,pady=10)


bath_lable = tk.Label(root,text='Enter number of bathrooms (Ex: 2 ,3 ,4...) :',bg="#e8c286")
bath_lable.pack(padx=5,pady=5)
bath_ip = tk.Entry(root,width=100,bg='orange')
bath_ip.pack(padx=10,pady=10)



myButton = tk.Button(root,text='Predict',command=set_var,bg="orange").pack()




root.mainloop()

