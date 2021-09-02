{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "view-in-github"
   },
   "source": [
    "<a href=\"https://colab.research.google.com/github/unt-iialab/INFO5731_Spring2020/blob/master/Assignments/INFO5731_Assignment_One.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Ryk8D1Q4Wsrp"
   },
   "source": [
    "# **INFO5731 Assignment One**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "90_NR8c5XGWc"
   },
   "source": [
    "# Question 1\n",
    "\n",
    "(20 points). Write a Python program to generate 12 random numbers between 1 and 100. Sort the list of numbers in ascending order and print it out.Sort the list of numbers in descending order and print it out. Calculate the average for the group and print it out."

    import random
    value = list(range(1,100))
    results = random.sample(value, k=12)
    results.sort()
    print(results)

    results.sort(reverse=True)
    print(results)

    avg = sum(results)/12
    print(avg)
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "5QX6bJjGWXY9"
   },
   "outputs": [],
   "source": [
    "# Your code here\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "1F_PZdH9Sh49"
   },
   "source": [
    "# Question 2\n",
    "(25 points). Write a program that will do the following string formatting tasks:\n",
    "\n",
    "(1) Ask the user to enter two sentences.\n",
    "\n",
    "(2) Make each sentence into a list. Each element in the list should correspond to a word in the sentence. For example, if the sentence is \"Alas! Am I alive? This is my first python program\", the program should print out ['Alas, '!', 'Am', 'I', 'alive, '?', 'This', 'is', 'my', 'first', 'python', 'program'].\n",
    "\n",
    "(3) Compare the two sentences. Print out a list of words that occur in both sentences.\n",
    "\n",
    "(4) Remove any punctuation from the sentence and print it back out. It should remove at least the following characters, but it can remove more: period(“.”), comma (“,”), semicolon (“;”), and colon (“:”)\n",
    "\n",
    "(5) Count the number of vowels in the sentences. Print out each vowel and the number of times it appears in the sentences, such as: a:2, e:1, i:0, etc"

    import nltk
    nltk.download('punkt')
    sentence1 = input("Please enter sentences1: ")
    sentence2 = input("Please enter sentences2: ")

    from nltk.tokenize import word_tokenize
    print(word_tokenize(sentence1))
    print(word_tokenize(sentence2))

    from sklearn.feature_extraction.text import CountVectorizer
    s1 = sentence1.lower()
    s2 = sentence2.lower()
    s = [s1] + [s2]
    vect = CountVectorizer()
    vect.fit(s)
    print(format(vect.vocabulary_)) 

s1 = word_tokenize(sentence1)
s2 = word_tokenize(sentence2)
words_list=[]
for words in s1:
  if words in s2:
    words_list.append(words)
print(words_list)

    sentence1_no_punct = str.maketrans(",.!?:;",6*" ")
    print(sentence1.translate(sentence1_no_punct))
    sentence2_no_punct = str.maketrans(",.!?:;",6*" ")
    print(sentence2.translate(sentence2_no_punct))

    s1_lower = sentence1.lower()
    s2_lower = sentence2.lower()
    s_a_lower = s1_lower.count("a")+s2_lower.count("a")
    print("a: " + str(s_a_lower))
    s_e_lower = s1_lower.count("e")+s2_lower.count("e")
    print("e: " + str(s_e_lower))
    s_i_lower = s1_lower.count("i")+s2_lower.count("i")
    print("i: " + str(s_i_lower))
    s_o_lower = s1_lower.count("o")+s2_lower.count("o")
    print("o: " + str(s_o_lower))
    s_u_lower = s1_lower.count("u")+s2_lower.count("u")
    print("u: " + str(s_u_lower))
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Y0oOSlsOS0cq"
   },
   "outputs": [],
   "source": [
    "# Your code here\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "CmFoI4jDS9nx"
   },
   "source": [
    "# Question 3 \n",
    "\n",
    "(15 points). The formula that describes the volume V of a sphere with radius r is the following:\n",
    "\n",
    "$ V=\\frac{4}{3}\\ast\\ \\pi\\ast\\ r^3 $\n",
    "\n",
    "Write a program to calculate the value of V when r is in the range of 1–10. Output the result in the following format:\n",
    "\n",
    "\tr\tV\n",
    "\t1\t…\n",
    "\t2\t…\n",
    "\t3\t…\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "pEyqeioAT95b"
   },
   "outputs": [],
   "source": [
    "# Your code here\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "pMCr3l8tnu0j"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "z3tBE7E-Xn5X"
   },
   "source": [
    "# Question 4\n",
    "\n",
    "(40 points). In the field of Data Science, data is often formatted as a comma-delimited (CSV) file, where each line in a file corresponds to a field's value. Refer to Chapter 9 (p. 106) for more information on comma-delimited files. To answer this question, you will need to download the file [Assignment1_denton_housing.csv](https://github.com/unt-iialab/info5731-fall2021/blob/main/assignments/Assignment1_denton_housing.csv) included with this assignment. The file [Assignment1_denton_housing.csv](https://github.com/unt-iialab/info5731-fall2021/blob/main/assignments/Assignment1_denton_housing.csv) contains statistics about housing in the city of Denton from 2008 to 2014. Write a program to implement the following questions.\n",
    "\n",
    "(1) (10 pts) Calculate the difference in the number of Occupied Housing Units from year to year and print it. The difference must be calculated for the consecutive years such as 2008-2009, 2009-2010 etc. Finally, print the values in the ascending order.\n",
    "\n",
    "(2) (10 pts) For all the years, calculate the percentage of housing units which are vacant an occupied. Print the results in the following format:\n",
    "\n",
    "Year Vacant Housing Units Occupied Housing Units\n",
    "\n",
    "    2008  30%   70%                          \n",
    "\t2009 ----- -----\n",
    "\t2010 ----- -----\n",
    "    2011 ----- -----\n",
    "\t2012 ----- -----\n",
    "    2013 ----- -----\n",
    "\t2014 ----- -----\n",
    "  \n",
    "  \n",
    "\n",
    "(3) (10 pts) Calculate and print the valued and years in which the highest number of housing units were vacant and occupied. Print the results in the following format:  \n",
    "\n",
    "                              Year\tValue\n",
    "\tVacant Housing Units\t  -----   -----\n",
    "\tOccupied Housing Units\t-----   -----\n",
    "\n",
    "(4) (10 pts) Calculate the harmonic mean of the total housing units and print it out. You can find the information about harmonic mean here: https://ncalculators.com/statistics/harmonic-mean-calculator.htm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "lqGYuHBhcsRH"
   },
   "outputs": [],
   "source": [
    "# Your code here\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyOAjsNCkNulTpzgRQbHdy3f",
   "collapsed_sections": [],
   "include_colab_link": true,
   "name": "INFO5731_Assignment_One.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
