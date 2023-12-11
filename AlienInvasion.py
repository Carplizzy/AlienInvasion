import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk


class AlienInvasion():
    def __init__(self,word=None):
        """
        Attributes:
            word: game word, determined randomly from preset words
            word_track: 
            guesses: how many guesses the user has left, initally 7, each incorrect guess counts as a guess
            self.length: length of game word or number of letters in word
            player_word: word progress of player, italizes to list of "___" (one for each letter in word) 
        """
        if word!=None:
            self.word=word
        else:
            self.word=AlienInvasion._gen_word_()
        self.total_guesses=7
        self.guesses=self.total_guesses
        self.word_track=self.__word_track__(self.word)
        self.player_word=["_"]*len(self.word)
        self.exit=False
        self.length=len(self.word)

    def _gen_word_():
        """This method randomly selects a word from the list words.
        Returns: 
            word:any word is the list words
        """
        words=["dog","cat","apple","pie","lime","ballon","cookie","lamp","pea","scarf","mittens","husky","python"]
        index=random.randrange(0,12)
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
    
    def _check_win_lose_(self):
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
    def _check_win_(self):
        """This method checks if  
        """
        return super()._check_win_lose_()
    def __turn__(self,guess):
        count=self.__guess_valid__(guess)
        if count=="DNE":
            return count
        count=super().__turn__(guess)
        self.word_track[self.location].pop(guess.upper())
        return count


