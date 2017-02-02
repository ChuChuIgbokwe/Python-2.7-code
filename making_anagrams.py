#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 12, 2016 by 2:28 PM

# def number_needed(a,b):
#     '''
#     Given two strings,  and , that may or may not be of the same length, determine the minimum number of character
#     deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.
#     '''
#
#     common_letters = [i for i in a if i in b]
#     print len(common_letters)
#     # print len(a),len(b)
#     no_needed = abs(len(a) + len(b) - 2 * len(common_letters))
#     return no_needed

# print number_needed('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke')
# print number_needed('zjadbkhmquvpcedlhsarcjzfsnekawczfccjomvfirwkvbveuvvwgwdbkklmgnlorpxgdunmnjwkksoepjdwiixssigbytppioxoikcwtyggsvmigrgoadisnovlhkdsacgjpkhiinqdkdnruvhwyqrngmbozgiziqkxarikfyprdciazswxinnqaogzuoaeglcgcmrjmibqnlqmfmkpczgcnmdjddnjorqtfjesthkgvataofqqewutizendrxtlpoqatktauavwtylyodekaxuzbieuhyhwoayhkrkhrhdmfqmtwqfwpcxsmcntcwrqwpajikqctvobmduivcgleddqfslhreyntaydkqffmwgazdkuhqhltndbfqkyukmpkmswdycrukrvnbpurxhmkmprcaqykenvsgtvgvocgfxvgmqzlzoxmdrofjnqncnfkgdqersmzrhhgzhrzxrlcibirqagtnndvswbkqnlivsoubhvyygdgilzylftatxxlvzxloktldjierdfpkkyuvzuifokanhniinvzxrkcasjrwojiajcvkwfpmprzyhjjwfitwswylfqjvbrvmvswtxogohhmorvkydgwyeullmuipndbixybwojkvrwmkuykxegxicivpedergizfidbwmlrdkfpeezdihbtklobqsfhapjixmjtyxnehsvlyvqjcrcodsptmxcnmlxkxgfydsemnzxlwquzjypmrfhfcmuoxraxygvdyzqnapzxfvypundnsnswznnyenvetqiurahspirxepoacrpxghvfwigdwbjrurlntthldyihnyjqpypygkfevljrntkjmwwgreruebesznkqmzouluagfkzudkfpgexziotorxgqlqjzrxtdttlbdlxivdydhvcrmxffvmwiehjyecbyxobdzylwblzkjdbxbhcyvaibhrzovcosrpxsnlppwqzhudgxmjvjldktumhpqvjhkhczstqqjqafvgchrxsdccyyqfnhczqogsnalesxwsctbfaueuxjwxhpevwguowcjkewqwtorwhsdjojdmsbjasqxowtftvofzkxxenocuihfxqilllwnemkujdzeaplbckygxnktxtyulifwvcjzotwzyxdapqbrcazzpjsmcsjncomyqvzhrvgrvmsketbhvagklbznvicyyqwpmvyftewosqyxkzefzmsmntbjddhbwfskaqptxnhpehmqgqvhdptskubnakpwpjisaxlzmvoqcbglreuwvqpgmsvofkmuwumytaxgxlybmhmgljeibvonoketwqpunesggpmddleputxhcepfzgsnsyiqpalcgdimvxpykvpeoplstcxsiqiaostfsejyjukgrbgdxwhlnuggwdahvijmbcrvidwuxgaqkhtjfcuswaaugadbjnnmrhhakduhmwxydqhkudcsgemmfsnqfbcyilaspwbdtybyqkjknnctsqfxitnpwrqgcqatnbwibzgtlpfzfjsxzawkvlbrcrxekzaxayhdynwjfdkkmfjlffxasbtussaeradtzkyzywkdzxplcywjfwlxxetryvwrwzmxkkykgkpfheqjcoshmfgjlzdjuzasaormypwealljpdttsncgtiqgjtqgusyuhsjhjfojtzvkdoexdidyrvfcqxikpjhydqgmxuyqvtdyjhxmrdnkyunprxbiikhlapyajwsepvfaeemwhbgivvzotaxbngnpvnpgjimafrakyoifsonnkoefrbgehvteilktvwvaqvkomuvejltvzxcqykwhisnqdzmywhyoflerfbxqmqnoorgocdykvlcaloyjyyzdlfwtgtltlzhbsnqusqgpdjpqzpbxqacbfyumtghfhqgzfywyqcpunfknwommorqwrmknutsdjadobbmrfeltlyihmwwcnmahakuvdoyooddrerjkvwfgwnoijmnza','ngaacvfquugxxyeqjomftsciimruzswpaxrcswuosbmpbqgkgupbmtjxgcthvqwxnnchmwwexkwyaeiiyajmtujzwfjtvfrkvtrhrplpzjpbnajlauavojxlogglnzviuprmefbeosfcsrpulpqabnnrttdivarpribwnecexjgraxmoneqqrfhmymutnnlgymcnrgrqszhuxvimzacsflggybznqmtozycseviwvrrspbgqcijhtpntspgjbazcyduczebuyuonvudxcofxeuryjxhlzjpxmkcloffoztduphstvzrbvkafjjsjshihtkskpayovclllfeigxkbhmgrxacskkzdvtnmtmdpqocbtgjzevaljjehlgzvrazotmcnafeqtgroodpsaqgkbmtmtuimujcpvecykiofoiudnlxnbdzesutlodzkmdajhehtnwbdgxitiggmliqdclqtordaudmektxxryazxjsgrbsejkilwaeksknopbszuqwoqznqkiwdjohsarfwsmhmwwanxtntlljdmztwhpbqfjkgapeudngzjhnicccnnnsammyvdalljxtlnxgqloswxhfzjjoyyjylvzgabunmrgxggfztwrptawvjhljguktrjbskxhwrovxwdypzpeurdpckbmsxwnpfpjroqpfgkdcnbtotajmdyppbbkzxxqeozxdrmiayneorycmynydonspqcqpcitqhstbeebftftkdxydlxgzmzqddjufroybitcnxfurmndsmcvzbcandrsganotdmulhyaffuysjdkyffxgjywmpqvrdlmizhwghwnntnherrcyyahkydypvvibgujhdfonedazrjdkagiagpkgulvqgfrnbcufkksoqunhdqrfybheruklfhdlowaqzxxjjpzzloiqgbxfdglwayjhhnvwjxokwlvgcwhnksftvcaaklwlliutvrrgpftlqotsldhxxmqsq')
# print number_needed('bugexikjevtubidpulaelsbcqlupwetzyzdvjphn','lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk')

