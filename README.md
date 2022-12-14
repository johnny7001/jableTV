# jableTV
jableTV 網站爬取, API相關
****

# 使用前請新進入虛擬環境
輸入以下指令  
```
cd .venv/bin  
source activate  
```
# API
主網址 = http://127.0.0.1:3123  
# 功能介紹
- 加上番號可從資料庫取得影片資訊  
```
url = http://127.0.0.1:3123/videos/<number>     
ex: http://127.0.0.1:3123/videos/pppe-052  
```

```json
{
    "actress": "['楪カレン']",
    "dir_name": "pppe-052",
    "header": "PPPE-052 隣家のゴミ部屋へ苦情を言ったらコドおじが性欲モンスター化！異臭の中で絶対に逃がさない抜かずの孕ませ絶倫ホールド中出し 楪可憐",
    "id": 11,
    "short_url": "https://assets-cdn.jable.tv/contents/videos_screenshots/25000/25458/25458_preview.mp4",
    "status": 0,
    "tag": "['凌辱強暴', '制服誘惑', '角色劇情', '少女', '巨乳', '中出', '口爆', '乳交', '凌辱', '強姦', '水着', '校服']",
    "url": "https://jable.tv/videos/pppe-052/"
}
```
- 輸入video status 可獲取該代碼所有影片的url (代碼0: 0 尚未下載,  1 正在下載, 2 下載完成)
```
url = http://127.0.0.1:3123/status/<status>
```