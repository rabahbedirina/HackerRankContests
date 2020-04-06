import string as st


def designerPdfViewer(h, word):
    letter = list(st.ascii_lowercase)
    dic = dict(zip(letter, h))
    area = max([dic[l] for l in word])*len(word)
    return area


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
print(designerPdfViewer(h, word))
