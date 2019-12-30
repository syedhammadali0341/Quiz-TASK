from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Test
from .models import Test_hard
from .models import Test_eng
from .models import Test_hard_eng
from .models import Test_datastructure
from .models import Test_hard_datastructure
import random
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'


# def test_page(request):
#     questions = list(Test.objects.all())
#     random.shuffle(questions)
#     object_list = questions[:]
#     return render(request, 'General_knowledge.html', {"Test": questions})
#     def test_page1():
#         questions1 = Test_hard.objects.all()
#
#         return render(request, 'General_knowledge.html', {"Test_hard": questions1})
#     test_page1()
#
#
# if __name__ == '__main__':
#     test_page1(request)

def test_page(request):
    questions =list(Test.objects.all())
    random.shuffle(questions)
    object_list = questions[:]
    questions1 =list( Test_hard.objects.all())
    random.shuffle(questions1)
    return render(request, 'General_knowledge.html', {"Test": questions,"Test_hard": questions1})
    # def test_page1(request):
    #     questions1 = Test_hard.objects.all()
    #     return render(request, 'General_knowledge.html', {"Test_hard": questions1})
    # return  test_page1(request)

# return test_page1(request),test_page(request)


#,{"Test_hard": questions1}
# def test_page(request):
#     questions= Test.objects.all()
#     return render(request,'General_knowledge.html', {"Test": questions})
def test_page1(request):
    questions = Test_hard.objects.all()
    return render(request, 'General_knowledge1.html', {"Test_hard": questions})


# def test_page1(request):
#      questions1= Test_hard.objects.all()
#      return render(request,'General_knowledge1.html', {"Test_hard": questions1})
def test_page2(request):
        questions = list(Test_eng.objects.all())
        random.shuffle(questions)
        object_list = questions[:]
        questions1 = list(Test_hard_eng.objects.all())
        random.shuffle(questions1)
        return render(request, 'General_knowledge2.html', {"Test_eng": questions, "Test_hard_eng": questions1})

    # def test_page2(request):
#     questions= Test_eng.objects.all()
#     return render(request,'General_knowledge2.html', {"Test_eng": questions})
# def test_page3(request):
#     questions1= Test_hard_eng.objects.all()
#     return render(request,'General_knowledge3.html', {"Test_hard_eng": questions1})
# def test_page4(request):
#     questions= Test_datastructure.objects.all()
#     return render(request,'General_knowledge4.html', {"Test_datastructure": questions})
# def test_page5(request):
#     questions1= Test_hard_datastructure.objects.all()
#     return render(request,'General_knowledge5.html', {"Test_hard_datastructure": questions1})

def test_page4(request):
    questions = list(Test_datastructure.objects.all())
    random.shuffle(questions)
    object_list = questions[:]
    questions1 = list(Test_hard_datastructure.objects.all())
    random.shuffle(questions1)
    return render(request, 'General_knowledge4.html', {"Test_datastructure": questions, "Test_hard_datastructure": questions1})


def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Test.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        eff = (score/total)*100
    return render(request,
        'result.html',
        {'score':score,
        'eff':eff,
        'total':total})


@login_required
def profile(request):
    return render(request, 'profile.html')