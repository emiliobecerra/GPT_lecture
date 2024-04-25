# read csv file from dataset.csv

import pandas

data = pandas.read_csv('dataset.csv')

from dotenv import load_dotenv

#For openai's package 
load_dotenv()

from openai import OpenAI
client = OpenAI()

def simple_call(prompt):
	completions = client.chat.completions.create(model = "gpt-3.5-turbo", 
		messages=[
	#System role, adding context for the question
	#{"role": "system", "content": "You are a helpful assistant"},
	#Not including the system role will assume the gpt is your assistant
		{"role": "user", "content": prompt},
		], max_tokens=200
	# temperature how creative it is, but higher temperature results in really creative begining content, but incomprehensible words later. 
		, temperature=0.1
	#top_p: from the highest probability of a word to a lower probability, top_p will restrict to certain words depending on the probability threshold. Default is 1
		, top_p=1

		)
	return completions.choices[0].message.content

#lambda specifies a function
dataset['positive'] = dataset['reviewtext'].apply(lambda x: simple_call("On a scale of 1 to 10, how positive is the following review for a programmer: \"" + x + "\" Answer in one number"))
dataset['professional'] = dataset['reviewtext'].apply(lambda x: simple_call("On a scale of 1 t0 10, how professional is the reviewer who wrote the following review: \"" + x + "\" Answer in one number"))
dataset['emotional'] = dataset['reviewtext'].apply(lambda x: simple_call("On a scale of 1 to 10, how emotional is the reviewer who wrote the following review: \"" + x + "\" Answer in one number"))
dataset['sarcastic'] = dataset['reviewtext'].apply(lambda x: simple_call("On a scale of 1 to 10, how sarcastic is the reviewer who wrote the following review: \"" + x + "\" Answer in one number"))


dataset.to_csv('dataset_processed.csv')
print(result)