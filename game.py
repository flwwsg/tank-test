import grequests

req_list = [  # 请求列表
    # grequests.get('http://httpbin.org/get?a=1&b=2'),
    grequests.post('https://admin.tepleton.info/twallet_fund/api/v1/product/prize/app/prize', Authorization={
        'eyJhbGciOiJIUzUxMiJ9.eyJhdXRob3JpdGllcyI6W3siYXV0aG9yaXR5Ijoibm9ybWFsIn1dLCJ1aWQiOjg5LCJpZCI6ImI0YWFhMTQ4MzMzMzk4NDBlMzRjMjY4ZjA0ZDRhNjY3OTY3Yjk2YzYzOTNlYjA4YTNlN2RlM2M1ZjAyZTJlZGUiLCJzdWIiOiJUQU5LOEJDQUIxOEI0RSIsImV4cCI6MTU5MDI5MDUyMH0.R_Kk6U8SIsiGCq39nqnXpZtHXde6TXrBh8CflUYTYXN7_lWO490cla8JVARkoopf6-gp7saohgQd3aLEXw6yWA'}),
    # grequests.put('http://httpbin.org/post', json={'a': 1, 'b': 2}),
]
res_list = grequests.map(req_list)  # 并行发送，等最后一个运行完后返回
print(res_list[0].text)  # 打印第一个请求的响应文本
