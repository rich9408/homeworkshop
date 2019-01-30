from django.shortcuts import render


    
def info(request):
    persons = {
        '홍길동':'28',
        '김길동':'128',
        '박길동':'228'
    }
    keys = persons.keys()
    values = persons.values()
    return render(request, "info.html", {"keys":keys}, {"values":values})
    
def student(request, name):
    s_list = {
        "홍길동":22,
        "박길동":23,
        "김길동":25
    }
    age = s_dict.get(name)
    return render(request,"student.html",{"name":name},{"age":age})
    