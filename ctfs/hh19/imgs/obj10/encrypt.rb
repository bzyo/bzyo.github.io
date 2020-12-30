require 'openssl'

KEY_LENGTH = 8 

def generate_key(seed)
  key = ""
  1.upto(KEY_LENGTH) do
    key += (((seed = (214013 * seed + 2531011) & 0x7fff_ffff) >> 16) & 0x0FF).chr
    end
  return key
end

def encrypt(data)
  c = OpenSSL::Cipher::DES.new('CBC')
  c.encrypt
  seed = 1577382983
  key = generate_key(seed)
  c.key = key
  #return (c.update(data) + c.final()).unpack('H*')
  return (c.update(data) + c.final())
end


#if(!ARGV[0])
#  puts("usage: ruby encrpyt.rb <data>")
#  exit
#end

#data = ARGV[0]

seed = 1577382983
key = generate_key(seed)


puts seed
puts("Generated key: #{key.unpack('H*')}")
#puts encrypt(data)
File.open("yo.pdf.enc","wb") do|outf|
  data = File.read("yo.pdf")
  outf.write(encrypt(data))
end