class window(tk.Tk):
#Pages set up
    def __init__(self):
        self.game=None
        tk.Tk.__init__(self)
        start_page=Frame(self,width=600,height=500)
        
        game_page=Frame(self,width=600,height=500)
        finish_page=Frame(self)
        start_page.grid(row=0,column=0,sticky="snew")
        game_page.grid(row=0,column=0,sticky="snew")
        finish_page.grid(row=0,column=0,sticky="snew")


        #set up game images
        self.images=["lost.png","6.png","5.png","4.png","3.png","2.png","1.png","0.png","win.png"]
        self.game_images=[]
        for image in range(len(self.images)):
            photo=Image.open(self.images[image])
            resized=photo.resize((250,250))
            converted=ImageTk.PhotoImage(resized)
            self.images[image]=converted


        #Start page set up
        start_label=Label(start_page, text="Welcome to Alien Invasion!")
        start_label.place(x=100,y=3,anchor="nw",width=400,height=100)
        start_button=Button(start_page,text="Start", command=lambda: self._start_game_() )
        start_button.place(x=200,y=400,anchor="nw",width=200,height=50)
        self.start_button=start_button

        #Game page set up
        self._set_up_game_screen(game_page)


        #####
        
        #game image finish set up
        game_image=tk.Label(self.progress_disp_frame,image=self.images[7])
        game_image.pack()
        self.game_image=game_image

        


        #Finish page set up
        finish_label=Label(finish_page, text="Uh oh....\n You lost!")
        finish_label.pack()
        lose_image=tk.Label(finish_page,image=self.images[0])
        lose_image.pack()

        self.geometry("600x520")
        self.title("Alien Invasion")
        self.start_page=start_page
        self.finish_page=finish_page
        self.game_page=game_page
        self.start_page.tkraise()
    def _set_up_game_screen(self,screen):
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
        a_button=Button(ltr_one,text="A", command=lambda:self._take_guess_("A",a_button),width=5,height=2)
        b_button=Button(ltr_one,text="B", command=lambda:self._take_guess_("B",b_button),width=5,height=2)
        c_button=Button(ltr_one,text="C", command=lambda:self._take_guess_("C",c_button),width=5,height=2)
        d_button=Button(ltr_one,text="D", command=lambda:self._take_guess_("D",d_button),width=5,height=2)
        e_button=Button(ltr_one,text="E", command=lambda:self._take_guess_("E",e_button),width=5,height=2)
        f_button=Button(ltr_one,text="F", command=lambda:self._take_guess_("F",f_button),width=5,height=2)
        g_button=Button(ltr_one,text="G", command=lambda:self._take_guess_("G",g_button),width=5,height=2)
        h_button=Button(ltr_one,text="H", command=lambda:self._take_guess_("H",h_button),width=5,height=2)
        i_button=Button(ltr_one,text="I", command=lambda:self._take_guess_("I",i_button),width=5,height=2)
        j_button=Button(ltr_two,text="J", command=lambda:self._take_guess_("J",j_button),width=5,height=2)
        k_button=Button(ltr_two,text="K", command=lambda:self._take_guess_("K",k_button),width=5,height=2)
        l_button=Button(ltr_two,text="L", command=lambda:self._take_guess_("L",l_button),width=5,height=2)
        m_button=Button(ltr_two,text="M", command=lambda:self._take_guess_("M",m_button),width=5,height=2)
        n_button=Button(ltr_two,text="N", command=lambda:self._take_guess_("N",n_button),width=5,height=2)
        o_button=Button(ltr_two,text="O", command=lambda:self._take_guess_("O",o_button),width=5,height=2)
        p_button=Button(ltr_two,text="P", command=lambda:self._take_guess_("P",p_button),width=5,height=2)
        q_button=Button(ltr_two,text="Q", command=lambda:self._take_guess_("Q",q_button),width=5,height=2)
        r_button=Button(ltr_two,text="R", command=lambda:self._take_guess_("R",r_button),width=5,height=2)
        s_button=Button(ltr_three,text="S", command=lambda:self._take_guess_("S",s_button),width=5,height=2)
        t_button=Button(ltr_three,text="T", command=lambda:self._take_guess_("T",t_button),width=5,height=2)
        u_button=Button(ltr_three,text="U", command=lambda:self._take_guess_("U",u_button),width=5,height=2)
        v_button=Button(ltr_three,text="V", command=lambda:self._take_guess_("V",v_button),width=5,height=2)
        w_button=Button(ltr_three,text="W", command=lambda:self._take_guess_("W",w_button),width=5,height=2)
        x_button=Button(ltr_three,text="X", command=lambda:self._take_guess_("X",x_button),width=5,height=2)
        y_button=Button(ltr_three,text="Y", command=lambda:self._take_guess_("Y",y_button),width=5,height=2)
        z_button=Button(ltr_three,text="Z", command=lambda:self._take_guess_("Z",z_button),width=5,height=2)
    
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
        buttons=[a_button,b_button,c_button,d_button,e_button,f_button,g_button,h_button,i_button,j_button,k_button,l_button,m_button,n_button,o_button,p_button,q_button,r_button,s_button,t_button,u_button,v_button,w_button,x_button,y_button,z_button]
        self.buttons=buttons
    def _switch_img_(self,x):
        self.game_image.configure(image=self.images[x])
    def _switch_screen_(self,page):
        page.tkraise()
    def _start_game_(self):
        newgame=AlienInvasion()
        self.game=newgame
        self._switch_img_(self.game.guesses)
        self.game_page_progress.forget()
        self.game_page_progress=Label(self.progress_disp_frame,text=("Guesses remaining:"+str(self.game.guesses)+"\nWord:"+str(self._word_display_())))
        self.game_page_progress.pack(side="top")
        self._switch_screen_(self.game_page)
    def _word_display_(self):
        display_text=""
        for letter in self.game.player_word:
            if letter =="_":
                display_text+="___  "
            else:
                display_text+="_"+str(letter.upper())+"_   "
        return display_text
    def _word_display_control_(self,message=1):
        if message==1:
            message="Guesses remaining:"+str(self.game.guesses)+"\nWord:"+str(self._word_display_())
        self.game_page_progress.forget()
        self.game_page_progress=Label(self.progress_disp_frame,text=message)
        self.game_page_progress.pack(side="top")
    def _results_control_(self,message):
        self.game_page_results.forget()
        self.game_page_results=Label(self.progress_disp_frame,text=message)
        self.game_page_results.pack(side="bottom")
    def _finish_button_(self,*widgetid):
        for widget in widgetid:
            widget.forget()
        self._switch_screen_(self.start_page)
        for button in self.buttons:
            button.configure(bg="white")
        self.game_page_results.forget()
    def _reveal_word_button_(self,buttonid):
        buttonid.forget()
        reveal_label=Label(self.game_page,text="The word was: "+self.game.word.upper())
        reveal_label.pack()
        finish_button=Button(self.ltr_three,text="FINISH", command=lambda:self._finish_button_(finish_button,reveal_label),bg="gold")
        finish_button.pack(side="bottom")
    def _check_game_progress_(self):
        progress=self.game._check_win_lose_()
        if progress==True:
            results_message="You won!"
            progress_message="\nWord:"+str(self._word_display_())
            self._results_control_(results_message)
            self._word_display_control_(progress_message)
            finish_button=Button(self.ltr_three,text="FINISH!", command=lambda:self._finish_button_(finish_button),bg="gold")
            finish_button.pack(side="bottom")
            self._switch_img_(8)
        if progress==False:
            results_message="Uh oh, you lost!"
            progress_message="\nWord:"+str(self._word_display_())
            self._results_control_(results_message)
            self._word_display_control_(progress_message)
            reveal_word_button=Button(self.game_page,text="View Results", command=lambda:self._reveal_word_button_(reveal_word_button))
            reveal_word_button.pack(side="bottom")

    def _take_guess_(self,guess,button):
        if self.game.guesses==0:
            return
        count=self.game.__turn__(guess)
        if count=="DNE":
            results_message="Invalid guess, try again!"
            self._results_control_(results_message)
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
        self._results_control_(results_message)
        self._switch_img_(self.game.guesses)
        self._word_display_control_()
        self._check_game_progress_()

