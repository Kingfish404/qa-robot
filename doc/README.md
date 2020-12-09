# Document

## 问答接口

请求功能 | 接口地址 | 请求方式 | 参数 | 返回结果
--- | --- | --- | --- | ---
文字提问与回答 | /msgAsk | POST | question | JSON-1 |

JSON-1  
```json  
// JSON-1
{
  "data": {
    "answer": ""
  },
  "code": "200",    // 200:成功，400：请求错误，404：请求不存在
  "msg":"SUCCESS"   // "SUCCESS":成功，"ERROR:错误描述":通用错误,"FAILD:失败描述":通用失败描述
}
```