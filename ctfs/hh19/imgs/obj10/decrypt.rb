require 'openssl'

KEY_LENGTH = 8 

def generate_key(seed)
  key = ""
  1.upto(KEY_LENGTH) do
    key += (((seed = (214013 * seed + 2531011) & 0x7fff_ffff) >> 16) & 0x0FF).chr
    end
  return key
end


def decrypt(data, key)
  c = OpenSSL::Cipher::DES.new('CBC') 
  c.decrypt
  c.key = key
  return (c.update(data) + c.final())
end

j = 0
i = 1575666001
while i > 1575658800
   i -= 1
   key = generate_key(i)
   begin
      File.open("#{i}.pdf","wb") do |outf|
        data = File.read("elf.pdf.enc")
        outf.write(decrypt(data, key))
   rescue; end
   end
end
