from tkinter import *


import webbrowser
import word_wiki_main_script as word_main


main_window  = Tk()
main_window.grid()

main_window.title('Welcome to WordWiki by logical1862' )

# Specify Grid
Grid.rowconfigure(main_window,0,weight=1)
Grid.columnconfigure(main_window,0,weight=1)
 
 ###
 #search input box with default value
search_choice = Entry(main_window, text=word_main.input2)
search_choice.grid(row=0, columnspan=2, sticky=NSEW, padx=25, pady= 15) 
 ###

suggested_choice_list = Listbox(main_window, listvariable=word_main.input1)
suggested_choice_list.grid(row=2, columnspan=2, sticky=NSEW, padx=35, pady= 20)

##


wiki_summary_label = Label(main_window, text='Wikepedia excerpt:', relief=RAISED, bd= 6, bg = 'white')
wiki_summary_label.grid(row=3, column=0, sticky=NSEW, padx=35, pady= 20)

wiki_summary_result = Label(main_window, text=word_main.excerpt_limit  + '...', relief=SUNKEN, wraplength=600, bd= 6, bg = 'white')
wiki_summary_result.grid(row=3, column=1, sticky=NSEW, padx=35, pady= 20)


## link to wikipedia page, needs work
def open_link(event):
    webbrowser.open_new(event.widget.cget('button'))


wiki_link_result = Label(main_window, text=word_main.wiki_link, relief=RAISED, bd= 4, bg= 'white')
wiki_link_result.grid(row=4, column=1, sticky=NSEW, padx=20, pady=15)
wiki_link_result.bind('link', open_link)

##

definition_result = Label(main_window, text=word_main.word_definition, relief=RAISED, bd= 6, bg = 'white')
definition_result.grid(row=5, column=1, sticky=NSEW, padx=35, pady= 20)
#
synonym_result = Label(main_window, text=word_main.word_synonym, relief=RAISED, bd= 6, bg = 'white')
synonym_result.grid(row=6, column=1, sticky=NSEW, padx=35, pady= 20)
#
antonym_result = Label(main_window, text= word_main.word_antonym, relief=RAISED, bd= 6, bg = 'white')
antonym_result.grid(row=7, column=1, sticky=NSEW, padx=35, pady= 20)

main_window.mainloop()