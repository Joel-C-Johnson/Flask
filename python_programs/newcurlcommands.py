SOURCE:

    curl -X POST -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.3TeFe67qtHfGH3t0-8Lrgw9Z5fLDIYax56ZNHhp7wV8" https://api.mt2414.in/v1/sources -d '{"language":"English", "version":"NIV", "content":["XGlkIE1BVCBVbmxvY2tlZCBMaXRlcmFsIEJpYmxlDQpcaWRlIFVURi04DQpcaCBNYXR0aGV3IA0KXHRvYzEgVGhlIEdvc3BlbCBBY2NvcmRpbmcgdG8gU3QuIE1hdHRoZXcNClx0b2MyIE1hdHRoZXcgDQpcdG9jMyBNYXQgDQpcbXQgVGhlIEdvc3BlbCBBY2NvcmRpbmcgdG8gU3QuIE1hdHRoZXcNClxjIDENClxwDQpcdiAxIFRoZSBib29rIG9mIHRoZSBnZW5lYWxvZ3kgb2YgSmVzdXMgQ2hyaXN0LCB0aGUgc29uIG9mIERhdmlkLCB0aGUgc29uIG9mIEFicmFoYW0uDQpcdiAyIEFicmFoYW0gd2FzIHRoZSBmYXRoZXIgb2YgSXNhYWMsIGFuZCBJc2FhYyB0aGUgZmF0aGVyIG9mIEphY29iLCBhbmQgSmFjb2IgdGhlIGZhdGhlciBvZiBKdWRhaCBhbmQgaGlzIGJyb3RoZXJzLCANClx2IDMgSnVkYWggdGhlIGZhdGhlciBvZiBQZXJleiBhbmQgWmVyYWggYnkgVGFtYXIsIFBlcmV6IHRoZSBmYXRoZXIgb2YgSGV6cm9uLCBIZXpyb24gdGhlIGZhdGhlciBvZiBSYW0sDQoNCg0K"]}'


AGT:

    curl -X POST -H "Authorization:bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.VwJyuxwIFMhHUJ5VamMli_WQUh23pGZDP8XTlxjk4og" http://127.0.0.1:8000/v1/autogeneratedtokens -d '{"language":"English", "version":"ULB", "revision":"1"}'

GENERATE CONCORDANCE:

    curl -X POST -H "Authorization:bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.VwJyuxwIFMhHUJ5VamMli_WQUh23pGZDP8XTlxjk4og" http://127.0.0.1:8000/v1/generateconcordance -d '{"language":"English", "version":"NIV"}'


GET CONCORDANCE:

    curl -X POST -H "Authorization:bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.VwJyuxwIFMhHUJ5VamMli_WQUh23pGZDP8XTlxjk4og" http://127.0.0.1:8000/v1/getconcordance -d '{"language":"English", "version":"NIV", "revision":"1", "token":"Ram"}'


curl -i -H "Authorization:bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2VsY2pvaG5zb24xMjNAZ21haWwuY29tIn0.COwWImiHEmy3TaNvP_GiBnvQgFsXVAn_CdaanBL1iKI" http://127.0.0.1:8000/v1/getbookwiseautotokens -d '{"sourcelang":"guj","version":"ULB","revision":"1","nbooks":[],"books":["GEN","LEV","NUM","DEU","JOS","JDG","RUT","EZR","NEH","EST","JOB","PSA","PRO","ECC","SNG","ISA","JER","LAM","EZK","DAN","HOS","JOL","AMO","OBA","JON","MIC","NAM","HAB","ZEP"]}'