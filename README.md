# Jekyll code for VDA-lab website

## Making changes

The changes have to be uploaded to the ESAT webserver, because jekyll is not installed there. This means that we had to set the base_url variable in `_config.yml` to `~jaerts`

After making changes locally:
* `jekyll build`
* `tar -cvzf _site vda-lab.tar.gz`
* `scp vda-lab.tar.gz ssh.esat.kuleuven.be:/users/stadius/jaerts/`

On the server:
* `tar -xvzf vda-lab.tar.gz`
* `rm -r -f public_html`
* `mv _site public_html`
