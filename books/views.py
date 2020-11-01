from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Chapter, Exercise
from shopping_cart.models import Order, OrderItem

OWNED = 'owned'
IN_CART = 'in_cart'
NOT_IN_CART = 'not_in_cart'




def check_book_relationship(request, book):
    if book in request.user.userlibrary.book_list():
        return OWNED
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        order_item_qs = OrderItem.objects.filter(book=book)
        if order_item_qs.exists():
            order_item = order_item_qs[0]
            if order_item in order.items.all():
                return IN_CART
    return NOT_IN_CART




def book_list(request):
    # main display
    queryset = Book.objects.all()
    context = {
        'queryset' : queryset
    }
    return render(request, "book_list.html", context)

@login_required
def book_detail(request, slug):
    # chapters
    book = get_object_or_404(Book, slug=slug)
    book_status = check_book_relationship(request, book)
    context = {
        'book' : book,
        'book_status': book_status
    }
    return render(request, "book_detail.html", context)


@login_required
def chapter_detail(request, book_slug, chapter_number):
    chapter_qs = Chapter.objects \
        .filter(book__slug=book_slug) \
        .filter(chapter_number=chapter_number)
    if chapter_qs.exists():
        context = {
            'chapter': chapter_qs[0]
        }
        return render(request, "chapter_detail.html", context)
    return Http404


@login_required
def exercise_detail(request, book_slug, chapter_number, exercise_number):
    exercise_qs = Exercise.objects \
        .filter(chapter__book__slug=book_slug) \
        .filter(chapter__chapter_number=chapter_number) \
        .filter(exercise_number=exercise_number)
    if exercise_qs.exists():
        context = {
            'exercise': exercise_qs[0]
        }
        return render(request, "exercise_detail.html", context)
    return Http404


def ebooks(request):
    ebooks = Ebook.objects.all()
    paginator = Paginator(ebooks, 12)
    try:
        page = request.GET['page']
    except:
        page = 1
    ebooks = paginator.get_page(page)
    return render(request, 'exercise_detail.html', {  ##ebook/ebooks.html
		'books': books,
		})

def ebook(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk = ebook_id)
    comments = ebook.comment_set.all()
    return render(request, 'exercise_detail.html', {
		'book' : book,
        'comments' : comments,
		})

def comment(request, ebook_id):
    if request.method == 'POST':
        user = auth.get_user(request)
        ebook = get_object_or_404(Ebook, pk = ebook_id)

        # create the comment
        comment = Comment()
        comment.body = request.POST['body']
        comment.pub_time = timezone.datetime.now()
        comment.ebook = ebook
        comment.user = user
        comment.save()

        return redirect('ebook', ebook_id)
    else:
        return redirect('home')