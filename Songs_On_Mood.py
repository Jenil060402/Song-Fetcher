
import sqlite3
from tkinter import *
import tkinter as tk
# import requests

root = tk.Tk()
root.title("SONG RECOMMENDER")
root.geometry('400x300')
   
    
def search():
    details.delete("1.0","end")
    mood = user.get()
    conn = sqlite3.connect('Songs.db')

    c = conn.cursor()
    c.execute("SELECT * FROM songs where mood_of_song is " + "'"  + mood + "'" )
    # c.execute("SELECT * FROM songs where song_name is " + "'"  + mood + "'" )
    details.insert(1.0, f"song: {c.fetchall()} ")
    # print(c.fetchall())
    
    # def __init__( self ):
    #     tk.Frame.__init__(self)
    #     self.pack()
    #     self.master.title("Song")
    #     self.button1 = Button( self, text = f"{c.fetchall}", width = 25,
    #                            command = self.new_window )
    #     self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    # # def new_window(self):
    #     self.newWindow = karl2()
        #url = f"https://www.instagram.com/{u_name}/?__a=1"

    # data = requests.get(url).json()
    # print(data)

    # def pic():
    #         import webbrowser
    #         d = data['graphql']['user']['profile_pic_url']
    #         webbrowser.open(d)

    # if details.get(1.0,END) != "":
    #         details.delete(1.0,END)
    #         details.insert(1.0,f"\t username : {data['graphql']['user']['username']} \n     followers : {data['graphql']['user']['edge_followed_by']['count']}      following : {data['graphql']['user']['edge_follow']['count']} \n   full name : {data['graphql']['user']['full_name']} \n Total post : {data['graphql']['user']['edge_owner_to_timeline_media']['count']}  category : {data['graphql']['user']['category_enum']} \n        Email : {data['graphql']['user']['business_email']} \nbio-link:{data['graphql']['user']['external_url']}private account:{data['graphql']['user']['is_private']} || verified account:{data['graphql']['user']['is_verified']}  bussiness account:{data['graphql']['user']['is_business_account']}  \n \n   see profile picture" )

    #         Button(innerframe1,text="click to see",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=pic).place(x=180,y=145)

# def clearTextInput():
#     details.delete("1.0","end")

# details=tk.Text(root, height=10)
# details.pack()
# btnRead=tk.Button(root, height=1, width=10, text="Clear", 
#                     command=clearTextInput)

# btnRead.pack()
frame = Frame(root, width=400, height=300,
              relief=RIDGE, borderwidth=5, bg='#248aa2')
frame.place(x=0, y=0)

innerframe = LabelFrame(frame, width=380, height=50, relief=RIDGE, borderwidth=3,
                        bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5, y=5)


user = Entry(frame, width=30, relief=RIDGE, borderwidth=3)
user.place(x=70, y=15)

search = Button(frame, text="Search", relief=RAISED, borderwidth=2, font=(
    'verdana', 8, 'bold'), bg='#248aa2', fg="white", command=search)
search.place(x=270, y=15)


innerframe = LabelFrame(frame, width=380, height=240, relief=RIDGE, borderwidth=3,
                        bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5, y=45)


innerframe1 = LabelFrame(innerframe, text="Songs List", width=370, height=230, highlightbackground="white",
                         highlightcolor="white", highlightthickness=5, font=('verdana', 10, 'bold'))
innerframe1.place(x=0, y=0)


details = Text(innerframe1, height=12, width=47, relief=RIDGE, borderwidth=5,
               highlightbackground="white", highlightcolor="white", font=('courier', 9, ''))
details.place(x=5, y=5)


root.mainloop()
