#!/usr/bin/env ruby
require 'net/ssh/shell'

puts "Bundling up the site"
`tar -czf t.tar.gz _site`

puts "Calculating local md5"
local_md5 = `md5 t.tar.gz`.split(/ = /)[1]

puts "Copying the site to the server"
`scp t.tar.gz jaerts@ssh.esat.kuleuven.be:/users/stadius/jaerts/`

Net::SSH.start('ssh.esat.kuleuven.be','jaerts') do |ssh|
  puts "Extracting bundle on server"
  ssh.exec "rm -r -f public_html; tar -xvf t.tar.gz; mv _site public_html; rm -f t.tar.gz"
end

puts "Removing local tar file"
`rm -f t.tar.gz`
