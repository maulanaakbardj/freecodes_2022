class SayHello:
  def hello(self): 
    self.text = '//x?!&$+#6#&$53'.replace('//x?!', 'H')
    self.text = self.text.replace('&$+#6', 'E')
    self.text = self.text.replace('#&$53', 'LL')
    return self.text+'#3$)38'.replace('#3$)38', '0')

class SayWord:
  def word(self):
    self.text = ('World')
    result =''
    for x in self.text:
      result = result+x
    result = result.upper()
    return result
      
hello = SayHello() 
word = SayWord()

text =''
hello = hello.hello()
for abjad in hello:
  text = text+abjad
text = text+'_'
word = word.word()
for abjad in word:
 text = text+abjad
text = text.replace('`','')
print(text)