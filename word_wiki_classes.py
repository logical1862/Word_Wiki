import wikipedia
import requests
import json

class word_data():
    count = 0
    input_string = 'apple'


    def __init__(self):
        word_data.count = self.count +1 
        word_data.input_string = 'apple'
        


    def definition(self):
        url = 'https://twinword-word-graph-dictionary.p.rapidapi.com/association/'

        params= {'entry':word_data.input_string}

        headers = {
            'x-rapidapi-key': "8c3d0e9c3bmsh56f764e5cd7882dp180713jsn83a8fc337498",
            'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com"
                }



        definition = requests.request("GET", url, headers=headers, params=params)
        definition = definition.json()

        return definition['meaning']


    def synonym(self):
        url = 'https://twinword-word-graph-dictionary.p.rapidapi.com/definition/'

        params= {'entry':word_data.input_string}

        headers = {
            'x-rapidapi-key': "8c3d0e9c3bmsh56f764e5cd7882dp180713jsn83a8fc337498",
            'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com"
                }



        synonym = requests.request("GET", url, headers=headers, params=params)
        synonym = synonym.json()

        return synonym['assoc_word']
        

    def antonym(self):
        output = (word_data.input_string + ': *antonyms*')
        return output




class wiki_data():
    

    def __init__(self):
    
        pass

    def get_wiki_data(self, input_string):
        wiki_data.wiki_page = wikipedia.WikipediaPage(title= input_string)

        wiki_data.link = wiki_data.wiki_page.html()#for graphic preview on GUI

        wiki_data.wiki_excerpt = wiki_data.wiki_page.summary
        
        wiki_data.wiki_URL = wiki_data.wiki_page.url



    def get_wiki_link(self, input_string):

        #link_string = 

        #wiki_data.link  = 
        pass