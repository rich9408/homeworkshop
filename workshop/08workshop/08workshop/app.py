from flask import Flask, render_template

app = Flask(__name__)


    
@app.route("/dictionary/<string:word>")
def dictionary(word):
    words = {
		'apple' : '사과',
		'germ' : '세균',
		'vertical' : '수직의',
		'horizontal' : '가로의',
		'assemble' : '집합시키다'
		}
    if word in words:
        word = word+"(은)는" +str(words[word]) + " 입니다!"
    else:
        word = f"{word}(은)는 나만의 단어장에 없습니다!"
        
    return render_template("dictionary.html", word=word)

def dictionary2(word):
    mydict = {
		'apple' : '사과',
		'germ' : '세균',
		'vertical' : '수직의',
		'horizontal' : '가로의',
		'assemble' : '집합시키다'
		}
	result = mydict.get(word)
    if result:
        result = f"{word} : {result}"
    else:
        result = f"{word}은(는) 단어장에 없는 단어"
		
	return result
		
		
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)