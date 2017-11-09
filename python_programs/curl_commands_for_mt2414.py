REGISTRATION:
curl -i -X POST -d "email=joelcjohnson123@gmail.com" -d "password=123joel123" http://127.0.0.1:8000/v1/registrations

	Output: Verification email sent




AUTHENTICATION
curl -i -X POST -d "username=joelcjohnson123@gmail.com" -d "password=123joel123" http://127.0.0.1:8000/v1/auth

	Output: {"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.VwJyuxwIFMhHUJ5VamMli_WQUh23pGZDP8XTlxjk4og"}

   NEW	Output: {access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.COwWImiHEmy3TaNvP_GiBnvQgFsXVAn_CdaanBL1iKI"}



KEYS
curl -i -X POST -H "Authorization:bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.VwJyuxwIFMhHUJ5VamMli_WQUh23pGZDP8XTlxjk4og" http://127.0.0.1:8000/v1/keys

	Output: {"id": "0b911c2107e14dab9f6dee84ddea8295", "key": "6d1305553cfa410e8958e91f301fe404"}

	New Output: {"id": "acbf2c6fe88a4d918c26f670b2b91802", "key": "40e188f7edba47c98abf10a8e7062aae"}




SOURCE
curl -i -H "Authorization:edceb3db5bdc40fcba156e9a821adbd7:24b9ec98942444fa8e24981817e15193" http://127.0.0.1:8000/v1/sources -d '{"language":"kan","content":{"AAA":"This is another test line"}}'

	Output: Completed Successfully

		  OR Acces Token

curl -i -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.COwWImiHEmy3TaNvP_GiBnvQgFsXVAn_CdaanBL1iKI" http://127.0.0.1:8000/v1/sources -d '{"language":"kan","content":{"AAA":"This is another test line"}}'

	Output: Completed Successfully


Sample  Language '{"language":"LKJ", "content":{"GEN":"\id GEN\n\c 1\n\p\n\v 1 In the beginning God created the heavens and the earth.\n\v 2 And the earth was without form and was void form.", "EXO":"\id EXO\n\c 1\n\p\n\v 1 Now these are the names of the children of Israel, which came to Egypt; every man and his household came with Jacob\n\v 2 Reuben, Simeon, Levi, and Judah", "LEV":"\id LEV\n\c 1\n\p\n\v 1 And the Lord called unto Moses, and spake unto him out of the tabernacle of the congregation, saying,\n\v 2 Speak unto the children of Israel"}}'





GET AVAILABLE LANGUAGE
curl -i -X POST -H "Authorization:acbf2c6fe88a4d918c26f670b2b91802:40e188f7edba47c98abf10a8e7062aae" http://127.0.0.1:8000/v1/get_languages




GET AVAILABLE BOOKS
 curl -i -X POST -H "Authorization:acbf2c6fe88a4d918c26f670b2b91802:40e188f7edba47c98abf10a8e7062aae" http://127.0.0.1:8000/v1/get_books -d '{"language":"English","version":"NIV"}'




TOKEN_WORDS
curl -H "Authorization:bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiaWpvYjg5QGdtYWlsLmNvbSJ9.RX_rx24v1uhzRv5FypR1X7QlyALUPvHSg1q6OUFtGos" http://127.0.0.1:8000/v1/tokenwords/kan

	Output:{"tokenwords": "[{'msgstr': '', 'msgid': 'test'}, {'msgstr': '', 'msgid': 'line'}, {'msgstr': '', 'msgid': 'is'}, {'msgstr': '', 'msgid': 'This'}, {'msgstr': '', 'msgid': 'another'}]"}


CLUSTER
curl -i -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.COwWImiHEmy3TaNvP_GiBnvQgFsXVAn_CdaanBL1iKI" http://127.0.0.1:8000/v1/getbookwiseautotokens -d '{"sourcelang":"LL","version":"JV","revision":"1","nbooks":["EXO"],"books":["LEV","GEN"]}'


TEST API
curl -i -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.COwWImiHEmy3TaNvP_GiBnvQgFsXVAn_CdaanBL1iKI" http://127.0.0.1:8000/v1/testapi -d '{"sourcelang":"eng","version":"ULB","revision":"1","targetlang":"tam"}'






To translate

curl -H "Authorization:bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiaWpvYjg5QGdtYWlsLmNvbSJ9.RX_rx24v1uhzRv5FypR1X7QlyALUPvHSg1q6OUFtGos" http://127.0.0.1:8000/v1/translations -d '{"sourcelang":"XYZ", "tokenwords": "[{'msgstr': 'Ni', 'msgid': 'In'}, {'msgstr': '\\c', 'msgid': '\\c'}, {'msgstr': '.', 'msgid': '.'}, {'msgstr': '\\id', 'msgid': '\\id'}, {'msgstr': 'GEN', 'msgid': 'GEN'}, {'msgstr': 'seavenh', 'msgid': 'heavens'}, {'msgstr': 'harte', 'msgid': 'earth'}, {'msgstr': 'tithow', 'msgid': 'without'}, {'msgstr': '1', 'msgid': '1'}, {'msgstr': 'God', 'msgid': 'God'}, {'msgstr': 'doiv', 'msgid': 'void'}, {'msgstr': '\\p', 'msgid': '\\p'}, {'msgstr': '\\v', 'msgid': '\\v'}, {'msgstr': 'saw', 'msgid': 'was'}, {'msgstr': 'dna', 'msgid': 'and'}, {'msgstr': 'dnA', 'msgid': 'And'}, {'msgstr': 'dreatec', 'msgid': 'created'}, {'msgstr': 'geginninb', 'msgid': 'beginning'}, {'msgstr': 'eht', 'msgid': 'the'}, {'msgstr': 'morf', 'msgid': 'form'}, {'msgstr': '2', 'msgid': '2'}]"}'


\

curl -X POST http://127.0.0.1:8000/v1/sources -d '{"language":"HHH", "content":{"GEN": "\id GEN\n\c 1\n\p\n\v 1 In the beginning God created the heavens and the earth.\n\v 2 And the earth was without form and was void form.", "EXO": "\id EXO\n\c 1\n\p\n\v 1 Now these are the names of the children of Israel, which came to Egypt; every man and his household came with Jacob\n\v 2 Reuben, Simeon, Levi, and Judah"}}' -H "Authorization:bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiaWpvYjg5QGdtYWlsLmNvbSJ9.RX_rx24v1uhzRv5FypR1X7QlyALUPvHSg1q6OUFtGos" {}
