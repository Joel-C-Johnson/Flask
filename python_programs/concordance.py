import nltk

def get_all_phrases_containing_tar_wrd(target_word, tar_passage, left_margin = 10, right_margin = 10):
    ## Create list of tokens using nltk function
    tokens = nltk.word_tokenize(tar_passage)

    ## Create the text of tokens
    text = nltk.Text(tokens)

    ## Collect all the index or offset position of the target word
    c = nltk.ConcordanceIndex(text.tokens, key = lambda s: s.lower())

    ## Collect the range of the words that is within the target word by using text.tokens[start;end].
    ## The map function is use so that when the offset position - the target range < 0, it will be default to zero
    concordance_txt = ([text.tokens[map(lambda x: x-5 if (x-left_margin)>0 else 0,[offset])[0]:offset+right_margin]
                        for offset in c.offsets(target_word)])

    ## join the sentences for each of the target phrase and return it
    return [''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]

# Test the function

# sample text from http://www.shol.com/agita/pigs.htm
raw  = """The little pig saw the wolf climb up on the roof and lit a roaring fire in the fireplace and placed on it a large kettle of water.When the wolf finally found the hole in the chimney he crawled down and KERSPLASH right into that kettle of water and that was the end of his troubles with the big bad wolf."""

tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
text.concordance('wolf') # default text.concordance output

results = get_all_phrases_containing_tar_wrd('wolf', raw)

for result in results:
    print result












if not source_id:
    return '{"success":false, "message":"Source is not available. Upload it"}'
else:
    cursor.execute("SELECT book_name, concordances FROM concordance WHERE token = %s AND source_id = %s AND revision_num = %s", (token, source_id[0], str(revision)))
    concord = cursor.fetchall()
    if not concord:
        return '{"success":false, "message":"Token is not available"}'
    con = [["TOKEN","REFRENCE","VERSE"]]
    for i in range(0, len(concord)):
        book = concord[i][0]
        concordances = concord[i][1]
        con.append((token,book,concordances))
    cursor.close()
    sheet = pyexcel.Sheet(con)
    output = flask.make_response(sheet.xlsx)
    output.headers["Content-Disposition"] = "attachment; filename = con.xlsx"
    output.headers["Content-type"] = "xlsx"
    # logging.warning('User:\'' + str(email_id) + '\'. Downloaded tokens from book/books ' + ", ".join(include_books) + '. Source ID:' + str(source_id[0]) + '. Revision:' + str(revision))
    return output
    # return json.dumps(con)
