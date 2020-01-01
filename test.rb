require 'socket'

server = TCPServer.new('0.0.0.0', 4000)

loop do

  # Wait for a connection
  socket = server.accept
  STDERR.puts "Incoming Request"

  # Read the HTTP request. We know it's finished when we see a line with nothing but \r\n
  http_request = ""
  while (line = socket.gets) && (line != "\r\n")
    http_request += line 
  end
  STDERR.puts http_request
  socket.close
end  
