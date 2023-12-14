import tkinter as tk
from tkinter import *
from tkinter.simpledialog import askstring
import random
from PIL import Image, ImageTk
import os

class AlienInvasion():
    def __init__(self,word=None):
        """
        Attributes:
            word: game word, determined randomly from preset words, or determined by input(this waS helpful for testing)
            word_track: 
            guesses: how many guesses the user has left, initally 7, each incorrect guess counts as a guess
            self.length: length of game word or number of letters in word
            player_word: word progress of player, italizes to list of "___" (one for each letter in word) 
        """
        if word!=None:
            self.word=word
        else:
            self.word=AlienInvasion.__gen_word__()
        self.total_guesses=7
        self.guesses=self.total_guesses
        self.word_track=self.__word_track__(self.word)
        self.player_word=["_"]*len(self.word)
        self.length=len(self.word)

    def __gen_word__():
        """This method randomly selects a word from the list words.
        Returns: 
            word:any word is the list words
        """
        words=["HUSKY","PYTHON","CAT","DOG","TEA","ROCK","BINARY","LAMP","APPLE","LAPTOP"]
        index=random.randrange(0,9)
        word=words[index]
        return word
    
    def __word_track__(self,word):
        """This method initalizes the tracking method for the game.
        Arguements: 
            word: string of letters
        Returns:
            word_track: a dictionary with each letter of the alphabet as keys and the number of times each letter 
                occurs in the word as the value associated with the key.
        """
        word_track={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
        for letter in word:
            word_track[letter.upper()]+=1
        return word_track
    
    def __guess_valid__(self, guess):
        """This method checks if a guess is valid, a guess is valid if it has not been already guessed. If valid returns count, if it is not valid return "DNE"
        Arguements:
            guess: a single alphabetical string
        Returns:
            count: number of times that the guess appears in the game word
            "DNE": string "DNE" used to reprea
        """
        try:
            count=self.word_track[guess.upper()]
            self.word_track.pop(guess.upper())
            return count
        except KeyError:
            return "DNE"
        
    def __update_pword__(self,guess):
        """This method updates player word based on a letter guess and returns the updates player word with any occurances of guess added.
        Arguements:
            guess: a single alphabetical string
        Returns:
            None: updates player word
        """
        place=0
        for letter in self.word:
            if guess.upper()==letter.upper():
                self.player_word[place]=letter
            place+=1
        return self.player_word
    
    def __check_win_lose__(self):
        """This method checks if the user has won or lost
        Returns:
            True: returns true if the user has won, player word=game word
            False: returns false if the user lost, guesses=0
            None: returns none if game should coninue, no win or lose
        """
        current_word=""
        for letter in self.player_word:
            current_word+=str(letter)
        if current_word.upper()==self.word.upper():
            return True
        if self.guesses==0:
            return False
    
    def __turn__(self,guess):
        """This method checks if a guess is valid
        Arguements:
            guess: a single alphabetical string
        Returns:
            Self.guesses: if guess is valid but there are no occurances one guess is deducted
            None: if guess is not a valid guess, no updates to self
            count: if guess is valid, updates self.guesses and self.player_word
        """
        count=self.__guess_valid__(guess)
        if count==0:
            self.guesses-=1
        else:
            self.__update_pword__(guess)
            return count


class AlienInvasionHard(AlienInvasion):
    def __init__(self, word=None):
        """This class manages hard mode for alien invasion where you must also guess the location.
        Attributes:
            word: game word, determined randomly from preset words
            guesses: how many guesses the user has left, initally 7, each incorrect guess counts as a guess
            self.length: length of game word or number of letters in word
            player_word: word progress of player, italizes to list of "___" (one for each letter in word) 
            word_track: a list of dictionarys (one for each letter in word). Each dictonary has each letter of the alphabet as the keys
                and the number of times the letter occurs in the word as the associated value.
            word_prog: a list of 0's the same length as the word

        """
        if word==None:
            super().__init__(word=None)
        else:
            super().__init__(word)
        self.word_track=self.__word_track__(self.word)
        self.word_prog=[0]*self.length
    def __word_track__(self, word):
        """This method initalizes the tracking method for the gamemode hard.
        Arguements:
            word: string of letters
        Returns:
            word_track: a list of dictionarys (one for each letter in word). Each dictonary has each letter of the alphabet as the keys
                and the number of times the letter occurs in the word as the associated value.
        """
        word_track=[]
        for letter in word.upper():
            alphabet={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
            alphabet[letter]=1
            word_track+=[alphabet]
        return word_track
    
    def __guess_location__(self,location):
        """This method takes location guesses.
        Arguements:
            location: any integer in the range of word length
        """
        if self.word_prog[location]==1:
            self.location=None
            return None
        if self.word_prog[location]==0:
            self.location=location
            return location

    def __guess_valid__(self, guess):
        """This method validates that a letter guess is valid depending on location guess. A guess is invalid if it has already been guessesed in that location.
        Arguements:
            guess: a single alphabetical string
        Returns:
            count: returns count=0 if the guess is valid but not correct, returns count=1 if the guess is valid and correct.
            "DNE": returns "DNE" if guess is invalid
            Self: updates word prog and player word
        """
        location=self.location
        try:
            count=self.word_track[location][guess]
            if count==1:
                self.player_word[location]=str(guess)
                self.word_prog[location]=1
            return count
        except KeyError:
            return "DNE"
        
    def __update_pword__(self,guess):
        """This method updates the player word depending on the guessed location and letter
        Returns:
            player_word: updated player word
        """
        self.player_word[self.location]=guess.upper()
        return self.player_word

    def __turn__(self,guess):
        count=self.__guess_valid__(guess)
        if count=="DNE":
            return count
        count=super().__turn__(guess)
        self.word_track[self.location].pop(guess.upper())
        return count


class AlienInvasionEasyGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #Initalize game pages
        start_page=Frame(self,width=600,height=500)
        game_page=Frame(self,width=600,height=500)
        finish_page=Frame(self)
        start_page.grid(row=0,column=0,sticky="snew")
        game_page.grid(row=0,column=0,sticky="snew")
        finish_page.grid(row=0,column=0,sticky="snew")

        self.start_page=start_page
        self.finish_page=finish_page
        self.game_page=game_page

        #Initalize game images
        self.images=["lost_img.png","1guesses_img.png","2guesses_img.png","3guesses_img.png","4guesses_img.png","5guesses_img.png","6guesses_img.png","7guesses_img.png","win_img.png"]
        self.game_images=[]
        for image in range(len(self.images)):
            photo=Image.open(self.images[image])
            resized=photo.resize((250,250))
            converted=ImageTk.PhotoImage(resized)
            self.images[image]=converted

        #Set up start page
        start_label=Label(start_page, text="Welcome to Alien Invasion!")
        start_label.place(x=100,y=3,anchor="nw",width=400,height=100)
        start_button=Button(start_page,text="Start", command=lambda: self.__start_game__(), bg="green" )
        start_button.place(x=100,y=450,anchor="nw",width=200,height=25)
        self.start_button=start_button

        #Game page set up
        self.__set_up_game_screen__(game_page)

        #Game page image display set up
        game_image=tk.Label(self.progress_disp_frame,image=self.images[7])
        game_image.pack()

        self.game_image=game_image

        #Set window properties
        self.geometry("600x520")
        self.title("Alien Invasion")
        self.start_page.tkraise()

    def __set_up_game_screen__(self,screen):
        game_label=Label(screen, text="Welcome to Alien Invasion!\nYou must guess the word to stay safe!")
        game_label.pack(side="top")
        progress_disp_frame=tk.Frame(screen)
        progress_disp_frame.pack(side="top")
        self.progress_disp_frame=progress_disp_frame
        game_page_progress=Label(progress_disp_frame,text=None)
        game_page_progress.pack()
        game_page_results=Label(progress_disp_frame,text=None)
        game_page_results.pack()
        self.game_page_progress=game_page_progress
        self.game_page_results=game_page_results
        letters_display=tk.Frame(screen)
        letters_display.pack(side="bottom")
        self.letters_display=letters_display
        ltr_one=tk.Frame(letters_display)
        ltr_one.pack(side="top")
        ltr_two=tk.Frame(letters_display)
        ltr_two.pack(side="top")
        ltr_three=tk.Frame(letters_display)
        ltr_three.pack(side="top")
        self.ltr_three=ltr_three
        a_button=Button(ltr_one,text="A", command=lambda:self.__take_guess__("A",a_button),width=5,height=2)
        b_button=Button(ltr_one,text="B", command=lambda:self.__take_guess__("B",b_button),width=5,height=2)
        c_button=Button(ltr_one,text="C", command=lambda:self.__take_guess__("C",c_button),width=5,height=2)
        d_button=Button(ltr_one,text="D", command=lambda:self.__take_guess__("D",d_button),width=5,height=2)
        e_button=Button(ltr_one,text="E", command=lambda:self.__take_guess__("E",e_button),width=5,height=2)
        f_button=Button(ltr_one,text="F", command=lambda:self.__take_guess__("F",f_button),width=5,height=2)
        g_button=Button(ltr_one,text="G", command=lambda:self.__take_guess__("G",g_button),width=5,height=2)
        h_button=Button(ltr_one,text="H", command=lambda:self.__take_guess__("H",h_button),width=5,height=2)
        i_button=Button(ltr_one,text="I", command=lambda:self.__take_guess__("I",i_button),width=5,height=2)
        j_button=Button(ltr_two,text="J", command=lambda:self.__take_guess__("J",j_button),width=5,height=2)
        k_button=Button(ltr_two,text="K", command=lambda:self.__take_guess__("K",k_button),width=5,height=2)
        l_button=Button(ltr_two,text="L", command=lambda:self.__take_guess__("L",l_button),width=5,height=2)
        m_button=Button(ltr_two,text="M", command=lambda:self.__take_guess__("M",m_button),width=5,height=2)
        n_button=Button(ltr_two,text="N", command=lambda:self.__take_guess__("N",n_button),width=5,height=2)
        o_button=Button(ltr_two,text="O", command=lambda:self.__take_guess__("O",o_button),width=5,height=2)
        p_button=Button(ltr_two,text="P", command=lambda:self.__take_guess__("P",p_button),width=5,height=2)
        q_button=Button(ltr_two,text="Q", command=lambda:self.__take_guess__("Q",q_button),width=5,height=2)
        r_button=Button(ltr_two,text="R", command=lambda:self.__take_guess__("R",r_button),width=5,height=2)
        s_button=Button(ltr_three,text="S", command=lambda:self.__take_guess__("S",s_button),width=5,height=2)
        t_button=Button(ltr_three,text="T", command=lambda:self.__take_guess__("T",t_button),width=5,height=2)
        u_button=Button(ltr_three,text="U", command=lambda:self.__take_guess__("U",u_button),width=5,height=2)
        v_button=Button(ltr_three,text="V", command=lambda:self.__take_guess__("V",v_button),width=5,height=2)
        w_button=Button(ltr_three,text="W", command=lambda:self.__take_guess__("W",w_button),width=5,height=2)
        x_button=Button(ltr_three,text="X", command=lambda:self.__take_guess__("X",x_button),width=5,height=2)
        y_button=Button(ltr_three,text="Y", command=lambda:self.__take_guess__("Y",y_button),width=5,height=2)
        z_button=Button(ltr_three,text="Z", command=lambda:self.__take_guess__("Z",z_button),width=5,height=2)
    
        a_button.pack(side="left")
        b_button.pack(side="left")
        c_button.pack(side="left")
        d_button.pack(side="left")
        e_button.pack(side="left")
        f_button.pack(side="left")
        g_button.pack(side="left")
        h_button.pack(side="left")
        i_button.pack(side="left")
        j_button.pack(side="left")
        k_button.pack(side="left")
        l_button.pack(side="left")
        m_button.pack(side="left")
        n_button.pack(side="left")
        o_button.pack(side="left")
        p_button.pack(side="left")
        q_button.pack(side="left")
        r_button.pack(side="left")
        s_button.pack(side="left")
        t_button.pack(side="left")
        u_button.pack(side="left")
        v_button.pack(side="left")
        w_button.pack(side="left")
        x_button.pack(side="left")
        y_button.pack(side="left")
        z_button.pack(side="left")
        buttons=[a_button,b_button,c_button,d_button,e_button,f_button,g_button,h_button,i_button,j_button,k_button,l_button,m_button,
                 n_button,o_button,p_button,q_button,r_button,s_button,t_button,u_button,v_button,w_button,x_button,y_button,z_button]
        self.buttons=buttons

    def __switch_img__(self,x):
        """This method switches the image display
        Arguments:
            x: any int 0-8 corresponds to the list location of the image.
        Return:
            The game image displayed will change
        """
        self.game_image.configure(image=self.images[x])

    def __switch_screen__(self,page):
        """This method switches the screen
        Arguments:
            page: the page that should be displayed
        return:
            The game page will change
        """
        page.tkraise()

    def __start_game__(self):
        """This method is used to start the game. It is run when the user clicks the start button.
        Return:
            Self.game: instance of game class
            Self.game_page_progress: label showing the guesses remain and word display
        """
        newgame=AlienInvasion()
        self.game=newgame
        self.__switch_img__(self.game.guesses)
        self.game_page_progress.forget()
        self.game_page_progress=Label(self.progress_disp_frame,text=("Guesses remaining:"+str(self.game.guesses)+"\nWord:"+str(self.__word_display__())))
        self.game_page_progress.pack(side="top")
        self.__switch_screen__(self.game_page)

    def __word_display__(self):
        """This method takes the player_word as reformats it to be displayed on the GUI.
        Returns:
            display_test: string
        """
        display_text=""
        for letter in self.game.player_word:
            if letter =="_":
                display_text+="___  "
            else:
                display_text+="_"+str(letter.upper())+"_   "
        return display_text
    
    def __word_display_control__(self,message=1):
        """This method controls the word display for the game GUI
        Arguements:
            Message: Either defaults to 1 which sets the message to the default format. A string can be assigned and this will be displayed instead.
        """
        if message==1:
            message="Guesses remaining:"+str(self.game.guesses)+"\nWord:"+str(self.__word_display__())
        self.game_page_progress.forget()
        self.game_page_progress=Label(self.progress_disp_frame,text=message)
        self.game_page_progress.pack(side="top")

    def __results_control__(self,message):
        """This method controls the results display for the GUI. The results for each guess will be displayed here.
        Arguements:
            message: string to be displayed in game results, contains count of guess in word or invalid message.
        """
        self.game_page_results.forget()
        self.game_page_results=Label(self.progress_disp_frame,text=message)
        self.game_page_results.pack(side="bottom")

    def __finish_button__(self,*widgetid):
        """This method runs when the finish button is clicked. Resets gamescreen and returns to start screen.
        Arguements:
            widgetid: widgets, for example labels and buttons, that should be forgotten in order to reset screen. 
        """
        for widget in widgetid:
            widget.forget()
        self.__switch_screen__(self.start_page)
        for button in self.buttons:
            button.configure(bg="white")
        self.game_page_results.forget()

    def __reveal_word_button__(self,buttonid):
        """This method runs when the reveal word button is clicked. It displays the game word to the user. 
        Arguements:
            buttonid: reveal word button 
        """
        buttonid.forget()
        reveal_label=Label(self.game_page,text="The word was: "+self.game.word.upper())
        reveal_label.pack()
        finish_button=Button(self.ltr_three,text="FINISH", command=lambda:self.__finish_button__(finish_button,reveal_label),bg="gold")
        finish_button.pack(side="bottom")

    def __check_game_progress__(self):
        """This method checks game progress, depending on if the user has won or lost the corresponding image and message will be displayed. If the user looses a button is added to reveal the game word.
        """
        progress=self.game.__check_win_lose__()
        if progress==True:
            results_message="You won!"
            progress_message="\nWord:"+str(self.__word_display__())
            self.__results_control__(results_message)
            self.__word_display_control__(progress_message)
            finish_button=Button(self.ltr_three,text="FINISH!", command=lambda:self.__finish_button__(finish_button),bg="gold")
            finish_button.pack(side="bottom")
            self.__switch_img__(8)
        if progress==False:
            results_message="Uh oh, you lost!"
            progress_message="\nWord:"+str(self.__word_display__())
            self.__results_control__(results_message)
            self.__word_display_control__(progress_message)
            reveal_word_button=Button(self.game_page,text="View Results", command=lambda:self.__reveal_word_button__(reveal_word_button))
            reveal_word_button.pack(side="bottom")

    def __take_guess__(self,guess,button):
        """This method runs when the letter buttons are clicked. If they 
        Arguments:
            guess: single letter string corresponding with the button
            button: letter button selected
        Returns:
            None: no changes or return if the user has no guesses remaining. If the guess is invalid display message with no gane changes.
                    For a valid guess:
                    if there are no occurannces of the letter in the word then button turns red. If guess is correct the button turns green.
                    correspondiong results image and player word is displayed.
        """
        if self.game.guesses==0:
            return
        count=self.game.__turn__(guess)
        if count=="DNE":
            results_message="Invalid guess, try again!"
            self.__results_control__(results_message)
            return
        if count==0 or count==None:
            count="is no "
            button.configure(bg="red")
        else:
            button.configure(bg="green")
            if count>1:
                count="are "+str(count)+" "
            else:
                count="is "+str(count)+" "
        results_message="There "+str(count)+str(guess)+" in the word\nYou have "+str(self.game.guesses)+" guesses left."
        self.__results_control__(results_message)
        self.__switch_img__(self.game.guesses)
        self.__word_display_control__()
        self.__check_game_progress__()


class AlienInvasionHardGUI(AlienInvasionEasyGUI):
    def __init__(self):
        super().__init__()

        #Save created properties as game page hard attributes
        self.ltr_three_hard=self.ltr_three
        self.game_page_hard=self.game_page
        self.game_image_hard=self.game_image
        self.progress_disp_frame_hard=self.progress_disp_frame
        self.game_page_progress_hard=self.game_page_progress
        self.game_page_results_hard=self.game_page_results
        self.progress_disp_frame_hard=self.progress_disp_frame
        self.letters_display_hard=self.letters_display
        finish_button=Button(self.ltr_three_hard,text="FINISH", command=lambda:self.__finish_button__(finish_button))
        self.finish_button_hard=finish_button
        self.game_page_results_hard.forget()
    
        #add extra buttons for position choice
        word_disp=tk.Frame(self.progress_disp_frame_hard)
        word_disp.pack(side="bottom")
        one_button=Button(word_disp,text="___",command=lambda:self.__choose_location__(0,one_button),width=5,height=2,bg="white")
        two_button=Button(word_disp,text="___",command=lambda:self.__choose_location__(1,two_button),width=5,height=2,bg="white")
        three_button=Button(word_disp,text="___",command=lambda:self.__choose_location__(2,three_button),width=5,height=2,bg="white")
        four_button=Button(word_disp,text="___",command=lambda:self.__choose_location__(3,four_button),width=5,height=2,bg="white")
        five_button=Button(word_disp,text="___",command=lambda:self.__choose_location__(4,five_button),width=5,height=2,bg="white")
        six_button=Button(word_disp,text="___",command=lambda:self.__choose_location__(5,six_button),width=5,height=2,bg="white")
        self.word_disp=word_disp
        word_buttons=[one_button,two_button,three_button,four_button,five_button,six_button]
        self.word_buttons=word_buttons

        #set up results display
        results_disp=tk.Frame(self.word_disp)
        results_disp.pack(side="bottom")
        self.game_page_results_hard=Label(results_disp,text="Choose a location to begin.")
        self.game_page_results_hard.pack(side="top")
        self.results_disp=results_disp

        #Create new game page for easy mode
        game_page_easy=Frame(self)
        game_page_easy.grid(row=0,column=0,sticky="snew")
        self.game_page=game_page_easy

        #Forget orignial start button
        self.start_button.destroy()
        #new start buttons
        start_button_easy=Button(self.start_page,text="Easy", command=lambda: self.__start_game__(),bg="green" )
        start_button_easy.place(x=100,y=450,anchor="nw",width=200,height=50) 
        start_button_hard=Button(self.start_page,text="Hard", command=lambda: self.__start_game_hard__(),bg="red" )
        start_button_hard.place(x=300,y=450,anchor="nw",width=200,height=50)

        #Set up new game page
        self.__set_up_game_screen__(self.game_page)

        #Set up image display for hard game page
        self.ltr_three_hard=self.ltr_three
        easy_image=tk.Label(self.progress_disp_frame,image=self.images[7])
        easy_image.pack()
        self.game_image=easy_image

        #Set title screen photo.
        start_image=tk.Label(self.start_page,image=self.images[8])
        start_image.place(x=200,y=100)

        #Start program of start page
        self.start_page.tkraise() 

    def __switch_img_hard__(self,x):
        """This method is used to switch the hard game image.
        Arguments:
            x: integer corresponding to the image that should be displayed.
        """
        self.game_image_hard.configure(image=self.images[x])
    
    def __start_game__(self):
        """This method sets the game mode then begins the easy mode of the game.
        """
        self.gamemode="easy"
        super().__start_game__()

    def __start_game_hard__(self):
        """This method sets the game mode to hard then begins the hard mode of the game
        """
        self.gamemode="hard"
        self.game=AlienInvasionHard()
        self.buttons_invalid=[list()]*self.game.length
        self.game.location=None
        for letter in range(self.game.length):
            self.word_buttons[letter].pack(side="left")
        self.__switch_img_hard__(self.game.guesses)
        self.__word_display_control_hard__()
        self.__switch_screen__(self.game_page_hard)

    def __choose_location__(self,location,button):
        """This method is called when users click location buttons. If game is won or lost already no changes are made. If location is valid inidcate valid guesses with 
            with button color.
        Arguements:
            location: integer in range 0-5(inc) that corresponding to location in string that user wants to guess
            button: location button that was clicked
        """
        if self.game.location!=None:
            self.word_buttons[self.game.location].configure(bg="white")
            for button in self.buttons_invalid[self.game.location]:
                button.configure(bg="white")
        if self.game.guesses==0 or self.game.__check_win_lose__()==True:
            return
        self.game.__guess_location__(location)
        if self.game.location==None:
            return
        self.word_buttons[location].configure(bg="yellow")
        for button in self.buttons_invalid[location]:
            button.configure(bg="red")
        self.game.__guess_location__(location)
        self.__results_control_hard__("Now choose a letter")

    def __word_display_control_hard__(self):
        """This method controls the word display for the game hard mode. Displays how many guesses remaining the user has remaining.
        """
        message="Guesses remaining:"+str(self.game.guesses)+"\nWord:"
        self.game_page_progress_hard.forget()
        self.game_page_progress_hard=Label(self.progress_disp_frame_hard,text=message)
        self.game_page_progress_hard.pack(side="top")

    def __results_control_hard__(self,message):
        """This method is used to control the results for the hard game mode. Displays how many guesses remaining the user has.
        """
        self.game_page_results_hard.forget()
        self.game_page_results_hard=Label(self.results_disp,text=message)
        self.game_page_results_hard.pack(side="bottom")
        
    def __finish_button__(self, *widgetid):
        """This method is run when the user clicks the finish button. Same as parent class but added functionality to reset the hard game page.
        """
        self.__reset_hard__()
        return super().__finish_button__(*widgetid)
    
    def __take_guess__(self, guess, button):
        """This method is called when a letter button is clicked. If user is in hard mode there must be a set game location. The results of the guess are displayed.
            Checks for win or lose at the end. 
        Arguements:
            guess: single letter sting corresponding the letter guess
            button: letter button clicked
        """
        if self.game.guesses==0:
            return
        if self.gamemode=="easy":
            super().__take_guess__(guess,button)
        if self.gamemode=="hard":
            if self.game.location==None:
                message="No location chosen."
                self.__results_control_hard__(message)
                return
            for button_in in self.buttons_invalid[self.game.location]:
                button_in.configure(bg="white")
            if self.game.guesses==0:
                return
            count=self.game.__turn__(guess)
            if count==None:
                self.word_buttons[self.game.location].configure(bg="white")
                self.buttons_invalid[self.game.location]=self.buttons_invalid[self.game.location]+[button]
                message="No "+str(guess)+" in that location."
            if count==1:
                message="Correct! Guess again."
                self.word_buttons[self.game.location].configure(text=guess,bg="green")
            if count=="DNE":
                message="Invalid Guess! Try again."
            self.__switch_img_hard__(self.game.guesses)
            self.__word_display_control_hard__()
            if (self.game.__check_win_lose__())==True:
                self.__switch_img_hard__(8)
                self.finish_button_hard.pack()
                self.finish_button_hard.configure(text="Finish!",bg="gold")
                message="You won! Congrats!"
            if (self.game.__check_win_lose__())==False:
                reveal_word_button=Button(self.results_disp,text="View Results", command=lambda:self.__reveal_word_button_hard__(reveal_word_button))
                reveal_word_button.pack(side="right")
                message="YOU LOST!"
            self.__results_control_hard__(message)
            if count!="DNE":
                self.game.location=None

    def __reveal_word_button_hard__(self, buttonid):
        """This method is called when the user clicks the reveal button word. It reveals the game word and displays and finish button.
        Arguements:
            buttonid: finish button
        """
        buttonid.forget()
        location=0
        for button in self.word_buttons:
            try:
                if self.game.word_prog[location]==0:
                    button.config(text=self.game.word[location].upper(),bg="red")
                location+=1
            except:
                None
        self.finish_button_hard.pack()
        self.finish_button_hard.configure(text="Finish!",bg="gold")

    def __reset_hard__(self):
        """This method is called after the game button is clicked. It resets the hard game page.
        """
        for button in self.word_buttons:
            button.configure(text="__",bg="white")
            button.forget()
            message="To begin choose a location."
            self.__results_control_hard__(message)


class AlienInvasionAddOns(AlienInvasionHardGUI):
    def __init__(self,):
        super().__init__()

        #Dictonary of hints with corresponding words as the key.
        self.hints={"HUSKY":"#LikeA_____","PYTHON":"The best programming language!","CAT":"Has nine lives!","DOG":"Woof!","TEA":"White, green, oolong, and black","ROCK":"Spongebob's bestfriend's house."
                    ,"BINARY":"10010=18","LAMP":"Provides light.","BALLONS":"Great party decor!","APPLE":"Hit sir Issac Newton.","LAPTOP":"Portable computer."}
        
        #Initalize hints display
        hints_frame=tk.Frame(self.word_disp)
        hints_frame.pack(side="bottom")
        hints_button=Button(hints_frame,text="Reveal hint!",command=lambda:self.__reveal_hint__())
        self.hints_button=hints_button
        hints_label=Label(hints_frame,text="",bg="gold")
        self.hints_label=hints_label

        #Set new window geometry to account for hint display
        self.geometry("600x540")

        #Assign new start buttons
        start_button_easy=Button(self.start_page,text="Easy", command=lambda: self.__start_game__(),bg="green" )
        start_button_easy.place(x=100,y=450,anchor="nw",width=200,height=25)
        start_button_easy=Button(self.start_page,text="Easy with a friend!", command=lambda: self.__play_with_friend__(),bg="dark green" )
        start_button_easy.place(x=100,y=475,anchor="nw",width=200,height=25)

    def __finish_button__(self, *widgetid):
        """This method is called when the finish button if pressed. Same as parent but removes hint button.
        """
        self.hints_label.forget()
        return super().__finish_button__(*widgetid)
    
    def __take_guess__(self, guess, button):
        """This method is called when the user selects a letter button guess. Same as parent function but if user has 4 guesses (in gamemode hard) remaining the hints button is shown
        Arguements:
            guess: single string letter corresponding to guess
            button: letter button clicked
        """
        if (self.game.guesses==4) and (self.gamemode=="hard"):
            self.hints_button.pack()
        super().__take_guess__(guess, button)
        if self.game.__check_win_lose__():
            self.hints_label.forget()

    def __reveal_hint__(self):
        """This method is called when the reveal hint button is clicked. Displays hint corresponding with the game word.
        """
        self.hints_button.forget()
        self.hints_label.pack()
        self.hint=self.hints[self.game.word]
        self.hints_label.configure(text=self.hint)

    def __play_with_friend__(self):
        """This method is called when the play with a friend easy mode is selected. A message box pops up that asks the user for a word, word inputted is set to the game word so another user can guess the word. 
        Once the a valid word is inputted the game is started with this word set to the game word.
        """
        word=askstring("Enter a word for your friend to guess!","Enter a word between 1-6 letters.")
        while (word==None) or (word.isalpha()==False) or (len(word)==(0) or (len(word)>6)):
            print(word.isalpha())
            word=askstring("Enter a word for your friend to guess!","ENTER A WORD BETWEEN 1-6 LETTERS!!\nMust be all letter characters.")
        self.friend_word=word
        self.__start_game__(friend=True, word=self.friend_word)

    def __start_game__(self, friend=None,word=None):
        """This method is called when either start easy or start easy with a friend is clicked. If easy with a friend is clicked 
        Arguements:
            friend: True if friend mode is enabled, None if playing alone
            word: 6 letter string or None
        """
        super().__start_game__()
        if friend==True:
             self.game=AlienInvasion(word)
             self.game_page_progress.configure(text=("Guesses remaining:"+str(self.game.guesses)+"\nWord:"+str(self.__word_display__())))


Run_AlienInvasion=AlienInvasionAddOns()
#Alien Invasion Full game and Alien Invasion Hints can both be ran using a predetermined word as a keyword string argument
#to be compatible with the codes hardmode gamefeature display the keyword string argument must be 1-6 characters long.

Run_AlienInvasion.mainloop()

