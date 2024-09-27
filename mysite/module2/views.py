from django.shortcuts import render, get_object_or_404, redirect
from .models import moovie_tablepy

# List API to display all movies in the database
def list(request):
    # Retrieve all movie objects from the database
    movie_data = moovie_tablepy.objects.all()
    
    # Pass movie data to the 'list.html' template to display the list of movies
    return render(request, 'list.html', {'movies': movie_data})


# API to render the movie details page (empty for now)
def details(request):
    # Simply render the 'details.html' template (this can be enhanced with specific movie details later)
    return render(request, 'details.html')


# Add API to handle adding new movies
def add(request):
    # Check if the request is a POST request (form submission)
    if request.POST:
        # Retrieve form data sent via POST
        title_post = request.POST.get('Title')  # Movie title
        year_post = request.POST.get('Year')    # Release year
        sum_post = request.POST.get('sum')      # Movie summary
        success_post = request.POST.get('success')  # Movie success status (yes/no)
        
        # Convert success radio button value to a boolean
        if success_post == 'yes':
            success_post = True
        elif success_post == 'no':
            success_post = False
        else:
            success_post = False
        
        # Retrieve the uploaded image from the form
        img_post = request.FILES.get('filename')

        # Debug print the uploaded image
        print(img_post)
        
        # Create a new movie object and save it to the database
        movie_tablepy_obj = moovie_tablepy(
            Title=title_post,
            Year=year_post,
            Summary=sum_post,
            Success=success_post,
            Img=img_post
        )
        movie_tablepy_obj.save()  # Save the new movie object to the database

    # Render the 'add.html' template to display the add movie form
    return render(request, 'add.html')


# Edit API to handle editing existing movies
def edit(request, pk):
    # Retrieve the specific movie object based on its primary key (pk)
    movie_obj = get_object_or_404(moovie_tablepy, id=pk)

    # Check if the request is a POST request (form submission for editing)
    if request.POST:
        # Retrieve form data sent via POST
        title_post = request.POST.get('Title')  # Updated movie title
        year_post = request.POST.get('Year')    # Updated release year
        sum_post = request.POST.get('sum')      # Updated summary
        success_post = request.POST.get('success')  # Updated success status

        # Convert success radio button value to a boolean
        if success_post == 'yes':
            success_post = True
        elif success_post == 'no':
            success_post = False
        else:
            success_post = False
        
        # Retrieve the updated image from the form (if provided)
        img_post = request.FILES.get('filename')

        # Update the movie object with the new data
        movie_obj.Title = title_post
        movie_obj.Year = year_post
        movie_obj.Summary = sum_post
        movie_obj.Success = success_post

        # Update the image only if a new image is uploaded
        if img_post:
            movie_obj.Img = img_post
        
        # Save the updated movie object back to the database
        movie_obj.save()

        # Debug print to confirm the update
        print(movie_obj)
        
        # After editing, display the updated list of movies
        movie_data = moovie_tablepy.objects.all()
        return render(request, 'list.html', {'movies': movie_data})

    # Render the 'edit.html' template with the existing movie data for editing
    return render(request, 'edit.html', {'movie': movie_obj})


# Delete API to handle removing a movie from the database
def delete(request, pk):
    # Retrieve the specific movie object based on its primary key (pk)
    movie_obj = get_object_or_404(moovie_tablepy, id=pk)
    
    # Debug print to confirm which movie is being deleted
    print(movie_obj)
    
    # Delete the movie object from the database
    movie_obj.delete()

    # After deletion, retrieve and display the updated list of movies
    movie_data = moovie_tablepy.objects.all()
    return render(request, 'list.html', {'movies': movie_data})
