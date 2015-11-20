# Jekyll code for VDA-lab website

## Creating new blog posts

There are two ways to create new blog posts, either using `_drafts` first, or straight in the `_posts` directory. We'll just use the `_posts` directory... Posts are written in markdown.

Creating a new blog post in the repo involves the following steps:

* Run `jekyll serve` (if you don't have jekyll installed yet, see jekyllrb.com)
* Create a new file in the `_posts` directory

  * The file name should be the date plus title, in the following format `YYYY-MM-DD-this-is-the-title.md`
  * The top of the file must include the *front matter*. These lines trigger the jekyll engine to parse that file as a blog post. The front matter should include:

    1. `layout`: should be `post`
    1. `title`
    1. `date`
    1. `author`: your name
    1. `tags`: list of tags. Please try to reuse the tags already available on vda-lab.be/posts.html

* Any pictures to be included: add these to the `assets` directory, and make sure that they are set to `644` permissions. You can refer to these images in your post using `{{ site.baseurl }}/assets/your-picture.png`.

While you're making these changes, the `jekyll serve` will pick up any saved changes and rebuild the html pages. Check out `http://localhost:4000/~jaerts/` to see you changes. Note that you have to use the `~jaerts` subdirectory there...

## Creating pages
Any page created will by default show up in the header of the website; the one listing "Home", "People", "Portfolio", etc. To prevent a file from appearing there, add `exclude: true` in the front matter.

## Pull requests and merges



## Deploying updates from bitbucket to the actual webserver

The changes have to be uploaded to the ESAT webserver, because jekyll is not installed there. This means that we had to set the base_url variable in `_config.yml` to `~jaerts`

After making changes locally:

* `jekyll build`
* `tar -cvzf _site vda-lab.tar.gz`
* `scp vda-lab.tar.gz ssh.esat.kuleuven.be:/users/stadius/jaerts/`

On the server:

* `tar -xvzf vda-lab.tar.gz`
* `rm -r -f public_html`
* `mv _site public_html`

Or now, just run `deploy.rb`.

## Merging the teaching subrepos

I'm keeping the teaching material in separate repositories per course. To manage these together with the main public_html (based on [this blog post](https://developer.atlassian.com/blog/2015/05/the-power-of-git-subtree/) and [this one](https://medium.com/@v/git-subtrees-a-tutorial-6ff568381844)):

### Starting from the course

#### Making changes to a course

As usual, just clone the course-specific repository (e.g. jandot/i0u19a), make changes, commit, and push to bitbucket.

#### Combining the subrepos into the main public_html

Using `git subtree`. For each course:

* `git remote add i0u19a git@bitbucket.org:jandot/i0u19a.git`
* `git subtree add --prefix teaching/i0u19a/ i0u19a master`

#### Pulling changes from the subrepo

`git subtree pull --prefix teaching/i0u19a/ i0u19a master`

### Making changes to a course from within public_html

#### Making changes to a course
Just make the changes in the subdirectory of the course within the `public_html` project. Then `git add`, `git commit` and `git push` to the `public_html` repository. At this point, the changes will not be in the course-specific repo yet.

#### Pushing those changes to the course-specific repository

`git subtree push --prefix teaching/i0u19a/ i0u19a master`

### Organizing the posts and pages from the subrepos

In order to have only the main blog posts appear in the website, add `categories: main` to each blog post. The posts in each course should have the name of the course as the category: e.g. `categories: i0u19a`.

The liquid code in the posts.md files mention `site.categories.i0u19a`, which will return all blog posts with category `i0u19a`.
