from django.shortcuts import render, redirect
from .form import ReviewForm, CommentForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    reviews = Review.objects.order_by("pk")
    page = request.GET.get('page')
    paginator = Paginator(reviews, '6')
    posts = paginator.get_page(page)
    context = {
        'reviews': reviews,
        'posts': posts,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()

    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


@login_required
def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment = review.comment_set.all()
    form = CommentForm()

    context = {
        "review": review,
        "comments": comment,
        "commentform": form,
    }

    return render(request, "reviews/detail.html", context)


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect("reviews:detail", review.pk)
        else:
            review_form = ReviewForm(instance=review)

        context = {
            "review_form": review_form,
        }

        return render(request, "reviews/update.html", context)
    else:
        return redirect("reviews:detail", review.pk)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
        return redirect("reviews:index")


@login_required
def like(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)

    return redirect("reviews:detail", review_pk)


@login_required
def comment_create(request, review_pk):
    review_data = Review.objects.get(id=review_pk)

    if request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review_data
            comment.user = request.user
            comment.save()

        return redirect('reviews:detail', review_data.pk)
    
    else:
        return redirect('accounts:login')


@login_required
def comment_delete(request, review_pk, comment_pk):
    review_data = Review.objects.get(id=review_pk)
    comment_data = review_data.comment_set.get(id=comment_pk)

    if request.user == comment_data.user:
        comment_data.delete()
    
    return redirect('reviews:detail', review_data.pk)


