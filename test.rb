require 'sinatra'

# By default Sinatra will return the string as the response.
get '/' do
  send_file 'test.html'
end