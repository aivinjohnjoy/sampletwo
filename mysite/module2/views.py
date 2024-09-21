from django.shortcuts import render
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2195185410.
from django.http import HttpResponse
from django.shortcuts import render
from . models import moovie_tablepy

# Create your views here.

#list api
def print_hello(request):
   #Moview list with dictionary of movies inside.
    movie_data= moovie_tablepy.objects.all()
    #print(movie_data)
    return render(request,'list.html', {'movies': movie_data})


#details api
def details(request):
        return render(request,'details.html')


#Add api
def add(request):
    if request.POST:
        #print(request.POST)
        title_post=request.POST.get('Title')
        year_post=request.POST.get('Year')
        sum_post=request.POST.get('sum')
        success_post=request.POST.get('success')
        if success_post=='yes':
            success_post=True
        elif success_post=='no':
            success_post=False
        else:
            success_post= False

        print(title_post,year_post,sum_post,success_post)
        movie_tablepy_obj=moovie_tablepy(Title=title_post,Year=year_post,Summary=sum_post,Success=success_post)
        movie_tablepy_obj.save()

    return render(request,'add.html')



#edit api
def edit(request,pk):
    movie_obj=moovie_tablepy.objects.get(id=pk)
    

    if request.POST:
        #print(request.POST)
        title_post=request.POST.get('Title')
        year_post=request.POST.get('Year')
        sum_post=request.POST.get('sum')
        success_post=request.POST.get('success')
        if success_post=='yes':
            success_post=True
        elif success_post=='no':
            success_post=False
        else:
            success_post= False

        
        movie_tablepy_obj=moovie_tablepy.objects.get(id=pk)
        movie_tablepy_obj.Title=title_post
        movie_tablepy_obj.Year=year_post
        movie_tablepy_obj.Summary=sum_post
        movie_tablepy_obj.Success=success_post
        movie_tablepy_obj.save()
        print(movie_tablepy_obj)
        movie_data= moovie_tablepy.objects.all()
        return render(request,'list.html',{'movies': movie_data})
    
    
    return render(request,'edit.html',{'movie': movie_obj} )





#delete api
def delete(request,pk):
    movie_obj=moovie_tablepy.objects.get(id=pk)
    print(movie_obj)
    movie_obj.delete()
    movie_data= moovie_tablepy.objects.all()
    return render(request,'list.html',{'movies': movie_data})    

