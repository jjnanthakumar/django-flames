from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Flames
# Create your views here.
# creator "NANTHAKUMAR J J"
import copy
from collections import Counter


# <!-- Author:  Nanthakumar -->

def home(request):
    n1 = request.POST.get('n1')
    n2 = request.POST.get('n2')
    if request.method == "POST":
        f = Flames()
        if len(str(n1)) != 0 and len(str(n2)) != 0 and len(str(n1)) != len(str(n2)):
            f.save()
    if len(str(n1)) == 0 or len(str(n2)) == 0:
        messages.error(request, "Please ensure that you have given some text in both fields")
        return render(request, 'home.html')
    elif n1 == n2 and n1 != None and n2 != None:
        messages.error(request, "We cant guess your relation! Try initials combined with names.")
        return render(request, 'home.html')
    elif n1 == None and n2 == None:
        return render(request, 'home.html')
    else:

        str1 = n1
        str2 = n2
        str1 = str1.split()
        str2 = str2.split()
        str1 = [i for i in str1 if len(i) > 1]
        str2 = [i for i in str2 if len(i) > 1]
        str1 = ''.join(str1)
        str2 = ''.join(str2)
        str1 = str1.lower()
        str2 = str2.lower()
        a = sorted(str1)
        b = sorted(str2)
        freq1 = dict(Counter(a))
        freq2 = dict(Counter(b))
        c = copy.deepcopy(freq1)
        c1 = copy.deepcopy(freq2)
        for (char, count), (char1, count1) in zip(c.items(), c1.items()):
            if len(a) > len(b):
                if char1 in c.keys():
                    freq1[char1] = abs(c1[char1] - c[char1])
                    freq2[char1] = 0
                else:
                    freq2[char1] = 1
            else:
                if char in c1.keys():
                    freq1[char] = abs(c1[char] - c[char])
                    freq2[char] = 0
                else:
                    freq1[char] = 1
        res = sum(freq2.values()) + sum(freq1.values())
        if res != 0:
            pass
        else:

            return redirect('home')

        dic = {'F': "Friends", 'L': "Love", 'A': "Affection", 'M': "Marriage", 'E': "Enemy", 'S': "Sibling"}
        lst = ['F', 'L', 'A', 'M', 'E', 'S']
        new_lst = []
        for i in range(6, 0, -1):
            r = res % i
            if r != 0:
                if len(new_lst) == 1:
                    break
                if len(lst) == 0:
                    break
                lst.pop(r - 1)
                new_lst = lst[r - 1:]
                if r >= 2:
                    for r in range(r - 1):
                        new_lst.append(lst[r])
                lst = new_lst
            elif r == 0:
                if len(new_lst) == 1:
                    break
                if len(lst) == 0:
                    break
                lst.pop(-1)
                new_lst = lst[r:]
                lst = new_lst
        final = dic.get(''.join(lst), "Sorry")
        return render(request, 'home.html', {'result': final, 'successful_submit': True})
# <!-- Author:  Nanthakumar -->
