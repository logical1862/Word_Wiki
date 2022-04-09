from tkinter import *
import wikipedia
from PIL import ImageTk,Image
from word_wiki_classes import wiki_data, word_data
import os


search_string = 'cat'



wiki_inst = wiki_data()
search_instance = word_data


wiki_inst.input_string = search_string
search_instance.input_string = search_string


suggested_page= wikipedia.page(wiki_inst.input_string, redirect=True, auto_suggest=False)
summary = '{}'.format(suggested_page.summary)
url = '{}'.format(suggested_page.url)

word_definition = search_instance.definition(search_instance)
word_synonym = search_instance.synonym(search_instance)
word_antonym = search_instance.antonym(search_instance)






tk = Tk()
tk.grid()

Grid.rowconfigure(tk,0,weight=1)
Grid.columnconfigure(tk,0,weight=1)

main_window  = Label(tk)




main_window.grid(sticky= NSEW)
    
tk.title('Welcome to WordWiki by logical1862' )


# Specify Grid

Grid.rowconfigure(main_window,0,weight=1)
Grid.columnconfigure(main_window,0,weight=1)
 
 ###
 #search input box with default value
current_string = '{}'.format(wiki_inst.input_string)
text_str = 'enter search word:(current search:', current_string, ')'


search_label = LabelFrame(
    main_window, 
    text=text_str ,
    bg = '#AB8CE4', 
    font = ('Cooper', '15')
    )

search_label.grid(row=1, columnspan=2, sticky=NSEW, padx=35, pady= 20)
#

search_variable = StringVar()
search_choice = Entry(search_label, text=wiki_data.input_string)
search_choice.grid(row=1, columnspan=2, sticky=NSEW, padx=25, pady= 15) 



def new_selection():
    
    wiki_inst.input_string = '{}'.format(suggested_choice_list.get(ANCHOR))
    #wiki_inst.wiki_page = suggested_choice_list.get(ANCHOR)

    
    suggested_page= str(wikipedia.search(wiki_inst.input_string, results = 1))
    suggested_page = wikipedia.page(suggested_page)
    new_summary = '{}'.format(((wikipedia.summary(suggested_page))[:450] + '...'))
    new_url = '{}'.format(suggested_page.url)
    wiki_summary_result.config(text=new_summary)
    wiki_link_result.config(text=new_url)
    x = 0
    row_count = 1
    for y in wikipedia.search(wiki_inst.input_string):

        suggested_choice_list.insert(row_count, y[:])

        x+=1
        row_count+=1


    new_word_definition = search_instance.definition(search_instance)
    definition_result.config(text=new_word_definition)
    synonym_result.config(text=search_instance.synonym(search_instance))

    current_string = '{}'.format(wiki_inst.input_string)
    text_str = 'enter search word:(current search:', current_string, ')'
    search_label.config(text=text_str)


def new_search():
    search_string = search_choice.get()

    wiki_inst.input_string = '{}'.format(search_string)
    search_instance.input_string = search_string

    
    suggested_page= str(wikipedia.search(wiki_inst.input_string, results = 1))
    suggested_page = wikipedia.page(suggested_page)
    new_summary = '{}'.format(((wikipedia.summary(suggested_page))[:450] + '...'))
    new_url = '{}'.format(suggested_page.url)
    wiki_summary_result.config(text=new_summary)
    wiki_link_result.config(text=new_url)
    x = 0
    row_count = 1
    for y in wikipedia.search(wiki_inst.input_string):

        suggested_choice_list.insert(row_count, y[:])

        x+=1
        row_count+=1


    new_word_definition = search_instance.definition(search_instance)
    definition_result.config(text=new_word_definition)
    synonym_result.config(text=search_instance.synonym(search_instance))
    antonym_result.config(text=search_instance.antonym(search_instance))

    current_string = '{}'.format(wiki_inst.input_string)
    text_str = 'enter search word:(current search:', current_string, ')'
    search_label.config(text=text_str)


search_new = Button(main_window, text= 'search input', command= new_search)
search_new.grid(row= 6, columnspan= 4 , padx= 40, pady=35)

 ###
   

wiki_output_frame = LabelFrame(
        main_window, 
        text= 'Search results from Wikipedia.com', 
        bg = 'light blue',
        font = ('bahnshrift', '15', 'italic bold'),
        relief='raised',
        bd=5
    )

