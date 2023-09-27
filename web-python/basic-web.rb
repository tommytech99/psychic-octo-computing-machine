require 'webrick'

server = WEBrick::HTTPServer.new(Port: 8000)

server.mount_proc('/') do |req, res|
  res.content_type = 'text/plain'
  res.body = 'Hello World!'
end

trap('INT') { server.shutdown }

server.start
