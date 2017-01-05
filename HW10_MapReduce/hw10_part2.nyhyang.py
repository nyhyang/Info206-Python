###
###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
##/

from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper1_extract_user_business(self,_,record):
        """Taken a record, yield <user_id, business_id>"""
        yield [record['user_id'], record['business_id']]

    def reducer1_compile_businesses_under_user(self,user_id,business_ids):
        ###
        # TODO_1: compile businesses as a list of array under given user_id,after 
        # remove duplicate business, yield <user_id, [business_ids]>
        ##/
        unique_business = set(business_ids) 
        unique_bizlst = list(unique_business)
        yield [user_id, unique_bizlst]


    def mapper2_collect_businesses_under_user(self, user_id, business_ids):
        ###
        # TODO_2: collect all <user_id, business_ids> pair, 
        # map into the same Keyword LIST,
        # yield <'LIST',[user_id, [business_ids]]>
        ##/
        yield ["LIST", [user_id, business_ids]]

    def reducer2_calculate_similarity(self,stat,user_business_ids):
        def Jaccard_similarity(business_list1, business_list2):
            ###
            # TODO_3: Implement Jaccard Similarity here, 
            # output score should between 0 to 1
            ##/
            bizset1 = set(business_list1)
            bizset2 = set(business_list2)

            unionset = bizset1.union(bizset2)
            intersectionset = bizset1.intersection(bizset2)

            similarity_score = len(intersectionset)/len(unionset)
            return similarity_score

        ###
        # TODO_4: Calulate Jaccard, 
        # output the pair users that have similarity over 0.5, 
        # yield <[user1,user2], similarity>
        ##/
        user_bizlist1 = list(user_business_ids)

        for x in range(len(user_bizlist1)):
            for y in range(x+1, len(user_bizlist1)):
                similarity_score = Jaccard_similarity(user_bizlist1[x][1],user_bizlist1[y][1])           
                if similarity_score >= 0.5:
                    user1 = user_bizlist1[x][0]
                    user2 = user_bizlist1[y][0]

                    yield [[user1, user2], similarity_score]


    def steps(self):
        return [
            MRStep(mapper=self.mapper1_extract_user_business, reducer=self.reducer1_compile_businesses_under_user),
            MRStep(mapper=self.mapper2_collect_businesses_under_user, reducer= self.reducer2_calculate_similarity)
        ]


if __name__ == '__main__':
    UserSimilarity.run()
