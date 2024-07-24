# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type,sender,recipient):
  opened_card_file = open(f"{card_type}.txt")
  renamed_card_file = open(f"{sender}_generic.txt",'w')
  try:
    renamed_card_file.write(f'Dear {recipient} \n')
    renamed_card_file.write(opened_card_file.read())
    renamed_card_file.write(f'\nSincerely, {sender} \n')
    yield renamed_card_file
  finally:
    opened_card_file.close()
    renamed_card_file.close()
  
with generic('thankyou_card','Mwenda','Amanda') as amanda_thankyou_card:
  print("Card Generated!")

with open('Mwenda_generic.txt','r') as first_order:
  print(first_order.read())

class personalized:
  def __init__(self,sender,receiver):
    self.sender = sender
    self.personalized_file = open(f'{sender}_personalized.txt','w')
    self.receiver = receiver
  def __enter__(self):
    self.personalized_file.write(f'Dear {self.receiver}\n')
    return self.personalized_file
  def __exit__(self,exc_type,exc_value,Traceback):
    self.personalized_file.write(f'Sincerely, {self.sender}')
    self.personalized_file.close()
with personalized('John','Michael') as first_personalized_card:
  first_personalized_card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

  with generic('happy_bday','Josiah','Remy') as Jcard1, personalized('Josiah','Esther') as Jcard2:
    Jcard2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old! ")
  
with open('Josiah_generic.txt','r') as jcard, open('Josiah_personalized.txt','r') as jcardtwo:
  print(jcard.read())
  print(jcardtwo.read())
