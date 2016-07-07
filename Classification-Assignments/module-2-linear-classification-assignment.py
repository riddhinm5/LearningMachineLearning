from __future__ import division
import graphlab
import math
import string

# Checking if all the imports were successful
print "#################"
print "all ready to run"
print "################"

# Importing the amazon reviews data
products = graphlab.SFrame('amazon_baby.gl/')

# print Length of Products Data set
print "##############"
print len(products)
print "##############"

# Testing imprt of amazon data
print "##############"
print products[234]
print "##############"

# Removing all punctuation from the review text
# Function to remove all punctuation
def remove_punctuation(text):
	import string
	return text.translate(None, string.punctuation)

reviews_without_punctuation = products['review'].apply(remove_punctuation)
products['word_count'] = graphlab.text_analytics.count_words(reviews_without_punctuation)

# Testing if creation of a word bag column worked
print "##############"
print products[234]['word_count']
print "##############"

# Removing all "nuetral" rating == 3 reviews from the data set
products = products[products['rating'] != 3]

# Testing removal of nuetral rating products
print "##############"
print len(products)
print "##############"

# Adding a base positive (rating > 3) and negative (rating < 3) "sentiment" value in the new products data set with no nuetral products
products['sentiment'] = products['rating'].apply(lambda rating: +1 if rating > 3 else -1)

# Test to see new sentiment column
print "##############"
print products
print "##############"

# Spliting products dataset into test and train
test_data, train_data = products.random_split(0.8, seed = 1)

# Testing split of data set
print "##############"
print len(test_data)
print "##############"
print len(train_data)
print "##############"

# Training an inbuilt sentiment classifier model using graphlab-create
print "##############"
sentiment_model = graphlab.logistic_classifier.create(train_data, 
														target = 'sentiment',
														features = ['word_count'],
														validation_set = None)
print "##############"

# checking output of sentiment model
print "##############"
print sentiment_model
print "##############"

# collecting the coefficients
weights = sentiment_model.coefficients

# Testing weights values
print "##############"
print weights.column_names()
print "##############"






