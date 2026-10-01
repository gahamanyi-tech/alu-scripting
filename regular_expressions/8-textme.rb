#!/usr/bin/env ruby
from = ARGV[0][/\[from:(.*?)\]/, 1]
to = ARGV[0][/\[to:(.*?)\]/, 1]
flags = ARGV[0][/\[flags:(.*?)\]/, 1]

puts "#{from},#{to},#{flags}"
