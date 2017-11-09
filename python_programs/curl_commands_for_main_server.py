REGISTRATION:
curl -i -X POST -d "email=joelcjohnson123@gmail.com" -d "password=123joel123" https://api.mt2414.in/v1/registrations

	Output: {"success":true, "message":"Verification Email Sent"}


AUTHENTICATION:
curl -i -X POST -d "username=joelcjohnson123@gmail.com" -d "password=123joel123" https://api.mt2414.in/v1/auth

	Output: {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8"}


KEYS:
curl -i -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" https://api.mt2414.in/v1/keys

	Output: {"id": "1cf02f3d5def4b8bbed9e6b453ca7904", "key": "e8aabf7c297a4a82b18d6cf869b4fbba"}


SOURCE:
curl -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" https://api.mt2414.in/v1/sources -d '{"language":"English", "version":"NIV", "content":["XGlkIE1BVCBVbmxvY2tlZCBMaXRlcmFsIEJpYmxlDQpcaWRlIFVURi04DQpcaCBNYXR0aGV3IA0KXHRvYzEgVGhlIEdvc3BlbCBBY2NvcmRpbmcgdG8gU3QuIE1hdHRoZXcNClx0b2MyIE1hdHRoZXcgDQpcdG9jMyBNYXQgDQpcbXQgVGhlIEdvc3BlbCBBY2NvcmRpbmcgdG8gU3QuIE1hdHRoZXcNClxjIDENClxwDQpcdiAxIFRoZSBib29rIG9mIHRoZSBnZW5lYWxvZ3kgb2YgSmVzdXMgQ2hyaXN0LCB0aGUgc29uIG9mIERhdmlkLCB0aGUgc29uIG9mIEFicmFoYW0uDQpcdiAyIEFicmFoYW0gd2FzIHRoZSBmYXRoZXIgb2YgSXNhYWMsIGFuZCBJc2FhYyB0aGUgZmF0aGVyIG9mIEphY29iLCBhbmQgSmFjb2IgdGhlIGZhdGhlciBvZiBKdWRhaCBhbmQgaGlzIGJyb3RoZXJzLCANClx2IDMgSnVkYWggdGhlIGZhdGhlciBvZiBQZXJleiBhbmQgWmVyYWggYnkgVGFtYXIsIFBlcmV6IHRoZSBmYXRoZXIgb2YgSGV6cm9uLCBIZXpyb24gdGhlIGZhdGhlciBvZiBSYW0sDQoNCg0K"]}'

	Output: {"success":true, "message":"New source added to database"}


GET AVAILABLE LANGUAGE:
curl -i -X POST -H "Authorization:1cf02f3d5def4b8bbed9e6b453ca7904:e8aabf7c297a4a82b18d6cf869b4fbba" https://api.mt2414.in/v1/get_languages

    Output : [["MAL", "NEW"], ["tam", "ULB"], ["HIN", "HIN"], ["English", "NIV"]]


GET AVAILABLE BOOKS:
 curl -i -X POST -H "Authorization:1cf02f3d5def4b8bbed9e6b453ca7904:e8aabf7c297a4a82b18d6cf869b4fbba" https://api.mt2414.in/v1/get_books -d '{"language":"English","version":"NIV"}'

    Output : [["MAT", "1"]]   ie; [book and revision_num]


AUTO_TOKENS:
curl -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" https://api.mt2414.in/v1/autotokens -d '{"language":"English", "version":"NIV", "revision":"1"}'

    Output : {"tokenwords": [{"msgid": "book", "msgstr": ""}, {"msgid": "to", "msgstr": ""}, {"msgid": "According", "msgstr": ""}, {"msgid": "and", "msgstr": ""}, {"msgid": "Zerah", "msgstr": ""}, {"msgid": "\\toc1", "msgstr": ""}, {"msgid": "The", "msgstr": ""}, {"msgid": "2", "msgstr": ""}, {"msgid": "\\ide", "msgstr": ""}, {"msgid": "Perez", "msgstr": ""}, {"msgid": "St", "msgstr": ""}, {"msgid": "father", "msgstr": ""}, {"msgid": "1", "msgstr": ""}, {"msgid": "Christ", "msgstr": ""}, {"msgid": "\\toc3", "msgstr": ""}, {"msgid": "was", "msgstr": ""}, {"msgid": "Bible", "msgstr": ""}, {"msgid": "son", "msgstr": ""}, {"msgid": "brothers", "msgstr": ""}, {"msgid": "Jesus", "msgstr": ""}, {"msgid": "by", "msgstr": ""}, {"msgid": "Matthew", "msgstr": ""}, {"msgid": "3", "msgstr": ""}, {"msgid": "Ram", "msgstr": ""}, {"msgid": "\\mt", "msgstr": ""}, {"msgid": "Isaac", "msgstr": ""}, {"msgid": "Gospel", "msgstr": ""}, {"msgid": "Tamar", "msgstr": ""}, {"msgid": "\\v", "msgstr": ""}, {"msgid": "\\h", "msgstr": ""}, {"msgid": "\\id", "msgstr": ""}, {"msgid": "MAT", "msgstr": ""}, {"msgid": "\\p", "msgstr": ""}, {"msgid": "David", "msgstr": ""}, {"msgid": "UTF8", "msgstr": ""}, {"msgid": "Abraham", "msgstr": ""}, {"msgid": "his", "msgstr": ""}, {"msgid": "of", "msgstr": ""}, {"msgid": "Mat", "msgstr": ""}, {"msgid": "Unlocked", "msgstr": ""}, {"msgid": "\\toc2", "msgstr": ""}, {"msgid": "Hezron", "msgstr": ""}, {"msgid": "Jacob", "msgstr": ""}, {"msgid": "\\c", "msgstr": ""}, {"msgid": "Literal", "msgstr": ""}, {"msgid": "Judah", "msgstr": ""}, {"msgid": "genealogy", "msgstr": ""}, {"msgid": "the", "msgstr": ""}]}


UPLOAD_TOKEN_TRANSLATION:
curl -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" https://api.mt2414.in/v1/uploadtokentranslation -d '{"language":"English", "version":"KJV", "revision":"1","targetlang":"j","tokenwords":{"book":"jn","to":"lm","Accordin":"pp","and":"qq","Zerah":"ww","\\toc1":"","The":"rr","2":"","\\ide":"","Perez":"ii","St":"ok","father":"pp","1":"","Christ":"hh","\\toc3":"","was": "dd","Bible": "cv","son": "zx","brothers":"vd","Jesus": "bg","by":"ds","Matthew":"hf","3":"","Ram": "adxdg","\\mt":"","Isaac": "jolt","Gospel": "hgkjsgx","Tamar":"rectk","\\v": "","\\h": "","\\id":""}}'

    Output : '{"success":true, "message":"Token translations have been updated."}'



GENERATE_CONCORDANCE:
curl -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" httpS://api.mt2414.in/v1/generateconcordance -d '{"language":"English", "version":"NIV"}'

    Output : {"success":true, "message":"concordances created and stored in DB"}


GET/DOWNLOAD_CONCORDANCE:
curl -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" https://api.mt2414.in/v1/getconcordance -d '{"language":"English", "version":"NIV", "revision":"1", "token":"Abraham"}'

    Output : {"MAT - 1:1": "The book of the genealogy of Jesus Christ, the son of David, the son of Abraham.", "MAT - 1:2": "Abraham was the father of Isaac, and Isaac the father of Jacob, and Jacob the father of Judah and his brothers, "}


TRANSLATION:
curl -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" https://api.mt2414.in/v1/translations -d '{"sourcelang":"English", "version":"KJV", "targetlang":"j","revision":"1"}}'


LATEST API'S
curl -i -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MDE2NTM1MDEsInJvbGUiOiJtZW1iZXIiLCJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.0-jg_DXFe0S8AWKW0h4KkW-Biod9FZfJumrEkNVa-kM" https://api.mt2414.in/v1/tokenlist -d '{"sourcelang":"ori","version":"GL-ORYA-NT","revision":"1","targetlang" :"peg"}'