class inheritance(window):
    def __init__(self):
        #create start page, hard game page
        super().__init__()
        self.ltr_three_hard=self.ltr_three
        self.game_page_hard=self.game_page
        self.game_image_hard=self.game_image
        self.progress_disp_frame_hard=self.progress_disp_frame
        self.game_page_progress_hard=self.game_page_progress
        self.game_page_results_hard=self.game_page_results
        self.progress_disp_frame_hard=self.progress_disp_frame
        self.letters_display_hard=self.letters_display
        finish_button=Button(self.ltr_three_hard,text="FINISH", command=lambda:self._finish_button_(finish_button))
        finish_button.pack(side="bottom")
        self.finish_button_hard=finish_button
        self.game_page_results_hard.forget()
        self.finish_button_hard.forget()
    

        #add extra buttons for position choice
        word_disp=tk.Frame(self.progress_disp_frame_hard)
        word_disp.pack(side="bottom")
        one_button=Button(word_disp,text="___",command=lambda:self._choose_location_(0,one_button),width=5,height=2,bg="white")
        one_button_letters=self.buttons
        two_button=Button(word_disp,text="___",command=lambda:self._choose_location_(1,two_button),width=5,height=2,bg="white")
        two_button_letters=self.buttons
        three_button=Button(word_disp,text="___",command=lambda:self._choose_location_(2,three_button),width=5,height=2,bg="white")
        three_button_letters=self.buttons
        four_button=Button(word_disp,text="___",command=lambda:self._choose_location_(3,four_button),width=5,height=2,bg="white")
        four_button_letters=self.buttons
        five_button=Button(word_disp,text="___",command=lambda:self._choose_location_(4,five_button),width=5,height=2,bg="white")
        five_button_letters=self.buttons
        six_button=Button(word_disp,text="___",command=lambda:self._choose_location_(5,six_button),width=5,height=2,bg="white")
        six_button_letters=self.buttons
        self.word_disp=word_disp
        word_buttons=[one_button,two_button,three_button,four_button,five_button,six_button]
        self.word_buttons=word_buttons


        #set up results display
        results_disp=tk.Frame(self.word_disp)
        results_disp.pack(side="bottom")
        self.game_page_results_hard=Label(results_disp,text="Choose a location to begin.")
        self.game_page_results_hard.pack(side="top")
        self.results_disp=results_disp

        #new frame for game
        game_page_easy=Frame(self)
        game_page_easy.grid(row=0,column=0,sticky="snew")
        self.game_page=game_page_easy

        #forget original start button
        self.start_button.destroy()
        #new start buttons
        start_button_easy=Button(self.start_page,text="Easy", command=lambda: self._start_game_(),bg="green" )
        start_button_easy.place(x=100,y=450,anchor="nw",width=200,height=50) 
        start_button_hard=Button(self.start_page,text="Hard", command=lambda: self._start_game_hard_(),bg="red" )
        start_button_hard.place(x=300,y=450,anchor="nw",width=200,height=50)

        #set up new game page for easy

        self._set_up_game_screen(self.game_page)

        #set up images
        self.ltr_three_hard=self.ltr_three
        easy_image=tk.Label(self.progress_disp_frame,image=self.images[7])
        easy_image.pack()
        self.game_image=easy_image

        #title screen photos
        start_image=tk.Label(self.start_page,image=self.images[8])
        start_image.place(x=200,y=100)

        #start on start screen
        self.start_page.tkraise() 
    def _pack_finish_button_(self):
        finish_button=Button(self.ltr_three_hard,text="FINISH", command=lambda:self._finish_button_(finish_button),bg="gold")
        finish_button.pack(side="left")
        return finish_button
    def _switch_img_hard_(self,x):
        self.game_image_hard.configure(image=self.images[x])
    def _switch_screen_(self, page):
        return super()._switch_screen_(page)
    def _start_game_(self):
        self.gamemode="easy"
        super()._start_game_()
    def _start_game_hard_(self):
        self.gamemode="hard"
        self.game=AlienInvasionHard()
        self.buttons_invalid=[list()]*self.game.length
        self.game.location=None
        for letter in range(self.game.length):
            self.word_buttons[letter].pack(side="left")
        self._switch_img_hard_(self.game.guesses)
        self._word_display_control_hard_()
        self._switch_screen_(self.game_page_hard)
    def _choose_location_(self,location,button):
        if self.game.location!=None:
            self.word_buttons[self.game.location].configure(bg="white")
            for button in self.buttons_invalid[self.game.location]:
                button.configure(bg="white")
        if self.game.guesses==0 or self.game._check_win_()==True:
            return
        self.game.__guess_location__(location)
        if self.game.location==None:
            return
        self.word_buttons[location].configure(bg="yellow")
        for button in self.buttons_invalid[location]:
            button.configure(bg="red")
        self.game.__guess_location__(location)
        self._results_control_hard_("Now choose a letter")
    def _word_display_control_hard_(self):
        message="Guesses remaining:"+str(self.game.guesses)+"\nWord:"
        self.game_page_progress_hard.forget()
        self.game_page_progress_hard=Label(self.progress_disp_frame_hard,text=message)
        self.game_page_progress_hard.pack(side="top")
    def _results_control_hard_(self,message):
        self.game_page_results_hard.forget()
        self.game_page_results_hard=Label(self.results_disp,text=message)
        self.game_page_results_hard.pack(side="bottom")
    def _finish_button_(self, *widgetid):
        self._reset_hard_()
        return super()._finish_button_(*widgetid)
    def _take_guess_(self, guess, button):
        if self.game.guesses==0:
            return
        if self.gamemode=="easy":
            super()._take_guess_(guess,button)
        if self.gamemode=="hard":
            if self.game.location==None:
                message="No location chosen."
                self._results_control_hard_(message)
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
            self._switch_img_hard_(self.game.guesses)
            self._word_display_control_hard_()
            if (self.game._check_win_lose_())==True:
                self._switch_img_hard_(8)
                self.finish_button_hard.pack()
                self.finish_button_hard.configure(text="Finish!",bg="gold")
                message="You won! Congrats!"
            if (self.game._check_win_lose_())==False:
                reveal_word_button=Button(self.results_disp,text="View Results", command=lambda:self._reveal_word_button_hard_(reveal_word_button))
                reveal_word_button.pack(side="right")
                message="YOU LOST!"
            self._results_control_hard_(message)
            if count!="DNE":
                self.game.location=None
    def _reveal_word_button_hard_(self, buttonid):
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
    def _reset_hard_(self):
        for button in self.word_buttons:
            button.configure(text="__",bg="white")
            button.forget()
            message="To begin choose a location."
            self._results_control_hard_(message)

game=inheritance()
game.mainloop()
