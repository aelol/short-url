endpoint

- http://112.74.83.185/raw

	- allowed method 
			
			POST
	- content type

			application/json
	- fields

		- sig
			
				msg = request_url

				key = b'1800cc75b39a99c0258b573f83a92e65'

				signature = hmac.new(key)
				signature.update(msg)
				signature.hexdigest()
				
				eg:"a512c6aad0094ad88a1c8454a5c13122"
		- raw

				Raw url

				*protocol required*
				
				eg:"https://www.edyd.cn"
				
		- json example [ utf-8 required ]

				{
					"raw":"http://www.edyd.cn",
					"sig":"a512c6aad0094ad88a1c8454a5c13122"
				}
				
	- return data [ json ]

			{
				 "short": "s.edyd.cn/UrfRq3",
                 "raw": "http://www.sina.com",
                 "last_update": "2016-12-14 14:59:20"
			}
	- error

		- 'ACCEPT JSON ONLY'

				提交的不是json
		- 'EMPTY REQUEST BODY'
		  
		  'A VALID JSON IS REQUIRED'

				提交的json不合法
		- 'MALFORMED JSON'
        
        	'JSON INVALID OR NOT ENCODED AS UTF-8'
        	
        		json不合法 或encode不是utf-8
       - 'BAD SIGNATURE', 'SIG INVALID'

       			签名错

    			