# def number_needed(a,b):
#     common_letters = sum (a[i] != b[i] for i in range(len(a)))
#     print common_letters
#
#     print len(a),len(b)
#     no_needed = abs(len(a) - common_letters + len(b))
#     return no_needed

# print number_needed('bugexikjevtubidpulaelsbcqlupwetzyzdvjphn','lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk')
# print number_needed('cde','abc')

# def number_needed(a,b):
#     count = 0
#     n = 0
#     for i in a:
#         temp = b.count(i)
#         if temp == 0:
#             n+=1
#         if temp !=1 or temp !=0:
#             temp = 1
#         count += temp
#     print len(a),len(b)
#     print n
#     #     if i in b:
#     #         count += b.count(i)
#     # print count
#     return len(a)+ len(b) - count



# def number_needed(a,b):
#     common = []
#     for i in b:
#         if i not in a:
#             common.append(i)
#     return common

#  a = abbaa
#  b = aacdabz
#  a2 = cdb
#  b2 = dab
# def set_to_dict(m_set, m_str):
#     m_dict = {}
#     for c in m_set:
#         m_dict[c]=m_str.count(c)
#     return m_dict
#
# def compare_dict(m_dict1, m_dict2):
#     compare_sum = 0
#
#     for key,value in m_dict1.items():
#         if key in m_dict2:
#             compare_sum += abs(value - m_dict2[key])
#             del(m_dict2[key])
#         else:
#             compare_sum += value
#     return compare_sum
#
# def number_needed(a, b):
#     set_a, set_b = set(a), set(b)
#     dict_a = set_to_dict(set_a, a)
#     dict_b = set_to_dict(set_b, b)
#
#     m_sum = compare_dict(dict_b, dict_a)
#     m_sum += compare_dict(dict_a, dict_b)
#     return m_sum
import string
def number_needed(a,b):
    count = 0
    # initialize a library from a - z with an empty as as a key for each letter
    my_dict = dict.fromkeys(string.ascii_lowercase, [])
    for c in string.ascii_lowercase:
        if c in a and c in b: #check for occurences of letters in both strings
        # populate the values of each dictionary key with the counts of  each letter in a list
            my_dict[c] = [a.count(c),b.count(c)]
        elif c in a and c not in b:
            my_dict[c] = [a.count(c), 0]
        else:
            my_dict[c] = [0, b.count(c)]
    for c in string.ascii_lowercase:
        count += abs(my_dict[c][1] - my_dict[c][0])
    return count

# print(number_needed(a, b))


# print number_needed('fsqoiaidfaukvngpsugszsnseskicpejjvytviya','ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget')
# print number_needed('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke')
# print number_needed('tttttttttttttttttttttttttttttttttttttsssssssssssssssss','sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss' )
print number_needed('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke')