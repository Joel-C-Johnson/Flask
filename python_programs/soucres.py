"""
@app.route("/v1/sources", methods=["POST"])
@check_token
def sources():
    req = request.get_json(True)
    language = req["language"]
    content = req["content"]
    version = req["version"]
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("SELECT s.id, st.book_name, st.content, st.revision_num  from sources s LEFT JOIN sourcetexts st ON st.source_id = s.id WHERE s.language = %s and s.version = %s",(language, version))
    try:
        rst = cursor.fetchall()
    except:
        pass
    changes = []
    source_id = rst[0][0]
    if source_id:
        books = []
        all_books =cursor.fetchall()
        for i in range(0, len(all_books)):
            books.append(all_books[i][1])
        for files in content:
            text_file = ((base64.b64decode(files)).decode('utf-8')).replace('\r','')
            book_name = (re.search('(?<=\id )\w+', text_file)).group(0)
            if book_name in books:
                count = 0
                count1 = 0
                for i in range(0, len(all_books)):
                    if all_books[i][1] != text_file and book_name == all_books[i][0]:
                        count = count + 1
                    elif all_books[i][1] == text_file and book_name == all_books[i][0]:
                        count1 = all_books[i][2]
                if count1 == 0 and count != 0:
                    revision_num = count + 1
                    cursor.execute("INSERT INTO sourcetexts (book_name, content, source_id, revision_num) VALUES (%s, %s, %s, %s)", (book_name, text_file, source_id, revision_num))
                    changes.append(book_name)
                    remove_punct = re.sub(r'([!"#$%&\\\'\(\)\*\+,-\.\/:;<=>\?\@\[\]^_`{|\}~।0123456789])','', text_file)
                    token_list = nltk.word_tokenize(remove_punct)
                    token_set = set([x.encode('utf-8') for x in token_list])
                    words = []
                    for t in token_set:
                        words.append(t.decode("utf-8"))
                        cursor.execute("SELECT token FROM autogeneratedtokens WHERE token = %s AND source_id = %s AND revision_num = %s", (t.decode("utf-8"), source_id, str(revision_num)))
                        if not cursor.fetchone():
                            cursor.execute("INSERT INTO autogeneratedtokens (token, revision_num, source_id) VALUES (%s, %s, %s)", (t.decode("utf-8"), revision_num, source_id))
                            cursor.execute("INSERT INTO clusters (book_name, token, revision_num, source_id) VALUES (%s,%s,%s,%s)",(book_name,t.decode("utf-8"),revision_num,source_id))
            elif book_name not in books:
                revision_num = 1
                cursor.execute("INSERT INTO sourcetexts (book_name, content, source_id, revision_num) VALUES (%s, %s, %s, %s)", (book_name, text_file, source_id, revision_num))
                changes.append(book_name)
                remove_punct = re.sub(r'([!"#$%&\\\'\(\)\*\+,-\.\/:;<=>\?\@\[\]^_`{|\}~।0123456789])','', text_file)
                token_list = nltk.word_tokenize(remove_punct)
                token_set = set([x.encode('utf-8') for x in token_list])
                words = []
                for t in token_set:
                    words.append(t.decode("utf-8"))
                    cursor.execute("SELECT token FROM autogeneratedtokens WHERE token = %s AND source_id = %s AND revision_num = %s", (t.decode("utf-8"), source_id, str(revision_num)))
                    if not cursor.fetchone():
                        cursor.execute("INSERT INTO autogeneratedtokens (token, revision_num, source_id) VALUES (%s, %s, %s)", (t.decode("utf-8"), revision_num, source_id))
                        cursor.execute("INSERT INTO clusters (book_name, token, revision_num, source_id) VALUES (%s,%s,%s,%s)",(book_name,t.decode("utf-8"),revision_num,source_id))
        cursor.close()
        connection.commit()
        if changes:
            return '{"success":true, "message":"Existing source, token and concordance are updated"}'
        else:
            return '{"success":false, "message":"No Changes. Existing source, toknes and concordance are already up-to-date."}'
    else:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO sources (language, version) VALUES (%s , %s) RETURNING id", (language, version))
        source_id = cursor.fetchone()[0]
        for files in content:
            text_file = ((base64.b64decode(files)).decode('utf-8')).replace('\r','')
            book_name = (re.search('(?<=\id )\w+', text_file)).group(0)
            revision_num = 1
            cursor.execute("INSERT INTO sourcetexts (book_name, content, revision_num, source_id) VALUES (%s, %s, %s, %s)", (book_name, text_file, revision_num, source_id))
            remove_punct = re.sub(r'([!"#$%&\\\'\(\)\*\+,-\.\/:;<=>\?\@\[\]^_`{|\}~।0123456789])','', text_file)
            token_list = nltk.word_tokenize(remove_punct)
            token_set = set([x.encode('utf-8') for x in token_list])
            words = []
            for t in token_set:
                words.append(t.decode("utf-8"))
                cursor.execute("INSERT INTO autogeneratedtokens (token, revision_num, source_id) VALUES (%s, %s, %s)", (t.decode("utf-8"), revision_num, source_id))
                cursor.execute("INSERT INTO clusters (book_name, token, revision_num, source_id) VALUES (%s,%s,%s,%s)",(book_name,t.decode("utf-8"),revision_num,source_id))
        cursor.close()
        connection.commit()
        return '{"success":true, "message":"New source, tokens, and concordance are added to database"}'
"""



@app.route("/v1/getbookwiseautotokens", methods=["POST"])
@check_token
def bookwiseagt():
    req = request.get_json(True)
    sourcelang = req["sourcelang"]
    version = req["version"]
    revision = req["revision"]
    books = req["books"]
    notbooks = req["nbooks"]
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM sources WHERE language = %s AND version = %s",(sourcelang, version))
    try:
        source_id = cursor.fetchone()[0]
    except:
        return '{"success":false, "message":"Source is not available. Upload source."}'
    toknwords = []
    ntoknwords = []
    if books and not notbooks:
        for bkn in books:
            cursor.execute("SELECT token FROM clusters WHERE book_name = %s",(bkn,))
            tokens = cursor.fetchall()
            for t in tokens:
                toknwords.append(t[0])
        stoknwords = set(toknwords)
        cursor.close()
        return json.dumps(list(stoknwords))
    elif books and notbooks:
        for bkn in books:
            cursor.execute("SELECT token FROM clusters WHERE book_name = %s",(bkn,))
            tokens = cursor.fetchall()
            for t in tokens:
                toknwords.append(t[0])
        for nbkn in notbooks:
            cursor.execute("SELECT token FROM clusters WHERE book_name = %s",(nbkn,))
            tokens = cursor.fetchall()
            for t in tokens:
                ntoknwords.append(t[0])
        stoknwords = set(ntoknwords) -  set(toknwords)
        cursor.close()
        return json.dumps(list(stoknwords))
