from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import NotForm
from .models import Not
from django.db.models import Q


class mantıkProje:

    def base(self):
        return render(self,"anasayfa.html")
    def notOlustur(self):
        not_form = NotForm()
        if self.method == "POST":
            post_form = NotForm(self.POST)
            if post_form.is_valid():
                created_post = post_form.save(commit=True)
                return HttpResponseRedirect("/")
        return render(self,"not_create.html",context={'form':not_form})

    def not_list(self):
        q = self.GET.get('q',None)
        posts_list = Not.objects.all()

        if q:
            posts_list = posts_list.filter(Q(baslık__icontains=q))


        return render(self,'not_lists.html',context={'post_list':posts_list})

    def not_detail(self,pk):
         post_not = get_object_or_404(Not,pk=pk)
         return render(self,"detail.html",context={"post":post_not})
    def not_delete(self,pk):
        post = get_object_or_404(Not,pk=pk)
        post.delete()
        return HttpResponseRedirect("/")