wiki_output_frame.grid(row=4, columnspan=2, padx=35, pady= 20)

suggested_choice_label = LabelFrame(wiki_output_frame, text= 'Did you mean?:' , bg = 'grey')
suggested_choice_label.grid(row=2, columnspan=2, sticky=NSEW, padx=35, pady= 20)

Grid.rowconfigure(suggested_choice_label,0,weight=1)
Grid.columnconfigure(suggested_choice_label,0,weight=1)

suggested_choice_list = Listbox(suggested_choice_label,  selectmode= 'SINGLE', bg= '#DCF5F7' )
suggested_choice_list.grid(row = 1, columnspan = 3, sticky=NSEW, padx=35, pady= 20)

x = 0
row_count = 1
for y in wikipedia.search(wiki_inst.input_string):

    suggested_choice_list.insert(row_count, y[:])

    x+=1
    row_count+=1
   

wiki_summary_label = Label(wiki_output_frame, text='Wikepedia excerpt:', relief=RAISED, bd= 6, bg = '#BFC9CA')
wiki_summary_label.grid(row=0, column=0,  padx=45, pady= 30)



wiki_summary_result = Label(wiki_output_frame, text=(summary[:450] + '...'), relief=SUNKEN, wraplength=600, bd= 6, bg = '#DCF5F7')
wiki_summary_result.grid(row=0, column=1, sticky=NSEW, padx=35, pady= 20)


##

new_choice_button = Button(suggested_choice_label, activebackground='dark grey', text= 'search selection instead', command= new_selection)
new_choice_button.grid(row=2, columnspan=2, sticky=NSEW, padx=35, pady= 20)
##

## link to wikipedia page, needs work
def open_link(event):
    
    pass

wiki_link_label = Label(wiki_output_frame, text='Wikipedia page url: ', relief=RAISED, bd= 6, bg = '#BFC9CA')
wiki_link_label.grid(row=1, column=0)

wiki_link_result = Label(wiki_output_frame, text=url, relief=RAISED, bd= 4, bg= '#DCF5F7')
wiki_link_result.grid(row=1, column=1, sticky=NSEW, padx=20, pady=15)

wiki_link_result.bind('link', open_link)

##definition

dict_output_label = LabelFrame(
    main_window, 
    text= 'Dictionary results', 
    bg='#AB8CE4',
    font = ('bahnshrift', '15', 'italic bold'),
    relief='raised',
    bd=5
    )
dict_output_label.grid(row=5, columnspan=2)


definition_label = Label(
    dict_output_label,
    text='dictionary definition: ',
    relief=RAISED,
    bd= 6,
    bg = '#BFC9CA'
    )
definition_label.grid(row=1, column=0)

definition_result = Label(dict_output_label, text=word_definition, relief=RAISED, bd= 6, bg = '#F0DFF7')
definition_result.grid(row=1, column=1, sticky=NSEW, padx=35, pady= 20)
#synonym

synonym_label = Label(
    dict_output_label,
    text='synonyms or related terms(if found): ',
    relief=RAISED,
    bd= 6,
    bg = '#BFC9CA'
    )
synonym_label.grid(row=2, column=0, sticky=EW)


synonym_result = Label(dict_output_label, text=word_synonym, relief=RAISED, bd= 6, bg = '#F0DFF7')
synonym_result.grid(row=2, column=1, sticky=NSEW, padx=35, pady= 20)

#anonym

antonym_label = Label(
    dict_output_label,
    text='antonyms(if found): ',
    relief=RAISED,
    bd= 6,
    bg = '#BFC9CA'
    )
antonym_label.grid(row=3, column=0, sticky=EW)

antonym_result = Label(dict_output_label, text= word_antonym, relief=RAISED, bd= 6, bg = '#F0DFF7')
antonym_result.grid(row=3, column=1, sticky=EW, padx=35, pady= 20)

w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()


cwd = os.getcwd()
image_path = "{}\\Word_Wiki\\Word_Wiki\\source_images\\background.png".format(cwd)

image1 = Image.open(image_path)

sized_image = image1.resize((w, h), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(sized_image)


main_window.config(image= new_pic)






tk.mainloop()