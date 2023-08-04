#l:
#1st request
import pprint
from bs4 import BeautifulSoup
import requests
import textblob
API_KEY = "t4HanjsvMAhaQ375vn6MpE9gbuuAN2iZ"
URL = "https://api.nytimes.com/svc/movies/v2/reviews/search.json"
user_input = input("what(movie) do you want to search about ")
params = {"query":user_input,"api-key":API_KEY}
response = requests.get(URL, params)
number_results = response.json()["num_results"]
user_response_movie = -1
results = response.json()["results"]
sentiment = {'positive':0, 'negative': 0, 'subjective': 0, 'objective': 0}

# from request get the number of resuts and print them out/ if cant find anything about then exit() 
if number_results == 0:
    print("Unfortunately we can't find the movie you want. ")
    exit()
else:
    print(f"\fHere are {number_results} results related to {user_input} found for you")

#print tou all related resuts and ask the user to input one resut they would like to know more about/and get the link for review
results_titles = []
print(f"\tpublication date:\tmovie name:")
for index in range(number_results):
    print(f" {index+1}. \t {results[index]['publication_date']}\t\t{results[index]['display_title']}")
    results_titles.append(results[index]['display_title'])
user_input_movie_title = input("I found these, Which specific one are you looking for? \n").lower()
for index in results_titles:
    user_response_movie += 1
    if index.lower() == user_input_movie_title:
        print(f"You are searching for, the movie {index}.")
        movie_name = user_response_movie
        break
#print(results[user_response_movie]["link"]["url"])


#2nd request & output the review
def request_for_review():    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    response = requests.get(results[user_response_movie]["link"]["url"], headers=headers)
    response_html = response.text
    soup = BeautifulSoup(response_html,"html.parser")
    all_text = soup.findAll("p",attrs={"class":"css-at9mc1 evys1bk0"})
    for text in all_text:
        text_string = text.text
        print(f"\n{text_string}\n")
#output the summary
def request_for_preview():
    summary = results[movie_name]["summary_short"]
    rating = results[movie_name]["mpaa_rating"]
    print(f"\nmpaa rating: {rating}")
    abstract_sentiment = textblob.TextBlob(summary).sentiment
    if abstract_sentiment[0] < 0:
        sentiment['negative'] += 1
    else:
        sentiment['positive'] += 1
    if abstract_sentiment[1] <= 0.5:
        sentiment['objective'] += 1
    else:
        sentiment['subjective'] += 1
    
    if sentiment['positive'] == sentiment['negative']:
        print("This movie has a nutral sentiment storyline.")
    elif sentiment['positive'] < sentiment['negative']:
        print("This movie has a positive sentiment storyline.")
    else:
        print("This movie has a negative sentiment storyline.")
    print(f"\n{summary}\n")



#ask user summary pr review     
while True:
    user_input_sum_or_rev = input("1.preview/short summary\n2.review\n3.quit\nplease enter 1, 2, or 3:  ").lower() 
    if user_input_sum_or_rev == "1":
        request_for_preview()
    elif user_input_sum_or_rev == "2":
        request_for_review()
    elif user_input_sum_or_rev == "3":
        exit()