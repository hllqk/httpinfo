import json
data={
    'code':200,
    'msg':'成功',
    'ip':'',
}
print(json.dumps(data,ensure_ascii=False,indent=4))