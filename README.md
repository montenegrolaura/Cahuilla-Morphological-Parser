# Cahuilla-Morphological-Parser

This parser takes in a Cahuilla noun and extracts the morphological components and their glosses. Because Cahuilla is an agglutinative language, some nouns can be comprised of many smaller components. This is a toy parser that focuses on nominalizer nouns. These nouns have a root verb base and have one or more nominalizers affixed to the root verb that change the meaning to some sort of abstract or concrete noun. This parser will extract the root verb and separate the remaining word into the nominalizers and each of their meanings. 

# Example:
Input noun: kʷáʔisniʔil̃

Output: The definition is 'the writing'. 
        The root verb is 'kʷáʔisni' which means 'to write'. This verb is transitive. 
        The nominalizer is 'ʔil̃' which is a NMLZ.ABST and means 'verbal abstract noun'.

To run this code, clone the repository and run in Pycharm or your preferred IDE. The tests are found in the test folder. 
