from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Project, Comment
from .forms import CommentForm

# Create your views here.


class ProjectList(generic.ListView):
    """
    Returns all published projects in :model:`projects.Project`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`projects.Project`
    ``paginate_by``
        Number of projects per page.

    **Template:**

    :template `projects/index.html`
    """
    queryset = Project.objects.filter(status=1)
    template_name = "projects/index.html"
    paginate_by = 6


def project_detail(request, slug):
    """
    Display an individual :model:`projects.Project`.

    **Context**

    ``project``
        An instance of :model:`projects.Project`.

    **Template:**

    :template:`projects/project_detail.html`
    """
    queryset = Project.objects.filter(status=1)
    project = get_object_or_404(queryset, slug=slug)
    next_project = Project.objects.filter(
        created_on__gt=project.created_on).last()
    previous_project = Project.objects.filter(
        created_on__lt=project.created_on).first(
            )
    comments = project.comments.all().order_by("-created_on")
    comment_count = project.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.project = project
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "projects/project_detail.html",
        {
            "project": project,
            "technologies": project.technologies.split(','),
            "next_project": previous_project,
            "previous_project": next_project,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``project``
        An instance of :model:`projects.Project`.
    ``comment``
        A single comment related to the project.
    ``comment_form``
        An instance of :form:`projects.CommentForm`
    """
    if request.method == "POST":

        queryset = Project.objects.filter(status=1)
        project = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('project_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``project``
        An instance of :model:`projects.Project`.
    ``comment``
        A single comment related to the project.
    """
    queryset = Project.objects.filter(status=1)
    project = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('project_detail', args=[slug]))
