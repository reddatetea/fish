class Address:
    detail = '广州'
    post_code ='510660'
    def info(self):
        #print(detail)
        print(Address.detail)
        print(Address.post_code)
print(Address.detail)
addr = Address()
addr.info()
Address.detail ='佛山'
Address.post_code ='460110'
addr.info()