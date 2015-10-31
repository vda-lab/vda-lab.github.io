# Jekyll code for VDA-lab website

## Creating new blog posts

There are two ways to create new blog posts, either using `_drafts` first, or straight in the `_posts` directory. We'll just use the `_posts` directory... Posts are written in markdown.

Creating a new blog post in the repo involves the following steps:

1. Run `jekyll serve` (if you don't have jekyll installed yet, see jekyllrb.com)
1. Create a new file in the `_posts` directory

  * The file name should be the date plus title, in the following format `YYYY-MM-DD-this-is-the-title.md`
  * The top of the file must include the *front matter*. These lines trigger the jekyll engine to parse that file as a blog post. The front matter should include:
  
    1. `layout`: should be `post`
    1. `title`
    1. `date`
    1. `author`: your name
    1. `tags`: list of tags. Please try to reuse the tags already available on vda-lab.be/posts.html
    
1. Any pictures to be included: add these to the `assets` directory, and make sure that they are set to `644` permissions. You can refer to these images in your post using `{{ site.baseurl }}/assets/your-picture.png`.

While you're making these changes, the `jekyll serve` will pick up any saved changes and rebuild the html pages. Check out `http://localhost:4000/~jaerts/` to see you changes. Note that you have to use the `~jaerts` subdirectory there...

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
