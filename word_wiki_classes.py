


import wikipedia
import requests
import json

class word_data():
    count = 0
    input_string = 'apple'


    def __init__(self):
        word_data.count = self.count +1 
        
        


    def definition(self):
        url = 'https://twinword-word-graph-dictionary.p.rapidapi.com/definition/'

        params= {'entry':word_data.input_string}

        headers = {
            'x-rapidapi-key': "8c3d0e9c3bmsh56f764e5cd7882dp180713jsn83a8fc337498",
            'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com"
                }



        definition = requests.request("GET", url, headers=headers, params=params)
        definition = definition.json()
        noun = definition['meaning']['noun'][1:]
        verb = definition['meaning']['verb']
        adverb = definition['meaning']['adverb']
        adjective = definition['meaning']['adjective']

        output = ('Nouns = : ', noun, '\n', 'Verbs = : ', verb, '\n', 'Adverbs = : ', adverb, '\n', 'Adjectives = : ', adjective)

        return output


    def synonym(self):
        url = 'https://twinword-word-graph-dictionary.p.rapidapi.com/reference/'

        params= {'entry':word_data.input_string}

        headers = {
            'x-rapidapi-key': "8c3d0e9c3bmsh56f764e5cd7882dp180713jsn83a8fc337498",
            'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com"
                }



        synonym = requests.request("GET", url, headers=headers, params=params)
        synonym = synonym.json()

        return synonym['relation']['synonyms']
        

    def antonym(self):

        url = "https://languagetools.p.rapidapi.com/antonyms/{}".format(word_data.input_string)

        headers = {
        'x-rapidapi-host': "languagetools.p.rapidapi.com",
        'x-rapidapi-key': "08754af8e3mshfe2705eb50fda80p1cc781jsn0ae2c4511afc"
                }

        output = requests.request("GET", url, headers=headers)

        output = output.json()       
        return output["antonyms"]




class wiki_data():
    input_string = 'apple'
    results = wikipedia.search(input_string, results = 15)
    suggested_results = results[0]
    wiki_page = wikipedia.page(suggested_results)
    summary = wikipedia.summary(suggested_results)
    
    wiki_url = wiki_page.url

    def __init__(self):
        results = wikipedia.search(wiki_data.input_string, results = 15)
        wiki_data.search_result = results
        suggested_results = results[0]
        wiki_data.input_string = suggested_results
        
        wiki_data.wiki_page = wikipedia.page(suggested_results)
        wiki_data.summary = wiki_data.wiki_page.summary
        wiki_data.wiki_url = wiki_data.wiki_page.url
        #wiki_data.search_choice = []
    
        

    def search_result(self):
        results = wikipedia.search(wiki_data.input_string, results = 15)
        wiki_data.search_result = results
        return results

        

    def wiki_url(self):
        try:
            page = wiki_data.wiki_page
            url = page.url
            

            wiki_data.wiki_url = url

        except:
            wiki_data.input_string = wikipedia.search(wiki_data.input_string, results= 1)
            wiki_data.wiki_page = wikipedia.page(wiki_data.input_string, auto_suggest=False)
            
            

            wiki_data.wiki_url = wiki_data.wiki_page.url

        return wiki_data.wiki_url
