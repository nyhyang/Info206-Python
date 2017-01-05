###
###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
##/

from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep

import re

WORD_RE = re.compile(r"[\w']+")


class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper1_extract_user_word(self,_,record):
        """Taken a record, yield <user_id, business_id>"""
        for word in WORD_RE.findall(record['text']):
            yield [ record['user_id'], word.lower()]

    def reducer1_compile_word_under_user(self,user_id,words):
        ###
        # TODO_1: compile businesses as a list of array under given user_id,after 
        # remove duplicate business, yield <user_id, [business_ids]>
        ##/
        unique_word = set(words) 
        unique_wordlst = list(unique_word)
        yield [user_id, unique_wordlst]


    def mapper2_collect_word_under_user(self, user_id, words):
        ###
        # TODO_2: collect all <user_id, business_ids> pair, 
        # map into the same Keyword LIST,
        # yield <'LIST',[user_id, [business_ids]]>
        ##/
        yield ["LIST", [user_id, words]]

    def reducer2_calculate_similarity(self,stat,user_words):
        def Jaccard_similarity(wordlist1, wordlist2):
            ###
            # TODO_3: Implement Jaccard Similarity here, 
            # output score should between 0 to 1
            ##/
            wordset1 = set(wordlist1)
            wordset2 = set(wordlist2)

            unionset = wordset1.union(wordset2)
            intersectionset = wordset1.intersection(wordset2)

            similarity_score = len(intersectionset)/len(unionset)
            return similarity_score

        ###
        # TODO_4: Calulate Jaccard, 
        # output the pair users that have similarity over 0.5, 
        # yield <[user1,user2], similarity>
        ##/
        user_wordlist1 = list(user_words)

        for x in range(len(user_wordlist1)):
            for y in range(x+1, len(user_wordlist1)):
                similarity_score = Jaccard_similarity(user_wordlist1[x][1],user_wordlist1[y][1])           
                if similarity_score >= 0.5:
                    user1 = user_wordlist1[x][0]
                    user2 = user_wordlist1[y][0]

                    yield [[user1, user2], similarity_score]


    def steps(self):
        return [
            MRStep(mapper=self.mapper1_extract_user_word, reducer=self.reducer1_compile_word_under_user),
            MRStep(mapper=self.mapper2_collect_word_under_user, reducer= self.reducer2_calculate_similarity)
        ]


if __name__ == '__main__':
    UserSimilarity.run()
