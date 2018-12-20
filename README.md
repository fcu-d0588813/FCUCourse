# FCUCourse
#### 參考:https://yaoandy107.github.io/line-bot-tutorial/ #### 
Procfile：web: {語言} {檔案}，這邊語言為 python，要自動執行的檔案為 app.py，因此我們改成 web: python app.py  
requirements.txt：列出所有用到的套件，heroku 會依據這份文件來安裝需要套件  
app.py (主程式): 可透過修改程式裡的 handle_message() 方法內的程式碼來控制機器人的訊息回覆
